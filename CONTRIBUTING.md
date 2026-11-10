# Contributing replication packages

## Acceptance rule

A package is accepted when `tools/check_package.py` reports an empty `missing`
list and exits zero. The checker reads the required artefact paths from
`standards/package_requirements.yaml` and treats a path as present only when it
is an existing, non-empty file.

## What is not an acceptance criterion

The following are explicitly NOT acceptance criteria and must never be used to
accept or reject a package:

- prose quality or polish of the documentation;
- documentation length or number of paragraphs;
- total file count of the package;
- the language the documentation is written in;
- commit recency or the number of commits;
- the identity or seniority of the author;
- a README statement that the package is finished.

Only the machine-readable requirements and the executable checker define
acceptance.
