from __future__ import annotations

import csv
import statistics
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "lif_intervention_metrics.csv"
OUT = ROOT / "data" / "terse_revision_metrics_summary.md"


def load_rows() -> list[dict[str, str]]:
    with DATA.open() as f:
        return list(csv.DictReader(f))


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def compute() -> str:
    rows = load_rows()

    by_authority: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_authority.setdefault(row["authority"], []).append(row)

    precise = [r for r in rows if r["scope"] in ("Account", "Module")]
    broad = [r for r in rows if r["scope"] in ("Protocol", "Network")]

    precise_success = [float(r["containment_success_pct"]) for r in precise]
    broad_success = [float(r["containment_success_pct"]) for r in broad]
    precise_time = [float(r["time_to_contain_min"]) for r in precise]
    broad_time = [float(r["time_to_contain_min"]) for r in broad]

    governance = by_authority.get("Governance", [])
    governance_success = [float(r["containment_success_pct"]) for r in governance]

    lines = [
        "# TERSE revision metrics summary",
        "",
        "Generated from `data/lif_intervention_metrics.csv` for the TERSE revision pass.",
        "",
        "## Authority-level containment success",
        "",
    ]

    for authority in ("Signer Set", "Delegated Body", "Governance"):
        subset = by_authority.get(authority, [])
        values = [float(r["containment_success_pct"]) for r in subset]
        lines.append(
            f"- {authority}: n={len(subset)}, mean containment success={mean(values):.1f}%, median={statistics.median(values):.1f}%"
        )

    lines.extend(
        [
            "",
            "## Governance-coded cases in the current 52-case high-fidelity subset",
            "",
        ]
    )
    for row in governance:
        lines.append(
            f"- {row['protocol']} ({row['incident_id']}): scope={row['scope']}, success={float(row['containment_success_pct']):.1f}%"
        )

    lines.extend(
        [
            "",
            "## Prediction 2 proxy check",
            "",
            "Operationalization used for the TERSE revision: treat scope breadth as a proxy for blast potential, and compare narrower interventions (Account/Module) against broader interventions (Protocol/Network). Asset scope is excluded from this proxy because issuer-controlled freezes and bridge-specific asset controls are not directly comparable to protocol/network shutdown behavior.",
            "",
            f"- Precise scope proxy (Account/Module): n={len(precise)}, mean success={mean(precise_success):.1f}%, median success={statistics.median(precise_success):.1f}%, median containment time={statistics.median(precise_time):.1f} minutes",
            f"- Broad scope proxy (Protocol/Network): n={len(broad)}, mean success={mean(broad_success):.1f}%, median success={statistics.median(broad_success):.1f}%, median containment time={statistics.median(broad_time):.1f} minutes",
            "",
            "Interpretation: narrower-scope interventions do not appear to sacrifice containment performance in this sample. They show slightly higher mean containment success, materially higher median containment success, and slightly faster median containment time. This is still a proxy test, not a direct market-wide measure of collateral disruption, but it is stronger than leaving Prediction 2 entirely unassessed.",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> None:
    OUT.write_text(compute())
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
