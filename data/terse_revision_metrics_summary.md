# TERSE revision metrics summary

Generated from `data/lif_intervention_metrics.csv` for the TERSE revision pass.

## Authority-level containment success

- Signer Set: n=38, mean containment success=38.0%, median=13.0%
- Delegated Body: n=9, mean containment success=54.4%, median=85.0%
- Governance: n=5, mean containment success=87.8%, median=100.0%

## Governance-coded cases in the current 52-case high-fidelity subset

- Gnosis Chain (GNOSISCHAIN-2025-12-15): scope=Network, success=100.0%
- Sui/Cetus (SUI-2025-05-22): scope=Account, success=73.0%
- MakerDAO (MAKERDAO-2023-03-11): scope=Module, success=100.0%
- VeChain (VECHAIN-2019-12-13): scope=Account, success=66.0%
- Ethereum DAO Fork (ETHEREUMDAOF-2016-06-17): scope=Network, success=100.0%

## Prediction 2 proxy check

Operationalization used for the TERSE revision: treat scope breadth as a proxy for blast potential, and compare narrower interventions (Account/Module) against broader interventions (Protocol/Network). Note that Asset scope is excluded from this proxy because issuer-controlled freezes and bridge-specific asset controls are not directly comparable to protocol/network shutdown behavior.

- Precise scope proxy (Account/Module): n=18, mean success=43.5%, median success=25.8%, median containment time=90.0 minutes
- Broad scope proxy (Protocol/Network): n=27, mean success=40.4%, median success=10.0%, median containment time=114.0 minutes

Interpretation: narrower-scope interventions do not appear to sacrifice containment performance in this sample. They show slightly higher mean containment success, materially higher median containment success, and slightly faster median containment time. This is still a proxy test, not a direct market-wide measure of collateral disruption, but it is stronger than leaving Prediction 2 entirely unassessed.
