"""Synthetic contract checks, not TU-01 or an Android/quality gate.

Run: python -m unittest discover -s tests/engine -v
All photos, state checkpoints and render outputs live in a system temp directory.
"""
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import PIL
from PIL import Image, ImageChops, ImageDraw, PngImagePlugin

ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "engine" / "render.py"
spec = importlib.util.spec_from_file_location("post_renderer", ENGINE)
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class EngineContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="gpt-social-engine-")
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.photo = self.work / "synthetic.png"
        # Synthetic source; no user photo or fetched assets.
        image = Image.new("RGB", (480, 600))
        image.putdata([((x * 7 + y) % 256, (x + y * 3) % 256, (x * y) % 256)
                       for y in range(600) for x in range(480)])
        image.save(self.photo)
        self.original_photo = self.photo.read_bytes()
        self.state = {
            "revision": 1, "formato": {"w": 1080, "h": 1350},
            "foto": {"file": "synthetic.png", "sha256": hashlib.sha256(self.original_photo).hexdigest(),
                     "crop": [0, 0, 480, 600]},
            "testi": {"A": {"ruolo": "titolo", "testo": "Titolo A", "font": "pillow-default",
                             "size": 64, "pos": [60, 80], "colore": "#aBcDeF"}},
            "palette": ["#aBcDeF", "#223344"], "layout": "photo-title",
            "bloccati": ["foto", "A", "fondo-titolo"],
            "storia": [{"rev": 1, "modifica": "checkpoint sintetico, non approvazione utente"}],
            "forme": [{"id": "fondo-titolo", "tipo": "rettangolo", "pos": [40, 60],
                       "size": [1000, 160], "colore": "#223344"}],
        }
        self.post = self.work / "post.json"
        self.write_state(self.state)

    def write_state(self, state):
        self.post.write_text(json.dumps(state), encoding="utf-8")

    def decode(self, png):
        with Image.open(io.BytesIO(png)) as image:
            return image.convert("RGB")

    def test_real_title_change_preserves_every_pixel_outside_title(self):
        a_state = copy.deepcopy(self.state)
        b_state = copy.deepcopy(self.state)
        b_state["testi"]["A"]["testo"] = "Nuovo B"
        # Only the title string changed; locks and decision history are untouched.
        self.assertEqual({k: v for k, v in a_state.items() if k != "testi"},
                         {k: v for k, v in b_state.items() if k != "testi"})
        a, b = self.decode(r.render(a_state, self.photo)), self.decode(r.render(b_state, self.photo))
        diff = ImageChops.difference(a, b)
        changed_bounds = diff.getbbox()
        self.assertIsNotNone(changed_bounds, "title edit must actually change pixels")
        title_area = (60, 80, 1000, 180)
        self.assertLess((title_area[2] - title_area[0]) * (title_area[3] - title_area[1]), a.width * a.height // 4)
        self.assertTrue(changed_bounds[0] >= title_area[0] and changed_bounds[1] >= title_area[1]
                        and changed_bounds[2] <= title_area[2] and changed_bounds[3] <= title_area[3])
        ImageDraw.Draw(diff).rectangle((60, 80, 999, 179), fill=(0, 0, 0))
        self.assertIsNone(diff.getbbox())
        self.assertEqual(self.photo.read_bytes(), self.original_photo)
        print(f"PROOF title change bounds={changed_bounds}; all pixels outside {title_area} identical")

    def test_a_b_a_decoded_pixel_hash_and_serialized_resume(self):
        before = copy.deepcopy(self.state)
        a = r.render(self.post, self.photo)
        changed = copy.deepcopy(self.state)
        changed["testi"]["A"]["testo"] = "Nuovo B"
        self.write_state(changed)
        b = r.render(self.post, self.photo)
        self.assertNotEqual(r.pixel_sha256(a), r.pixel_sha256(b))
        self.write_state(before)
        restored = r.render(self.post, self.photo)
        self.assertEqual(r.pixel_sha256(a), r.pixel_sha256(restored))
        self.assertEqual(a, restored)
        self.assertEqual(self.state, before)
        print("PROOF decoded A=" + r.pixel_sha256(a) + " B=" + r.pixel_sha256(b)
              + " restored=" + r.pixel_sha256(restored))

    def test_source_hash_checked_and_source_not_modified(self):
        self.assertEqual(r.photo_sha256(self.photo), self.state["foto"]["sha256"])
        state = copy.deepcopy(self.state)
        state["foto"]["sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            r.render(state, self.photo)
        self.photo.write_bytes(self.original_photo + b"tamper")
        with self.assertRaises(ValueError):
            r.render(self.state, self.photo)
        print("PROOF source file SHA256=" + self.state["foto"]["sha256"] + "; tampering rejected")

    def test_pixel_hash_ignores_png_metadata_and_compression(self):
        png = r.render(self.state, self.photo)
        changed_encoding = io.BytesIO()
        info = PngImagePlugin.PngInfo()
        info.add_text("unrelated", "different metadata")
        self.decode(png).save(changed_encoding, format="PNG", compress_level=0, pnginfo=info)
        self.assertNotEqual(hashlib.sha256(png).digest(), hashlib.sha256(changed_encoding.getvalue()).digest())
        self.assertEqual(r.pixel_sha256(png), r.pixel_sha256(changed_encoding.getvalue()))

    def test_crop_scale_photo_only_matches_pillow_and_no_hidden_crop(self):
        state = {"revision": 1, "formato": {"w": 216, "h": 270},
                 "foto": {**self.state["foto"], "crop": [40, 50, 400, 500]}}
        rendered = self.decode(r.render(state, self.photo))
        with Image.open(self.photo) as source:
            expected = source.convert("RGB").crop((40, 50, 440, 550)).resize((216, 270), Image.Resampling.LANCZOS)
        self.assertEqual(rendered.tobytes(), expected.tobytes())
        state["foto"]["crop"] = [40, 50, 400, 499]
        with self.assertRaises(ValueError):
            r.render(state, self.photo)

    def test_shapes_have_exact_half_open_bounds_and_layer_order(self):
        state = copy.deepcopy(self.state)
        state["testi"] = {}
        state["bloccati"] = ["foto", "fondo-titolo"]
        output = self.decode(r.render(state, self.photo))
        for pos in ((40, 60), (1039, 219), (300, 150)):
            self.assertEqual(output.getpixel(pos), (34, 51, 68))
        state["forme"] = []
        state["bloccati"] = ["foto"]
        base = self.decode(r.render(state, self.photo))
        for pos in ((39, 60), (1040, 219), (40, 220)):
            self.assertEqual(output.getpixel(pos), base.getpixel(pos))
        diff = ImageChops.difference(output, base)
        self.assertEqual(diff.getbbox(), (40, 60, 1040, 220))

    def test_colors_normalize_without_input_mutation(self):
        snapshot = copy.deepcopy(self.state)
        normalized = r.normalized_state(self.state)
        self.assertEqual(normalized["testi"]["A"]["colore"], "#ABCDEF")
        self.assertEqual(normalized["palette"][0], "#ABCDEF")
        self.assertEqual(self.state, snapshot)
        self.assertEqual(r.render(normalized, self.photo), r.render(self.state, self.photo))

    def test_revision_boolean_rejected_at_root_and_history(self):
        for value in (True, False, 0, -1, 1.0, "1", None):
            with self.subTest(value=value):
                state = copy.deepcopy(self.state)
                state["revision"] = value
                with self.assertRaises(ValueError):
                    r.render(state, self.photo)
        state = copy.deepcopy(self.state)
        state["storia"][0]["rev"] = True
        with self.assertRaises(ValueError):
            r.render(state, self.photo)

    def test_closed_keys_at_every_object_depth(self):
        paths = [(), ("formato",), ("foto",), ("testi", "A"), ("storia", 0), ("forme", 0)]
        for path in paths:
            with self.subTest(path=path):
                state = copy.deepcopy(self.state)
                target = state
                for key in path:
                    target = target[key]
                target["unknown"] = "rejected"
                with self.assertRaises(ValueError):
                    r.render(state, self.photo)

    def test_all_skill_decision_elements_can_be_locked(self):
        snapshot = copy.deepcopy(self.state)
        self.state["bloccati"].extend(["palette", "layout"])
        normalized = r.normalized_state(self.state)
        self.assertEqual(normalized["bloccati"], self.state["bloccati"])
        self.assertEqual(r.render(snapshot, self.photo), r.render(self.state, self.photo))
        self.assertEqual(self.state["revision"], 1)

    def test_bad_inputs_raise_only_value_error(self):
        for post in (None, [], 42, {}, {"revision": True}, "missing.json"):
            with self.subTest(post=post):
                with self.assertRaises(ValueError):
                    r.render(post, self.photo)
        for key, value in (("foto", None), ("formato", []), ("testi", []), ("palette", {}),
                           ("forme", {}), ("storia", {}), ("bloccati", [{}]), ("layout", False)):
            with self.subTest(key=key):
                state = copy.deepcopy(self.state)
                state[key] = value
                with self.assertRaises(ValueError):
                    r.render(state, self.photo)
        bad_nested = [("testi", "A", "size", True), ("testi", "A", "colore", "red"),
                      ("testi", "A", "font", "missing-font.ttf"), ("foto", "crop", None),
                      ("foto", "crop", [0, 0, 481, 600]), ("foto", "sha256", []),
                      ("formato", "w", True), ("forme", 0, "tipo", "circle")]
        for mutation in bad_nested:
            with self.subTest(mutation=mutation):
                state = copy.deepcopy(self.state)
                target = state
                for key in mutation[:-2]:
                    target = target[key]
                target[mutation[-2]] = mutation[-1]
                with self.assertRaises(ValueError):
                    r.render(state, self.photo)
        with self.assertRaises(ValueError):
            r.photo_sha256(self.work / "absent")
        with self.assertRaises(ValueError):
            r.pixel_sha256(b"not PNG")

    def test_duplicate_json_keys_and_invalid_json(self):
        for content in ('{"revision":1,"revision":2}', '{"testi":{"A":{},"A":{}}}', "not json"):
            self.post.write_text(content, encoding="utf-8")
            with self.assertRaises(ValueError):
                r.render(self.post, self.photo)

    def test_source_invalid_image_is_value_error(self):
        self.photo.write_bytes(b"not a photo")
        self.state["foto"]["sha256"] = r.photo_sha256(self.photo)
        with self.assertRaises(ValueError):
            r.render(self.state, self.photo)

    def test_output_external_atomic_and_protected_inputs(self):
        output = self.work / "render-A.png"
        state_before, photo_before = self.post.read_bytes(), self.photo.read_bytes()
        self.assertEqual(output.parent, self.work)
        png = r.render(self.post, self.photo, output)
        self.assertEqual(output.read_bytes(), png)
        self.assertEqual(self.post.read_bytes(), state_before)
        self.assertEqual(self.photo.read_bytes(), photo_before)
        for bad in (self.photo, self.post, ROOT / "render-must-not-exist.png",
                    self.work / "missing" / "render.png", self.work / "render.jpg"):
            with self.subTest(output=str(bad)):
                with self.assertRaises(ValueError):
                    r.render(self.post, self.photo, bad)
        self.assertEqual(self.photo.read_bytes(), photo_before)
        self.assertFalse((ROOT / "render-must-not-exist.png").exists())
        self.assertFalse(list(self.work.glob(".gpt-social-*")))

    def test_git_worktree_marker_also_blocks_output(self):
        nested = self.work / "worktree"
        nested.mkdir()
        (nested / ".git").write_text("gitdir: elsewhere", encoding="utf-8")
        with self.assertRaises(ValueError):
            r.render(self.state, self.photo, nested / "render.png")

    def test_font_version_recorded_and_local_font_optional(self):
        with Image.open(io.BytesIO(r.render(self.state, self.photo))) as image:
            record = json.loads(image.info["gpt-social"])
        self.assertEqual(record["pillow"], r.PILLOW_VERSION)
        self.assertEqual(record["fonts"]["A"]["font"], "pillow-default")
        self.assertEqual(record["fonts"]["A"]["size"], 64)
        self.assertEqual(record["photo_sha256"], self.state["foto"]["sha256"])
        self.assertEqual(record["photo_pixel_sha256"], r.pixel_sha256(self.photo))
        # Only already-installed fonts, no download and no dependency on one font.
        candidates = [Path("C:/Windows/Fonts/arial.ttf"), Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")]
        local = next((p for p in candidates if p.is_file()), None)
        if local is not None:
            self.state["testi"]["A"]["font"] = str(local)
            with Image.open(io.BytesIO(r.render(self.state, self.photo))) as image:
                record = json.loads(image.info["gpt-social"])
            self.assertEqual(record["fonts"]["A"]["sha256"], hashlib.sha256(local.read_bytes()).hexdigest())
            print("PROOF installed font verified: " + local.name)

    def test_undecided_fields_and_clipped_text_fail_explicitly(self):
        for field in ("ruolo", "testo", "font", "size", "pos", "colore"):
            state = copy.deepcopy(self.state)
            del state["testi"]["A"][field]
            with self.subTest(missing=field):
                with self.assertRaises(ValueError):
                    r.render(state, self.photo)
        for value in (0, -1):
            self.state["testi"]["A"]["size"] = value
            with self.assertRaises(ValueError):
                r.render(self.state, self.photo)
        self.state["testi"]["A"].update(size=64, pos=[1070, 1340])
        with self.assertRaises(ValueError):
            r.render(self.state, self.photo)

    def test_standalone_import_cli_and_new_process_resume(self):
        standalone = self.work / "render.py"
        shutil.copyfile(ENGINE, standalone)
        output = self.work / "render-cli.png"
        # -I excludes user-site packages; Pillow is installed there on this machine.
        # Explicitly expose only its installed package directory to isolated Python.
        pillow_site = str(Path(PIL.__file__).resolve().parent.parent)
        bootstrap = ("import sys,runpy;sys.path.insert(0," + repr(pillow_site)
                     + ");sys.argv=sys.argv[1:];runpy.run_path(sys.argv[0],run_name='__main__')")
        process = subprocess.run([sys.executable, "-I", "-c", bootstrap, str(standalone), str(self.post), str(self.photo), str(output)],
                                 cwd=self.work, capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr + process.stdout)
        receipt = json.loads(process.stdout)
        self.assertEqual(receipt["pixel_sha256"], r.pixel_sha256(r.render(self.post, self.photo)))
        # Import only copied file, with isolated sys.path, no repo cwd/modules.
        code = ("import sys;sys.path.insert(0," + repr(pillow_site) + ");"
                + "import importlib.util,json; s=importlib.util.spec_from_file_location('standalone'," + repr(str(standalone))
                + ");m=importlib.util.module_from_spec(s);s.loader.exec_module(m);print(m.pixel_sha256(m.render("
                + repr(str(self.post)) + "," + repr(str(self.photo)) + ")))")
        imported = subprocess.run([sys.executable, "-I", "-c", code], cwd=self.work, capture_output=True, text=True)
        self.assertEqual(imported.returncode, 0, imported.stderr)
        self.assertEqual(imported.stdout.strip(), receipt["pixel_sha256"])
        bad = subprocess.run([sys.executable, "-I", "-c", bootstrap, str(standalone), "absent.json", str(self.photo), str(output)],
                             cwd=self.work, capture_output=True, text=True)
        self.assertEqual(bad.returncode, 2)
        self.assertIn("error", json.loads(bad.stdout))
        self.assertNotIn("Traceback", bad.stderr)
        print("PROOF standalone isolated CLI/import/new-process resume PASS; Pillow=" + receipt["pillow"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
