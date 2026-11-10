"""Round-trip contract tests: no Android UI or remote GitHub claim."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("roundtrip", ROOT / "roundtrip.py")
bridge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bridge)

class RoundTripTests(unittest.TestCase):
    def setUp(self):
        self.baseline = bridge.load(ROOT / "neutral-state.json")

    def test_export_import_and_recovery(self):
        changed = bridge.export_change(self.baseline, "#B36A48", 1)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "checkpoint.json"
            path.write_text(bridge.canonical(changed), encoding="utf-8")
            recovered = bridge.load(path)
            self.assertEqual(bridge.canonical(recovered), bridge.canonical(changed))
            self.assertEqual(bridge.fingerprint(recovered), bridge.fingerprint(changed))
            self.assertTrue(bridge.verify_transition(self.baseline, recovered, 1))

    def test_only_fill_and_revision(self):
        changed = bridge.export_change(self.baseline, "#B36A48", 1)
        expected = copy.deepcopy(self.baseline)
        expected["revision"] = 2
        expected["layers"][1]["fill"] = "#B36A48"
        self.assertEqual(changed, expected)

    def test_stale_revision(self):
        with self.assertRaises(ValueError):
            bridge.export_change(self.baseline, "#B36A48", 0)

    def test_tampered_asset(self):
        changed = bridge.export_change(self.baseline, "#B36A48", 1)
        changed["assets"][0]["sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            bridge.verify_transition(self.baseline, changed, 1)

    def test_unrelated_change(self):
        changed = bridge.export_change(self.baseline, "#B36A48", 1)
        changed["projectId"] = "other"
        with self.assertRaises(ValueError):
            bridge.verify_transition(self.baseline, changed, 1)

    def test_noop_rejected(self):
        with self.assertRaises(ValueError):
            bridge.verify_transition(self.baseline, self.baseline, 1)

    def test_cli_export_verify(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "checkpoint.json"
            cmd = [sys.executable, str(ROOT / "roundtrip.py")]
            baseline = str(ROOT / "neutral-state.json")
            result = subprocess.run(cmd + ["export", "--baseline", baseline, "--expected-revision", "1", "--fill", "#B36A48", "--out", str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["revision"], 2)
            recovered = bridge.load(output)
            self.assertEqual(output.read_bytes(), bridge.canonical(recovered).encode("utf-8"))
            self.assertEqual(json.loads(result.stdout), bridge.fingerprint(recovered))
            result = subprocess.run(cmd + ["verify", "--baseline", baseline, "--expected-revision", "1", "--state", str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

if __name__ == "__main__":
    unittest.main()
