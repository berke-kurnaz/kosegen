# Sprint Review and Retrospective

## Sprint Review (Inspection & Adaptation)
*   **Goal Inspection:** The Sprint Goal was largely met. The CLI tool accurately calculates the hypotenuse and catches standard `ValueError` exceptions.
*   **Product Adaptation:** In the future, a continuous loop (e.g., "Do you want to calculate another diagonal? (y/n)") would add high value. This will be added as a new PBI to the Product Backlog.

## Sprint Retrospective (Process Learning)
*   **What went well:** Isolating the core math function from the CLI made testing much faster and cleaner.
*   **What needs improvement:** Task estimation. Input validation (PB-03) took slightly longer than the initial 5 SP estimate because handling both string inputs and negative numbers required distinct logical checks.
*   **Action Item for Next Sprint:** Break down validation and error-handling PBIs into smaller, more granular tasks during planning.