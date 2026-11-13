"""Il kit zip è coerente con i sorgenti e genera i 4 fogli. python -m unittest discover -s tests/campionari -v"""
import hashlib, json, os, subprocess, sys, tempfile, unittest, zipfile
import PIL
from PIL import Image, ImageDraw
import runpy
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, "campionari")
ZIP = os.path.join(DIR, "kit-campionari-v1.zip")


def sha(b):
    return hashlib.sha256(b).hexdigest()


class TestKit(unittest.TestCase):
    def test_zip_allineato_ai_sorgenti(self):
        with zipfile.ZipFile(ZIP) as z:
            for nome in ["campionario.py", "fonts.json"] + ["esempi/" + f for f in os.listdir(os.path.join(DIR, "esempi"))]:
                with open(os.path.join(DIR, nome), "rb") as f:
                    self.assertEqual(sha(z.read(nome)), sha(f.read()), nome)

    def test_ogni_font_ha_file_e_licenza(self):
        with zipfile.ZipFile(ZIP) as z:
            nomi = set(z.namelist())
        with open(os.path.join(DIR, "fonts.json"), encoding="utf-8") as f:
            fonts = json.load(f)
        for fam, info in fonts.items():
            self.assertIn("font/" + info["file"], nomi, fam)
        self.assertTrue(any(n.startswith("font/licenze/OFL-") for n in nomi))

    def test_quattro_modi(self):
        # -I excludes user-site packages. Expose the already-imported Pillow
        # location, as in tests/engine, without enabling repo/cwd imports.
        pillow_site = os.path.dirname(os.path.dirname(os.path.abspath(PIL.__file__)))
        bootstrap = ("import sys,runpy;sys.path.insert(0," + repr(pillow_site)
                     + ");sys.argv=sys.argv[1:];runpy.run_path(sys.argv[0],run_name='__main__')")
        with tempfile.TemporaryDirectory() as t:
            with zipfile.ZipFile(ZIP) as z:
                z.extractall(t)
            for modo in ("font", "palette", "layout", "combo"):
                out = os.path.join(t, modo + ".png")
                r = subprocess.run([sys.executable, "-I", "-c", bootstrap, os.path.join(t, "campionario.py"),
                                    os.path.join(t, "esempi", modo + ".json"), out], cwd=t, capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertGreater(os.path.getsize(out), 10000)


    def test_foto_dal_kit_integrita_ritaglio_e_protezione(self):
        pillow_site = os.path.dirname(os.path.dirname(os.path.abspath(PIL.__file__)))
        bootstrap = ("import sys,runpy;sys.path.insert(0," + repr(pillow_site)
                     + ");sys.argv=sys.argv[1:];runpy.run_path(sys.argv[0],run_name='__main__')")
        with tempfile.TemporaryDirectory() as t:
            with zipfile.ZipFile(ZIP) as z:
                z.extractall(t)
            photo = os.path.join(t, "sintetica.png")
            fixture = Image.new("RGB", (2400, 1200), "blue")
            ImageDraw.Draw(fixture).rectangle((800, 0, 1599, 1199), fill="red")
            fixture.save(photo)
            original = Path(photo).read_bytes()
            digest = sha(original)
            for modo in ("layout", "combo"):
                spec = os.path.join(t, "esempi", modo + ".json")
                with open(spec, encoding="utf-8") as f:
                    data = json.load(f)
                data["foto"] = "../sintetica.png"
                Path(spec).write_text(json.dumps(data), encoding="utf-8")
                out = os.path.join(t, modo + ".png")
                cmd = [sys.executable, "-I", "-c", bootstrap, os.path.join(t, "campionario.py"), spec]
                r = subprocess.run(cmd + [out], cwd=os.path.dirname(t), capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertIn("SHA-256 originale prima: " + digest, r.stdout)
                self.assertIn("SHA-256 originale dopo: " + digest, r.stdout)
                with Image.open(out) as sheet:
                    # Centro del riquadro L1: rosso; bordo sinistro: blu.
                    # Verifica foto presente, ritaglio centrato, colori conservati.
                    self.assertEqual(sheet.getpixel((180, 324)), (255, 0, 0))
                    self.assertEqual(sheet.getpixel((50, 324)), (0, 0, 255))
                rejected = subprocess.run(cmd + [photo], capture_output=True, text=True)
                self.assertNotEqual(rejected.returncode, 0)
                self.assertIn("sovrascrivere", rejected.stderr)
                self.assertEqual(Path(photo).read_bytes(), original)
            # Anche un alias hard link non deve consentire di scrivere sull'originale.
            alias = os.path.join(t, "alias.png")
            os.link(photo, alias)
            rejected = subprocess.run(cmd + [alias], capture_output=True, text=True)
            self.assertNotEqual(rejected.returncode, 0)
            self.assertEqual(Path(photo).read_bytes(), original)

    def test_copia_ridotta_orientamento_e_foto_invalida(self):
        module = runpy.run_path(os.path.join(DIR, "campionario.py"))
        with tempfile.TemporaryDirectory() as t:
            photo = Path(t) / "orientata.jpg"
            fixture = Image.new("RGB", (1600, 800), "red")
            exif = fixture.getexif()
            exif[274] = 6  # Rotazione EXIF di 90 gradi.
            fixture.save(photo, exif=exif)
            original = photo.read_bytes()
            reduced = module["carica_foto"](photo)
            self.assertEqual(reduced.size, (400, 800))
            self.assertEqual(photo.read_bytes(), original)
            spec = Path(t) / "spec.json"
            spec.write_text(json.dumps({"modo": "combo", "foto": "manca.jpg"}), encoding="utf-8")
            out = Path(t) / "out.png"
            with self.assertRaises(FileNotFoundError):
                module["main"](spec, out)
            self.assertFalse(out.exists())


if __name__ == "__main__":
    unittest.main()
