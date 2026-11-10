#!/usr/bin/env python3
"""Acceptance entry point for the Phase Settle replication package."""

import json
import sys
from pathlib import Path

META = Path(__file__).resolve().parent.parent / "meta.json"


def main():
    if not META.is_file():
        print("meta.json is missing; cannot run acceptance")
        return 1
    meta = json.loads(META.read_text(encoding="utf-8"))
    if not meta.get("slug"):
        print("meta.json does not declare a slug")
        return 1
    print("acceptance preparation complete for", meta["slug"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
