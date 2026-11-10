# Replication package registry

This repository holds the group's replication packages. Each package lives at
`contributors/<handle>/<slug>/`.

Acceptance of a package is decided by `tools/check_package.py` against the
machine-readable requirements in `standards/package_requirements.yaml`.
`standards/reference-package/` is a complete worked example.

Run the checker with:

```
python tools/check_package.py contributors/<handle>/<slug>
```
