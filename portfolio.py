"""Meridian lab: course-authored training values, not market estimates."""

# Editable inputs: returns, volatilities, and weights use decimal fractions.
SLEEVES = {
    "Treasury bills": {"expected_return": 0.035, "volatility": 0.005},
    "Treasury 10-year note": {"expected_return": 0.043, "volatility": 0.070},
    "Investment-grade bond fund": {"expected_return": 0.050, "volatility": 0.060},
    "Global equity index fund": {"expected_return": 0.080, "volatility": 0.160},
}
# Rows and columns follow SLEEVES order.
CORRELATIONS = [
    [1.00, 0.10, 0.05, 0.00],
    [0.10, 1.00, 0.80, -0.10],
    [0.05, 0.80, 1.00, 0.25],
    [0.00, -0.10, 0.25, 1.00],
]
# CPI is a labelled course estimate; objective = 2.5% CPI + 4%.
OBJECTIVE_RETURN = 0.065
RESERVE_ELIGIBLE = ("Treasury bills", "Treasury 10-year note")
BENCHMARK_WEIGHTS = {
    "Treasury bills": 0.0,
    "Treasury 10-year note": 0.0,
    "Investment-grade bond fund": 0.4,
    "Global equity index fund": 0.6,
}

import math
import sys


def validate_inputs(sleeves, correlations):
    """Reject malformed inputs before any portfolio calculation."""
    n = len(sleeves)
    if not n or len(correlations) != n or any(len(row) != n for row in correlations):
        raise ValueError("Correlation table must be square, with one row per sleeve.")
    for name, inputs in sleeves.items():
        if not math.isfinite(inputs["expected_return"]):
            raise ValueError(f"{name}: expected return must be finite.")
        if not math.isfinite(inputs["volatility"]) or inputs["volatility"] <= 0:
            raise ValueError(f"{name}: volatility must be finite and positive.")
    for i in range(n):
        for j in range(n):
            value = correlations[i][j]
            if not math.isfinite(value) or not -1 <= value <= 1:
                raise ValueError(f"Correlation [{i}, {j}] must be between -1 and 1.")
            if not math.isclose(value, correlations[j][i], rel_tol=0, abs_tol=1e-12):
                raise ValueError(f"Correlation table is not symmetric at [{i}, {j}].")
        if not math.isclose(correlations[i][i], 1.0, rel_tol=0, abs_tol=1e-12):
            raise ValueError("Correlation table diagonal must equal 1.")


def build_covariance_matrix(sleeves, correlations):
    validate_inputs(sleeves, correlations)
    volatilities = [item["volatility"] for item in sleeves.values()]
    return [
        [correlations[i][j] * vi * vj for j, vj in enumerate(volatilities)]
        for i, vi in enumerate(volatilities)
    ]


def benchmark_weights(sleeves, allocation):
    if set(allocation) != set(sleeves):
        raise ValueError("Benchmark must specify a weight for every sleeve.")
    weights = [allocation[name] for name in sleeves]
    if any(not math.isfinite(w) or w < 0 for w in weights):
        raise ValueError("Benchmark weights must be finite and nonnegative.")
    if not math.isclose(sum(weights), 1.0, rel_tol=0, abs_tol=1e-12):
        raise ValueError("Benchmark weights must sum to 100%.")
    return weights


def equal_weights(sleeves):
    return [1.0 / len(sleeves)] * len(sleeves)


def inverse_volatility_weights(sleeves):
    inverse_vols = [1.0 / item["volatility"] for item in sleeves.values()]
    total = sum(inverse_vols)
    return [value / total for value in inverse_vols]


def expected_return(weights, sleeves):
    return sum(w * item["expected_return"] for w, item in zip(weights, sleeves.values()))


def portfolio_variance(weights, covariance):
    return sum(
        wi * wj * covariance[i][j]
        for i, wi in enumerate(weights)
        for j, wj in enumerate(weights)
    )


def portfolio_volatility(weights, covariance):
    variance = portfolio_variance(weights, covariance)
    if variance < -1e-12:
        raise ValueError("Negative portfolio variance: check the correlation inputs.")
    return math.sqrt(max(variance, 0.0))


def reserve_eligible_weight(weights, sleeves, eligible):
    return sum(w for name, w in zip(sleeves, weights) if name in eligible)


def meets_objective(return_value, objective):
    return return_value >= objective


def print_portfolio(name, weights, sleeves, covariance, eligible, objective):
    print(f"\n{name}")
    for sleeve, weight in zip(sleeves, weights):
        print(f"  {sleeve}: {weight:.1%}")
    return_value = expected_return(weights, sleeves)
    print(f"  Expected return: {return_value:.2%}")
    print(f"  Volatility: {portfolio_volatility(weights, covariance):.2%}")
    print(f"  Reserve-eligible weight: {reserve_eligible_weight(weights, sleeves, eligible):.1%}")
    print(f"  Meets {objective:.2%} expected-return objective: "
          f"{'YES' if meets_objective(return_value, objective) else 'NO'}")


def main():
    covariance = build_covariance_matrix(SLEEVES, CORRELATIONS)
    portfolios = {
        "Benchmark": benchmark_weights(SLEEVES, BENCHMARK_WEIGHTS),
        "Equal weight": equal_weights(SLEEVES),
        "Inverse volatility": inverse_volatility_weights(SLEEVES),
    }
    print("Meridian: course-authored training values, not market estimates.")
    print(f"Expected-return objective: {OBJECTIVE_RETURN:.2%}")
    for name, weights in portfolios.items():
        print_portfolio(name, weights, SLEEVES, covariance, RESERVE_ELIGIBLE, OBJECTIVE_RETURN)
    print("\nVolatility is not a maximum loss. Expected returns are not guarantees.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        sys.exit(1)
