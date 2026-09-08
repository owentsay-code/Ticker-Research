"""Five-year FCFF DCF. Dollar amounts and shares are in millions."""

# Editable inputs: rates are decimals (0.08 means 8%).
STARTING_FCFF = 100
YEARLY_GROWTH_RATES = [0.08, 0.06, 0.05, 0.04, 0.03]
WACC = 0.10
TERMINAL_GROWTH = 0.03
NON_OPERATING_CASH = 50
DEBT = 300
DILUTED_SHARES = 50


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


if __name__ == "__main__":
    main()
