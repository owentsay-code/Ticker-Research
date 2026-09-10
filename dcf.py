"""Five-year FCFF DCF. Dollar amounts and shares are in millions."""

# Editable inputs: rates are decimals (0.08 means 8%).
# Training case. Dollar amounts and shares are in millions.
STARTING_FCFF = 100
YEARLY_GROWTH_RATES = [0.08, 0.06, 0.05, 0.04, 0.03]
WACC = 0.10
TERMINAL_GROWTH = 0.03
NON_OPERATING_CASH = 50
DEBT = 300
DILUTED_SHARES = 50

SENSITIVITY_WACCS = [0.09, 0.10, 0.11]
SENSITIVITY_TERMINAL_GROWTHS = [0.02, 0.03, 0.04]
TARGET_SHARE_PRICE = 30.00  # Editable USD target for the training case.
GROWTH_SHIFT_LOWER = -0.05  # -5 percentage points, added to each annual rate.
GROWTH_SHIFT_UPPER = 0.10  # +10 percentage points.


def share_value(wacc, terminal_growth, growth_rates):
    """Use the base model's conventions, holding its other inputs fixed."""
    if terminal_growth >= wacc or wacc <= -1:
        raise ValueError("invalid discount rate or terminal growth")
    fcff = STARTING_FCFF
    explicit_pv = 0.0
    for year, growth in enumerate(growth_rates, start=1):
        fcff *= 1 + growth
        explicit_pv += fcff / (1 + wacc) ** year
    terminal_value = fcff * (1 + terminal_growth) / (wacc - terminal_growth)
    enterprise_value = explicit_pv + terminal_value / (1 + wacc) ** len(growth_rates)
    return (enterprise_value + NON_OPERATING_CASH - DEBT) / DILUTED_SHARES


def print_sensitivity():
    print("\nTraining case — sensitivity: value per diluted share (USD)")
    rows = [["WACC / terminal growth"] + [f"{g:.2%}" for g in SENSITIVITY_TERMINAL_GROWTHS]]
    for wacc in SENSITIVITY_WACCS:
        row = [f"{wacc:.2%}"]
        for growth in SENSITIVITY_TERMINAL_GROWTHS:
            if growth >= wacc or wacc <= -1:
                row.append("INVALID")
            else:
                row.append(f"{share_value(wacc, growth, YEARLY_GROWTH_RATES):.4f}")
        rows.append(row)
    widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]
    for index, row in enumerate(rows):
        print(" | ".join(cell.rjust(width) for cell, width in zip(row, widths)))
        if index == 0:
            print("-+-".join("-" * width for width in widths))


def solve_growth_shift(target, lower, upper):
    """Bisect a valid bracket; return None when it does not bracket the target."""
    import math

    if not all(math.isfinite(x) for x in [target, lower, upper, *YEARLY_GROWTH_RATES]):
        raise ValueError("target, bounds, and annual growth rates must be finite")
    if lower >= upper:
        raise ValueError("lower bound must be less than upper bound")
    if any(g + lower <= -1 or g + upper <= -1 for g in YEARLY_GROWTH_RATES):
        raise ValueError("bracket pushes an annual growth rate to -100% or below")

    def residual(shift):
        value = share_value(WACC, TERMINAL_GROWTH, [g + shift for g in YEARLY_GROWTH_RATES])
        if not math.isfinite(value):
            raise ValueError("non-finite valuation in bracket")
        return value - target

    low_error, high_error = residual(lower), residual(upper)
    if low_error == 0:
        return lower
    if high_error == 0:
        return upper
    if (low_error > 0) == (high_error > 0):
        return None
    for _ in range(200):
        midpoint = (lower + upper) / 2
        error = residual(midpoint)
        if abs(error) <= 1e-8:
            return midpoint
        if midpoint == lower or midpoint == upper:
            break
        if (error > 0) == (low_error > 0):
            lower, low_error = midpoint, error
        else:
            upper = midpoint
    raise ValueError("bisection could not match the target within $0.00000001")


