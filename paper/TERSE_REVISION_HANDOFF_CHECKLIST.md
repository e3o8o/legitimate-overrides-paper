# TERSE Revision Handoff Checklist

This checklist is the handoff surface for final review, Overleaf update, and arXiv reupload of the revised Legitimate Overrides paper.

## Canonical revised paper artifacts

- revised manuscript:
  [main_revised_terse.tex](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/paper/main_revised_terse.tex)
- reviewer-response mapping:
  [terse_reviewer_issue_response_matrix.md](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/paper/terse_reviewer_issue_response_matrix.md)
- coding justification note:
  [terse_governance_coding_justification.md](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/paper/terse_governance_coding_justification.md)
- internal Nimrod draft email:
  [terse_email_to_nimrod_draft.md](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/paper/terse_email_to_nimrod_draft.md)
- TERSE acknowledgement draft:
  [terse_email_ack_to_terse_draft.md](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/paper/terse_email_ack_to_terse_draft.md)
- TERSE final response draft:
  [terse_email_final_to_terse_draft.md](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/paper/terse_email_final_to_terse_draft.md)

## Data and figure provenance

- revision metrics script:
  [terse_revision_checks.py](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/notebooks/terse_revision_checks.py)
- metrics summary output:
  [terse_revision_metrics_summary.md](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/data/terse_revision_metrics_summary.md)
- figure regeneration script:
  [terse_regenerate_figures.py](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/notebooks/terse_regenerate_figures.py)
- regenerated figures:
  [lof05_intervention_effectiveness.png](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/paper/figures/lof05_intervention_effectiveness.png)
  [lof06_authority_distribution.png](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/paper/figures/lof06_authority_distribution.png)

## Revision outcomes currently reflected

- Figure 6 caption inconsistency corrected
- Prediction 2 now tested in bounded form via scope-breadth proxy
- governance coding tightened
  - `Aave v2` -> `Delegated Body`
  - `Alpha Homora V2` -> `Signer Set`
- Governance-coded subset now:
  - `5` cases
  - mean containment success `87.8%`
- Euler explicitly scoped as negotiation-dominated recovery
- Sui/Cetus explicitly scoped as a hybrid case
- model certainty softened around `CentralizationCost(m)` and `BlastRate(m)`
- stronger limitations added for:
  - audit-status proxy
  - process-built legitimacy
  - non-onchain complement channels

## Before sending to Nimrod

- verify Overleaf compiles `main_revised_terse.tex`
- visually inspect regenerated figures in the compiled PDF
- confirm appendix tables render cleanly
- confirm no stale text remains from the earlier coding state
- send:
  [terse_email_to_nimrod_draft.md](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/LIF/legitimate-overrides-paper/paper/terse_email_to_nimrod_draft.md)

## After Nimrod review

- fold any final wording or evidence corrections into `main_revised_terse.tex`
- update the reviewer-response matrix if any mapping changes
- send TERSE acknowledgement or final response using the prepared drafts as appropriate

## Before arXiv reupload

- keep the same technical report number
- update:
  [PARAMETRIG_TECHNICAL_REPORTS_INDEX.md](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/PARAMETRIG/parametrig/specs/research/PARAMETRIG_TECHNICAL_REPORTS_INDEX.md)
- follow:
  [TECHNICAL_REPORT_INDEX_AND_ARXIV_UPDATE_WORKFLOW.md](/Users/elemoghenekaro/Workspace/tasks/01_ACTIVE_PROJECTS/PARAMETRIG/parametrig/specs/research/TECHNICAL_REPORT_INDEX_AND_ARXIV_UPDATE_WORKFLOW.md)

## Final operator note

Do not treat the revised TERSE manuscript as complete until:

- Overleaf compile is clean
- figures look correct in the compiled PDF
- Nimrod has reviewed the `\elem{}` comments
- the final TERSE reply reflects the same issue-response mapping as the paper
