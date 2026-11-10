# Working notes — Biofilm Ridge

## Note block 1

The Biofilm Ridge package documents how the biofilm ridge formation under oscillatory shear study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.

## Note block 2

The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the biofilm ridge formation under oscillatory shear boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.

## Note block 3

Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.
The comparison stage emits one row per reported quantity and a final summary row for the study of biofilm ridge formation under oscillatory shear.
Seeds for stochastic components are fixed and listed in the metadata so that variance cannot be mistaken for a difference.
The Biofilm Ridge maintainers reviewed the reconstruction notes before the package was proposed for acceptance.

## Note block 4

A package is considered reproducible when the comparison stage finishes without introducing new discrepancies.
The documentation describes the reasoning behind each choice, including the alternatives that were rejected.
Intermediate artefacts are small enough to be regenerated from the frozen inputs on a single workstation.
The acceptance entry point is intentionally thin; it validates the environment and dispatches to the stage scripts.
Units follow the convention used in the original publication, and conversions are explicit in the preparation stage.
Where the original study reported ranges, the package reports the same ranges rather than collapsing them to a point estimate.

## Note block 5

The Biofilm Ridge package documents how the biofilm ridge formation under oscillatory shear study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.

## Note block 6

The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the biofilm ridge formation under oscillatory shear boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.

## Note block 7

Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.
The comparison stage emits one row per reported quantity and a final summary row for the study of biofilm ridge formation under oscillatory shear.
Seeds for stochastic components are fixed and listed in the metadata so that variance cannot be mistaken for a difference.
The Biofilm Ridge maintainers reviewed the reconstruction notes before the package was proposed for acceptance.

## Note block 8

A package is considered reproducible when the comparison stage finishes without introducing new discrepancies.
The documentation describes the reasoning behind each choice, including the alternatives that were rejected.
Intermediate artefacts are small enough to be regenerated from the frozen inputs on a single workstation.
The acceptance entry point is intentionally thin; it validates the environment and dispatches to the stage scripts.
Units follow the convention used in the original publication, and conversions are explicit in the preparation stage.
Where the original study reported ranges, the package reports the same ranges rather than collapsing them to a point estimate.

## Note block 9

The Biofilm Ridge package documents how the biofilm ridge formation under oscillatory shear study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.

## Note block 10

The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the biofilm ridge formation under oscillatory shear boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.

## Note block 11

Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.
The comparison stage emits one row per reported quantity and a final summary row for the study of biofilm ridge formation under oscillatory shear.
Seeds for stochastic components are fixed and listed in the metadata so that variance cannot be mistaken for a difference.
The Biofilm Ridge maintainers reviewed the reconstruction notes before the package was proposed for acceptance.

## Note block 12

A package is considered reproducible when the comparison stage finishes without introducing new discrepancies.
The documentation describes the reasoning behind each choice, including the alternatives that were rejected.
Intermediate artefacts are small enough to be regenerated from the frozen inputs on a single workstation.
The acceptance entry point is intentionally thin; it validates the environment and dispatches to the stage scripts.
Units follow the convention used in the original publication, and conversions are explicit in the preparation stage.
Where the original study reported ranges, the package reports the same ranges rather than collapsing them to a point estimate.

## Note block 13

The Biofilm Ridge package documents how the biofilm ridge formation under oscillatory shear study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.

## Note block 14

The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the biofilm ridge formation under oscillatory shear boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.

## Note block 15

Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.
The comparison stage emits one row per reported quantity and a final summary row for the study of biofilm ridge formation under oscillatory shear.
Seeds for stochastic components are fixed and listed in the metadata so that variance cannot be mistaken for a difference.
The Biofilm Ridge maintainers reviewed the reconstruction notes before the package was proposed for acceptance.

## Note block 16

A package is considered reproducible when the comparison stage finishes without introducing new discrepancies.
The documentation describes the reasoning behind each choice, including the alternatives that were rejected.
Intermediate artefacts are small enough to be regenerated from the frozen inputs on a single workstation.
The acceptance entry point is intentionally thin; it validates the environment and dispatches to the stage scripts.
Units follow the convention used in the original publication, and conversions are explicit in the preparation stage.
Where the original study reported ranges, the package reports the same ranges rather than collapsing them to a point estimate.

## Note block 17

The Biofilm Ridge package documents how the biofilm ridge formation under oscillatory shear study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.

## Note block 18

The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the biofilm ridge formation under oscillatory shear boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.

## Note block 19

Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.
The comparison stage emits one row per reported quantity and a final summary row for the study of biofilm ridge formation under oscillatory shear.
Seeds for stochastic components are fixed and listed in the metadata so that variance cannot be mistaken for a difference.
The Biofilm Ridge maintainers reviewed the reconstruction notes before the package was proposed for acceptance.

