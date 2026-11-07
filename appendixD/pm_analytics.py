# Listing D.1 Loading the project data
"""Data-driven project control for HealthSync: AgileEVM and schedule risk."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA = Path("data")
BUDGET = 2_600_000      # software release budget (K)
MVP_POINTS = 640        # release baseline scope
PLANNED_VELOCITY = 68   # points a sprint in the release plan


def load_sprints(path: Path = DATA / "healthsync_sprints.csv") -> pd.DataFrame:
    """Load sprint records and add running totals."""
    df = pd.read_csv(path)
    df["cum_points"] = df["points_done"].cumsum()
    df["cum_mvp_points"] = df["mvp_points_done"].cumsum()
    df["cum_cost"] = df["actual_cost"].cumsum()
    return df


def load_network(path: Path = DATA / "migration_network.csv") -> pd.DataFrame:
    """Load activities, three-point estimates and predecessors."""
    df = pd.read_csv(path, dtype={"predecessors": str})
    df["predecessors"] = df["predecessors"].fillna("").str.split()
    return df.set_index("id")


# Listing D.2 AgileEVM measures for every sprint
def agile_evm(df: pd.DataFrame) -> pd.DataFrame:
    """Add PV, EV, AC, SPI, CPI and EAC against the MVP baseline."""
    out = df.copy()
    planned = (out["sprint"] * PLANNED_VELOCITY).clip(upper=MVP_POINTS)
    out["pv"] = planned / MVP_POINTS * BUDGET
    out["ev"] = out["cum_mvp_points"] / MVP_POINTS * BUDGET
    out["ac"] = out["cum_cost"]
    out["spi"] = out["ev"] / out["pv"]
    out["cpi"] = out["ev"] / out["ac"]
    out["eac"] = BUDGET / out["cpi"]
    return out


# Listing D.3 Applying the escalation thresholds
def status(index: float) -> str:
    """Return the reporting level for a performance index."""
    if index < 0.90:
        return "red: tell the investment committee"
    if index < 0.95:
        return "amber: steering group, with a recovery plan"
    return "green: within tolerance"


def flag_breaches(evm: pd.DataFrame) -> list[str]:
    """List every sprint in which SPI or CPI breaches a threshold."""
    warnings = []
    for row in evm.itertuples():
        for name in ("spi", "cpi"):
            value = getattr(row, name)
            if value < 0.95:
                warnings.append(
                    f"Sprint {row.sprint}: {name.upper()} {value:.3f}, "
                    f"{status(value)}"
                )
    return warnings


# Listing D.4 Sampling durations and running the network
RNG = np.random.default_rng(42)  # fixed seed: results can be reproduced


def pert_sample(o: float, m: float, p: float, n: int) -> np.ndarray:
    """Draw n durations from a PERT (scaled beta) distribution."""
    if p == o:
        return np.full(n, float(m))
    a = 1 + 4 * (m - o) / (p - o)
    b = 1 + 4 * (p - m) / (p - o)
    return o + (p - o) * RNG.beta(a, b, n)


def simulate(net: pd.DataFrame, n: int = 10_000) -> np.ndarray:
    """Return n simulated finish times for the whole network."""
    dur = {
        k: pert_sample(r.optimistic, r.most_likely, r.pessimistic, n)
        for k, r in net.iterrows()
    }
    finish: dict[str, np.ndarray] = {}
    for k, r in net.iterrows():  # activities are listed in network order
        preds = r.predecessors
        start = (np.max([finish[p] for p in preds], axis=0)
                 if preds else np.zeros(n))
        finish[k] = start + dur[k]
    return finish[net.index[-1]]


# Listing D.5 Reading the simulation
def summarise(finish: np.ndarray, target: float = 100) -> dict[str, float]:
    """Chance of meeting the target and the P50, P80 and P90 dates."""
    return {
        "p_within_target": float((finish <= target).mean()),
        "p50": float(np.percentile(finish, 50)),
        "p80": float(np.percentile(finish, 80)),
        "p90": float(np.percentile(finish, 90)),
    }


# Listing D.6 Charts for the steering group
def plot_histogram(finish: np.ndarray, s: dict[str, float],
                   path: str = "schedule_risk.png") -> None:
    """Save a histogram of finish times with the P50 and P80 dates."""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.hist(finish, bins=50, color="#0E9AA7", alpha=0.8)
    for key, colour in (("p50", "#1B2A41"), ("p80", "#B5402A")):
        ax.axvline(s[key], color=colour, linestyle="--",
                   label=f"{key.upper()}: {s[key]:.0f} days")
    ax.axvline(100, color="#C9A227", label="Target: 100 days")
    ax.set_xlabel("Working days from the start of Month 2")
    ax.set_ylabel("Number of simulated runs")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


# Listing D.7 Running the workflow
def main() -> None:
    """Run the analysis, print a summary and export the results."""
    evm = agile_evm(load_sprints())
    cols = ["sprint", "pv", "ev", "ac", "spi", "cpi", "eac"]
    table = evm[cols].round({"spi": 3, "cpi": 3})
    for c in ("pv", "ev", "ac", "eac"):
        table[c] = table[c].round().astype(int)
    print(table.to_string(index=False))
    for line in flag_breaches(evm):
        print(line)

    finish = simulate(load_network())
    s = summarise(finish)
    print(f"Chance of finishing within 100 days: {s['p_within_target']:.0%}")
    print(f"P50 {s['p50']:.0f}, P80 {s['p80']:.0f}, P90 {s['p90']:.0f} days")
    plot_histogram(finish, s)

    with pd.ExcelWriter("pm_report.xlsx") as xl:
        evm[cols].to_excel(xl, sheet_name="AgileEVM", index=False)
        pd.DataFrame([s]).to_excel(xl, sheet_name="Schedule risk",
                                   index=False)
    evm[cols].to_csv("agile_evm.csv", index=False)  # for other tools
    print("Report saved to pm_report.xlsx and agile_evm.csv")


if __name__ == "__main__":
    main()
