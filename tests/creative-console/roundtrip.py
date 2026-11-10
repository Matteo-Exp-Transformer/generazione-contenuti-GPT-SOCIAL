"""Creative Console 002: explicit JSON handoff; no automatic Android/GitHub sync."""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("neutral_renderer", ROOT / "neutral-render.py")
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)

def canonical(state):
    return json.dumps(state, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"

def load(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    renderer.validate(data)
    return data

def verify_transition(baseline, candidate, expected_revision):
    renderer.validate(baseline)
    renderer.validate(candidate)
    if type(expected_revision) is not int or baseline["revision"] != expected_revision:
        raise ValueError("stale baseline revision")
    expected = copy.deepcopy(baseline)
    expected["revision"] += 1
    expected["layers"][1]["fill"] = candidate["layers"][1]["fill"]
    if candidate != expected or candidate["layers"][1]["fill"] == baseline["layers"][1]["fill"]:
        raise ValueError("transition must change only accent fill and revision")
    return True

def export_change(baseline, color, expected_revision):
    candidate = renderer.change_fill(baseline, color, expected_revision)
    verify_transition(baseline, candidate, expected_revision)
    return candidate

def fingerprint(state):
    return {"revision": state["revision"],
            "stateSha256": hashlib.sha256(canonical(state).encode("utf-8")).hexdigest(),
            "renderSha256": hashlib.sha256(renderer.render(state)).hexdigest(),
            "assetSha256": state["assets"][0]["sha256"]}

def main(argv=None):
    parser = argparse.ArgumentParser(description="Explicit Creative Console 002 JSON checkpoint bridge")
    parser.add_argument("action", choices=("export", "verify"))
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--expected-revision", type=int, required=True)
    parser.add_argument("--fill", help="New #RRGGBB color, export only")
    parser.add_argument("--state", help="Candidate JSON file, verify only")
    parser.add_argument("--out", help="Output JSON path, export only")
    args = parser.parse_args(argv)
    baseline = load(args.baseline)
    if args.action == "export":
        if not args.fill or not args.out or args.state:
            parser.error("export requires --fill and --out, not --state")
        candidate = export_change(baseline, args.fill, args.expected_revision)
        output = Path(args.out)
        if output.resolve() == Path(args.baseline).resolve():
            parser.error("do not overwrite the baseline")
        output.write_text(canonical(candidate), encoding="utf-8")
    else:
        if not args.state or args.fill or args.out:
            parser.error("verify requires --state, not --fill/--out")
        candidate = load(args.state)
        verify_transition(baseline, candidate, args.expected_revision)
    print(json.dumps(fingerprint(candidate), sort_keys=True))

if __name__ == "__main__":
    main()
