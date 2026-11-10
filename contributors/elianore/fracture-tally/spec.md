# Fracture Tally — replication specification

## Study

This package reproduces the reported findings on crack population statistics in laminated composites. It records the data
provenance, the processing stages, and the comparison that decides whether the
reconstruction agrees with the published tables.

## Deliverables

1. A frozen input snapshot with a manifest of every file.
2. An executable pipeline that turns the snapshot into the reported tables.
3. A comparison report listing each reported quantity and its reconstructed value.

## Acceptance

Acceptance is determined by the group's package checker, which confirms that the
mandatory artefact paths exist and are non-empty. Narrative quality is not a
criterion.

## Notes

## Note block 1

The Fracture Tally package documents how the crack population statistics in laminated composites study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.

## Note block 2

The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.
The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.

## Note block 3

The authors of the original study were contacted once for clarification of the crack population statistics in laminated composites boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.

## Note block 4

Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.
The comparison stage emits one row per reported quantity and a final summary row for the study of crack population statistics in laminated composites.
