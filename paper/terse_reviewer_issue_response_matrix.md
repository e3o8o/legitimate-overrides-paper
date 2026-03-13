# TERSE reviewer issue response matrix

This memo maps each reviewer concern to the concrete change made in the TERSE revision pass.

## 1. Figure 6 caption inconsistency

- Reviewer issue:
  the caption stated that Signer Set interventions were more reliable than Delegated Bodies, while the section text reported the reverse.
- Fix:
  corrected the caption in `main_revised_terse.tex` so it now states that Delegated Body interventions outperform Signer Set interventions in the verified sample.
- Additional clarification:
  the caption now also warns that the Governance-coded subset is small and mixed.

## 2. Prediction 2 was not actually assessed clearly

- Reviewer issue:
  the paper implied that all three predictions were tested, but Prediction 2 did not have a clear empirical treatment.
- Fix:
  added a bounded proxy test using scope breadth as a proxy for blast potential.
- Evidence path:
  - `notebooks/terse_revision_checks.py`
  - `data/terse_revision_metrics_summary.md`
- Result:
  Account/Module interventions outperform Protocol/Network on median containment success and are slightly faster at the median.
- Limitation preserved:
  this remains a proxy test, not a direct market-wide collateral-loss estimate.

## 3. Governance success-rate coding was too loose

- Reviewer issue:
  the governance figure was based on a small subset and appeared to mix direct governance, delegated freezes, and negotiated recovery.
- Fix:
  tightened the coding and corrected two authority labels in the underlying data.
- Data corrections:
  - `Aave v2` reclassified from `Governance` to `Delegated Body`
  - `Alpha Homora V2` reclassified from `Governance` to `Signer Set`
- Files updated:
  - `data/lif_intervention_metrics.csv`
  - `data/lif_all_interventions.csv`
  - `data/lif_exploits_final.csv`
- Revised result:
  the Governance-coded subset is now `5` cases with mean containment success `87.8%`.
- Transparency added:
  the paper now includes an appendix table listing the retained Governance-coded cases and the reclassified exclusions.

## 4. Euler should not silently count as governance success

- Reviewer issue:
  Euler was resolved mainly through negotiation and legal pressure.
- Fix:
  Euler is now explicitly treated as negotiation-dominated recovery, not as a clean onchain governance-containment success.

## 5. Sui/Cetus is a hybrid case

- Reviewer issue:
  the case combines an earlier freeze with later governance authorization.
- Fix:
  the revised text now states clearly that Sui/Cetus is a two-stage hybrid: delegated freeze first, governance authorization later.

## 6. Non-onchain channels needed to be acknowledged

- Reviewer issue:
  negotiation, legal pressure, attacker cooperation, and law enforcement were under-scoped.
- Fix:
  the revised paper now states that these channels are external complements or competitors to onchain intervention, not fully modeled mechanism choices in the current framework.

## 7. CentralizationCost(m) and BlastRate(m) were overclaimed as estimable

- Reviewer issue:
  the abstract and model language sounded too close to a fully estimable optimization.
- Fix:
  abstract, contributions, interpretation, and conclusion now present the framework as a decision-support scaffold rather than a fully calibrated optimization model.

## 8. Audit status needed a stronger limitation

- Reviewer issue:
  audit status is an unstable and incomplete proxy for exploit probability.
- Fix:
  the revised draft now includes explicit limitation text that treats audit status as a coarse heuristic only.

## 9. Legitimacy is often built through process, not just ex ante design

- Reviewer issue:
  the original framing risked reducing legitimacy to a cost parameter.
- Fix:
  added a boundary note explaining that legitimacy is often produced through abstention, renunciation, procedure, and post-crisis conduct, not only architecture choice.

## Figure regeneration status

- Regenerated from the analysis path:
  - `paper/figures/lof05_intervention_effectiveness.png`
  - `paper/figures/lof06_authority_distribution.png`
- Helper used:
  - `notebooks/terse_regenerate_figures.py`

## Final caution retained in the revision

- Even after recoding, the Governance-coded subset is still small and conceptually mixed.
- The revised paper now says that explicitly instead of presenting the percentage as a pure governance-containment benchmark.
