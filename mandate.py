"""Static Meridian mandate checks; weights are percentage points, not fractions."""

# Editable inputs. Holding: (issuer, business days to redeem, reserve-eligible).
HOLDINGS = {
    "Cash": ("none", 0, True),
    "Treasury bills": ("U.S. Treasury", 1, True),
    "Treasury 10-year note": ("U.S. Treasury", 1, True),
    "Global equity index fund": ("diversified fund", 2, False),
    "Investment-grade bond fund": ("diversified fund", 3, False),
    "Private real estate fund": ("diversified fund", 90, False),
    "Acme Corp bonds": ("Acme Corp", 4, False),
    "Acme Corp stock": ("Acme Corp", 1, False),
}
# Weights follow HOLDINGS insertion order, including zero positions.
CANDIDATES = {
    "A": [2, 2, 10, 60, 26, 0, 0, 0],
    "B": [1, 0, 0, 55, 20, 15, 5, 4],
    "C": [1, 1, 0, 70, 20, 0, 0, 8],
    "D": [100, 0, 0, 0, 0, 0, 0, 0],
}
RESERVE_SIZE = 100  # USD millions
QUARTERLY_DISTRIBUTION = 0.75  # USD millions
QUARTERS_TO_COVER = 4
LIQUIDITY_WINDOW = 5  # business days
MINIMUM_LIQUID_SHARE = 90
ISSUER_LIMIT = 8
EXEMPT_ISSUERS = {"none", "U.S. Treasury", "diversified fund"}

import math
from collections import defaultdict


def check(weights, reserve_minimum):
    if len(weights) != len(HOLDINGS):
        raise ValueError("Supply one weight for each holding, including zeros")
    if not all(math.isfinite(weight) for weight in weights):
        raise ValueError("Weights must be finite numbers")
    reserve = 0.0
    liquid = 0.0
    companies = defaultdict(float)
    for weight, (issuer, days, eligible) in zip(weights, HOLDINGS.values()):
        if eligible:
            reserve += weight
        if days <= LIQUIDITY_WINDOW:
            liquid += weight
        if issuer not in EXEMPT_ISSUERS:
            companies[issuer] += weight
    total = sum(weights)
    lowest = min(weights)
    largest = max(companies.values(), default=0.0)
    return [
        ("Weights sum to 100", total, math.isclose(total, 100, rel_tol=0, abs_tol=1e-9)),
        ("Long-only (lowest weight)", lowest, lowest >= 0),
        (f"Reserve >= {reserve_minimum:.1f}%", reserve, reserve >= reserve_minimum),
        (f"Redeemable in {LIQUIDITY_WINDOW} days >= {MINIMUM_LIQUID_SHARE:.1f}%", liquid, liquid >= MINIMUM_LIQUID_SHARE),
        (f"Largest single company <= {ISSUER_LIMIT:.1f}%", largest, largest <= ISSUER_LIMIT),
    ]


def main():
    if RESERVE_SIZE <= 0:
        raise ValueError("Reserve size must be positive")
    reserve_minimum = QUARTERS_TO_COVER * QUARTERLY_DISTRIBUTION / RESERVE_SIZE * 100
    print(f"Reserve minimum: {reserve_minimum:.1f}% of the portfolio.")
    for name, weights in CANDIDATES.items():
        print(f"\nCandidate {name}")
        results = check(weights, reserve_minimum)
        for label, value, passed in results:
            print(f"{label}: {value:.1f} {'pass' if passed else 'FAIL'}")
        print("Calendar-year loss: requires CIO clarification")
        failures = sum(not passed for _, _, passed in results)
        print("passes every checkable rule" if not failures else f"fails {failures} rule(s)")


if __name__ == "__main__":
    main()