def print_reverse_dcf():
    print("\nTraining case — reverse DCF: uniform shift added to all five explicit growth rates")
    print(f"Target share price (USD): {TARGET_SHARE_PRICE:.4f}")
    print(f"Shift bracket (percentage points): {100 * GROWTH_SHIFT_LOWER:+.6f} to {100 * GROWTH_SHIFT_UPPER:+.6f}")
    print("Held fixed: " + "; ".join([
        f"STARTING_FCFF={STARTING_FCFF}",
        f"baseline YEARLY_GROWTH_RATES={YEARLY_GROWTH_RATES} (only uniform shift varies)",
        f"WACC={WACC}", f"TERMINAL_GROWTH={TERMINAL_GROWTH}",
        f"NON_OPERATING_CASH={NON_OPERATING_CASH}", f"DEBT={DEBT}",
        f"DILUTED_SHARES={DILUTED_SHARES}",
    ]))
    try:
        shift = solve_growth_shift(TARGET_SHARE_PRICE, GROWTH_SHIFT_LOWER, GROWTH_SHIFT_UPPER)
    except ValueError as exc:
        print(f"Reverse DCF refused: {exc}.")
        return
    if shift is None:
        print("No solution in that bracket.")
        return
    print(f"Solved shift (percentage points): {100 * shift:+.8f}")
    price = share_value(WACC, TERMINAL_GROWTH, [g + shift for g in YEARLY_GROWTH_RATES])
    print(f"Value per diluted share at solved shift (USD): {price:.8f}")


def main():
    if TERMINAL_GROWTH >= WACC:
        raise SystemExit("Error: terminal growth must be less than WACC.")
    if len(YEARLY_GROWTH_RATES) != 5:
        raise SystemExit("Error: provide exactly five yearly growth rates.")
    if WACC <= -1:
        raise SystemExit("Error: WACC must be greater than -1.")
    if DILUTED_SHARES <= 0:
        raise SystemExit("Error: diluted shares must be positive.")

    yearly_fcff = []
    fcff = STARTING_FCFF
    for growth in YEARLY_GROWTH_RATES:
        fcff *= 1 + growth
        yearly_fcff.append(fcff)

    explicit_pv = sum(
        cash_flow / (1 + WACC) ** year
        for year, cash_flow in enumerate(yearly_fcff, start=1)
    )
    terminal_value = yearly_fcff[-1] * (1 + TERMINAL_GROWTH) / (WACC - TERMINAL_GROWTH)
    terminal_pv = terminal_value / (1 + WACC) ** len(yearly_fcff)
    enterprise_value = explicit_pv + terminal_pv
    equity_value = enterprise_value + NON_OPERATING_CASH - DEBT
    value_per_share = equity_value / DILUTED_SHARES
    if enterprise_value == 0:
        raise SystemExit("Error: enterprise value is zero; terminal-value share is undefined.")
    terminal_share = terminal_pv / enterprise_value

    for year, cash_flow in enumerate(yearly_fcff, start=1):
        print(f"Year {year} FCFF (USD millions): {cash_flow:.4f}")
    print(f"PV of five explicit FCFF (USD millions): {explicit_pv:.4f}")
    print(f"Terminal value at Year 5 (USD millions): {terminal_value:.4f}")
    print(f"PV of terminal value (USD millions): {terminal_pv:.4f}")
    print(f"Enterprise value (USD millions): {enterprise_value:.4f}")
    print(f"Equity value (USD millions): {equity_value:.4f}")
    print(f"Value per diluted share (USD): {value_per_share:.4f}")
    print(f"PV of terminal value / enterprise value (fraction): {terminal_share:.4f}")
    print_sensitivity()
    print_reverse_dcf()


if __name__ == "__main__":
    main()
