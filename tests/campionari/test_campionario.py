"""Il kit zip è coerente con i sorgenti e genera i 4 fogli. python -m unittest discover -s tests/campionari -v"""
import hashlib, json, os, subprocess, sys, tempfile, unittest, zipfile
import PIL

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


if __name__ == "__main__":
    unittest.main()
