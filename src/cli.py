from __future__ import annotations
import argparse, json
from pathlib import Path
from .scanner import scan

def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan")
    s.add_argument("--path", type=Path, required=True)
    args = p.parse_args(argv)
    print(json.dumps(scan(args.path), indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
