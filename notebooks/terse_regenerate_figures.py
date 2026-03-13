from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIGURES_DIR = ROOT / "paper" / "figures"

COLORS = {
    "primary_blue": "#2563EB",
    "danger_red": "#DC2626",
    "success_green": "#16A34A",
    "warning_amber": "#D97706",
    "neutral_gray": "#6B7280",
    "purple": "#7C3AED",
}

AUTHORITY_COLORS = {
    "Signer Set": COLORS["primary_blue"],
    "Delegated Body": COLORS["success_green"],
    "Governance": COLORS["purple"],
}


def setup() -> tuple[pd.DataFrame, pd.DataFrame]:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams["figure.dpi"] = 150
    plt.rcParams["savefig.dpi"] = 300
    plt.rcParams["font.family"] = "sans-serif"
    metrics = pd.read_csv(DATA_DIR / "lif_intervention_metrics.csv")
    interventions = pd.read_csv(DATA_DIR / "lif_all_interventions.csv")
    return metrics, interventions


def fig05(metrics: pd.DataFrame, interventions: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    order = ["Signer Set", "Delegated Body", "Governance"]
    auth_success = metrics.groupby("authority")["containment_success_pct"].mean().reindex(order).dropna()
    colors = [AUTHORITY_COLORS.get(a, COLORS["neutral_gray"]) for a in auth_success.index]
    axes[0].bar(range(len(auth_success)), auth_success.values, color=colors)
    axes[0].set_xticks(range(len(auth_success)))
    axes[0].set_xticklabels(auth_success.index)
    axes[0].set_ylabel("Average Containment Success (%)")
    axes[0].set_title("Containment Success by Authority", fontweight="bold")
    axes[0].set_ylim(0, 100)

    auth_prevented = (
        interventions.groupby("authority")["loss_prevented_usd"].sum().reindex(order).dropna() / 1e6
    )
    auth_prevented = auth_prevented[auth_prevented > 0]
    colors = [AUTHORITY_COLORS.get(a, COLORS["neutral_gray"]) for a in auth_prevented.index]
    axes[1].bar(range(len(auth_prevented)), auth_prevented.values, color=colors)
    axes[1].set_xticks(range(len(auth_prevented)))
    axes[1].set_xticklabels(auth_prevented.index)
    axes[1].set_ylabel("Loss Prevented ($ Millions)")
    axes[1].set_title("Total Losses Prevented by Authority", fontweight="bold")

    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "lof05_intervention_effectiveness.png", dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def fig06(interventions: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    order = ["Signer Set", "Delegated Body", "Governance"]
    auth_counts = interventions["authority"].value_counts().reindex(order).dropna()
    colors = [AUTHORITY_COLORS.get(a, COLORS["neutral_gray"]) for a in auth_counts.index]
    axes[0].pie(auth_counts.values, labels=auth_counts.index, autopct="%1.1f%%", colors=colors, startangle=90)
    axes[0].set_title("Interventions by Authority (Count)", fontweight="bold")

    auth_value = interventions.groupby("authority")["loss_prevented_usd"].sum().reindex(order).dropna()
    auth_value = auth_value[auth_value > 0]
    colors = [AUTHORITY_COLORS.get(a, COLORS["neutral_gray"]) for a in auth_value.index]
    axes[1].pie(auth_value.values, labels=auth_value.index, autopct="%1.1f%%", colors=colors, startangle=90)
    axes[1].set_title("Value Protected by Authority ($)", fontweight="bold")

    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "lof06_authority_distribution.png", dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main() -> None:
    metrics, interventions = setup()
    fig05(metrics, interventions)
    fig06(interventions)
    print("Regenerated lof05_intervention_effectiveness.png")
    print("Regenerated lof06_authority_distribution.png")


if __name__ == "__main__":
    main()