## Note block 20

A package is considered reproducible when the comparison stage finishes without introducing new discrepancies.
The documentation describes the reasoning behind each choice, including the alternatives that were rejected.
Intermediate artefacts are small enough to be regenerated from the frozen inputs on a single workstation.
The acceptance entry point is intentionally thin; it validates the environment and dispatches to the stage scripts.
Units follow the convention used in the original publication, and conversions are explicit in the preparation stage.
Where the original study reported ranges, the package reports the same ranges rather than collapsing them to a point estimate.

## Note block 21

The Biofilm Ridge package documents how the biofilm ridge formation under oscillatory shear study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.

## Note block 22

The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the biofilm ridge formation under oscillatory shear boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.

## Note block 23

Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.
The comparison stage emits one row per reported quantity and a final summary row for the study of biofilm ridge formation under oscillatory shear.
Seeds for stochastic components are fixed and listed in the metadata so that variance cannot be mistaken for a difference.
The Biofilm Ridge maintainers reviewed the reconstruction notes before the package was proposed for acceptance.

## Note block 24

A package is considered reproducible when the comparison stage finishes without introducing new discrepancies.
The documentation describes the reasoning behind each choice, including the alternatives that were rejected.
Intermediate artefacts are small enough to be regenerated from the frozen inputs on a single workstation.
The acceptance entry point is intentionally thin; it validates the environment and dispatches to the stage scripts.
Units follow the convention used in the original publication, and conversions are explicit in the preparation stage.
Where the original study reported ranges, the package reports the same ranges rather than collapsing them to a point estimate.

## Note block 25

The Biofilm Ridge package documents how the biofilm ridge formation under oscillatory shear study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.

## Note block 26

The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the biofilm ridge formation under oscillatory shear boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.

## Note block 27

Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.
The comparison stage emits one row per reported quantity and a final summary row for the study of biofilm ridge formation under oscillatory shear.
Seeds for stochastic components are fixed and listed in the metadata so that variance cannot be mistaken for a difference.
The Biofilm Ridge maintainers reviewed the reconstruction notes before the package was proposed for acceptance.

## Note block 28

A package is considered reproducible when the comparison stage finishes without introducing new discrepancies.
The documentation describes the reasoning behind each choice, including the alternatives that were rejected.
Intermediate artefacts are small enough to be regenerated from the frozen inputs on a single workstation.
The acceptance entry point is intentionally thin; it validates the environment and dispatches to the stage scripts.
Units follow the convention used in the original publication, and conversions are explicit in the preparation stage.
Where the original study reported ranges, the package reports the same ranges rather than collapsing them to a point estimate.

## Note block 29

The Biofilm Ridge package documents how the biofilm ridge formation under oscillatory shear study was reconstructed from the archived raw records.
All processing stages are driven from the top-level acceptance entry point and write their results into the run directory.
Input tables are frozen at the snapshot recorded in the metadata file, so reruns against the same snapshot are byte-stable.
Every intermediate object is named after the stage that produced it, which keeps the audit trail easy to follow.
The reconstruction deliberately avoids hidden state; a clean checkout is sufficient to repeat the whole pipeline.
Ambiguous parameter choices are recorded next to the value that was finally used in the run.

## Note block 30

The repository keeps the working notes that were taken while the original analysis was reproduced.
Diagnostic plots are not treated as evidence; only the tabulated outputs participate in the comparison.
The authors of the original study were contacted once for clarification of the biofilm ridge formation under oscillatory shear boundary conditions.
Convergence was assessed by repeating the most expensive stage with a stricter tolerance.
The package separates preparation, execution and comparison so that each can be checked independently.
Result files carry a short header that names the stage, the snapshot and the checker that produced them.

## Note block 31

Any deviation from the original numerical values is documented in the comparison notes rather than silently adjusted.
The scripts assume a POSIX shell and a Python 3 interpreter; no graphical tooling is required.
Raw measurements are never edited in place; corrections are applied by a separate, recorded transformation.
The comparison stage emits one row per reported quantity and a final summary row for the study of biofilm ridge formation under oscillatory shear.
Seeds for stochastic components are fixed and listed in the metadata so that variance cannot be mistaken for a difference.
The Biofilm Ridge maintainers reviewed the reconstruction notes before the package was proposed for acceptance.

## Note block 32

A package is considered reproducible when the comparison stage finishes without introducing new discrepancies.
The documentation describes the reasoning behind each choice, including the alternatives that were rejected.
Intermediate artefacts are small enough to be regenerated from the frozen inputs on a single workstation.
The acceptance entry point is intentionally thin; it validates the environment and dispatches to the stage scripts.
Units follow the convention used in the original publication, and conversions are explicit in the preparation stage.
Where the original study reported ranges, the package reports the same ranges rather than collapsing them to a point estimate.
