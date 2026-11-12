"""Il kit zip è coerente con i sorgenti e genera i 4 fogli. python -m unittest discover -s tests/campionari -v"""
import hashlib, json, os, subprocess, sys, tempfile, unittest, zipfile

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
        for fam, info in json.load(open(os.path.join(DIR, "fonts.json"), encoding="utf-8")).items():
            self.assertIn("font/" + info["file"], nomi, fam)
        self.assertTrue(any(n.startswith("font/licenze/OFL-") for n in nomi))

    def test_quattro_modi(self):
        with tempfile.TemporaryDirectory() as t:
            zipfile.ZipFile(ZIP).extractall(t)
            for modo in ("font", "palette", "layout", "combo"):
                out = os.path.join(t, modo + ".png")
                r = subprocess.run([sys.executable, "-I", os.path.join(t, "campionario.py"),
                                    os.path.join(t, "esempi", modo + ".json"), out], capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertGreater(os.path.getsize(out), 10000)


if __name__ == "__main__":
    unittest.main()
