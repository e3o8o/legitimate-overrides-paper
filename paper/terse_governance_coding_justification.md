# TERSE governance coding justification

This note records why the TERSE revision changed the authority coding for certain high-fidelity cases.

## Coding rule used in the revision

Classify authority by the operative trigger holder that actually executed the emergency intervention, not by the broader governance environment of the protocol.

That means:

- if a guardian, council, committee, or bounded operator body executed the intervention:
  classify as `Delegated Body`
- if a core team or keyholding operator path executed the intervention directly:
  classify as `Signer Set`
- if the decisive intervention required an explicit collective governance process:
  classify as `Governance`

## Case-specific decisions

### Aave v2

- Previous label:
  `Governance`
- Revised label:
  `Delegated Body`
- Reason:
  the operative intervention was a Guardian pause. Even if the broader protocol also involves governance discussion and later governance process, the emergency act itself was exercised through bounded delegated authority.

### Alpha Homora V2

- Previous label:
  `Governance`
- Revised label:
  `Signer Set`
- Reason:
  the emergency response was core-team-led rather than collectively governed. The operative intervention path is better described as a concentrated operator response than as a delegated council or formal governance vote.

### Euler

- No authority recode made in this pass:
  remains outside the Governance bucket discussion
- Interpretation fix:
  Euler is now described as negotiation-dominated recovery, not as a clean example of onchain governance containment.

### Sui/Cetus

- No authority recode made in this pass:
  remains in the Governance-coded subset, but explicitly as a hybrid
- Interpretation fix:
  delegated freeze came first; governance supplied the later recovery authorization

The reviewer was right that the governance success-rate claim was too loose if it silently aggregated hybrid, guardian, and negotiated cases without saying so. This revised coding narrows the Governance subset and makes the remaining cases auditable.
