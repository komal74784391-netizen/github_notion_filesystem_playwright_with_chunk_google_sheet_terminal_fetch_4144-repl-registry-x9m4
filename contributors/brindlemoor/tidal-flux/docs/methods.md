# Methods log — Tidal Flux

## Note block 1

The Tidal Flux package documents how the tidally driven exchange in shallow shelf basins study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.

## Note block 2

Ambiguous parameter choices are recorded next to the value that was finally used in the run.
The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the tidally driven exchange in shallow shelf basins boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.

## Note block 3

The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.
Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.

## Note block 4

The comparison stage emits one row per reported quantity and a final summary row for the study of tidally driven exchange in shallow shelf basins.
Seeds for stochastic components are fixed and listed in the metadata so that variance cannot be mistaken for a difference.
The Tidal Flux maintainers reviewed the reconstruction notes before the package was proposed for acceptance.
A package is considered reproducible when the comparison stage finishes without introducing new discrepancies.
The documentation describes the reasoning behind each choice, including the alternatives that were rejected.

## Note block 5

Intermediate artefacts are small enough to be regenerated from the frozen inputs on a single workstation.
The acceptance entry point is intentionally thin; it validates the environment and dispatches to the stage scripts.
Units follow the convention used in the original publication, and conversions are explicit in the preparation stage.
Where the original study reported ranges, the package reports the same ranges rather than collapsing them to a point estimate.
The Tidal Flux package documents how the tidally driven exchange in shallow shelf basins study was reconstructed from the archived raw records.

## Note block 6

All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.

## Note block 7

The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the tidally driven exchange in shallow shelf basins boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.

## Note block 8

Result files carry a short header that names the stage, the snapshot and the checker that produced them.
Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.
The comparison stage emits one row per reported quantity and a final summary row for the study of tidally driven exchange in shallow shelf basins.

## Note block 9

Seeds for stochastic components are fixed and listed in the metadata so that variance cannot be mistaken for a difference.
The Tidal Flux maintainers reviewed the reconstruction notes before the package was proposed for acceptance.
A package is considered reproducible when the comparison stage finishes without introducing new discrepancies.
The documentation describes the reasoning behind each choice, including the alternatives that were rejected.
Intermediate artefacts are small enough to be regenerated from the frozen inputs on a single workstation.

## Note block 10

The acceptance entry point is intentionally thin; it validates the environment and dispatches to the stage scripts.
Units follow the convention used in the original publication, and conversions are explicit in the preparation stage.
Where the original study reported ranges, the package reports the same ranges rather than collapsing them to a point estimate.
The Tidal Flux package documents how the tidally driven exchange in shallow shelf basins study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.

## Note block 11

Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.
The repository keeps the working notes that were taken while the original analysis was reproduced.

## Note block 12

Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the tidally driven exchange in shallow shelf basins boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.
