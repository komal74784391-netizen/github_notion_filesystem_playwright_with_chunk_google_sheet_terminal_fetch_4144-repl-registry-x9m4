#!/usr/bin/env python3
"""Validate a replication package against standards/package_requirements.yaml."""

import argparse
import json
import sys
from pathlib import Path

DEFAULT_MANIFEST = Path(__file__).resolve().parent.parent / "standards" / "package_requirements.yaml"


def load_required_paths(manifest_path):
    """Minimal reader for the deliberately simple manifest format."""
    entries = []
    in_list = False
    for raw in manifest_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('required_paths:'):
            in_list = True
            continue
        if in_list and line.startswith('- '):
            value = line[2:].strip().strip('"').strip("'")
            if value:
                entries.append(value)
        elif in_list:
            in_list = False
    return entries


def check_package(package_dir, required):
    missing = []
    for rel in required:
        candidate = package_dir / rel
        if not candidate.is_file() or candidate.stat().st_size == 0:
            missing.append(rel)
    return missing


def main():
    parser = argparse.ArgumentParser(description="Check a replication package")
    parser.add_argument("package", help="path to the package directory")
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    args = parser.parse_args()
    required = load_required_paths(Path(args.manifest))
    missing = check_package(Path(args.package), required)
    print(json.dumps({"missing": missing}))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
