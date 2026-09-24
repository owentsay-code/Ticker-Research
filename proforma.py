"""ABG five-year pro forma. USD and shares in millions, except per-share value.

Inputs are supplied assignment assumptions, not independently verified data.
FCFE follows the assignment formula before revolver draws and repayments.
Revolver movements are shown separately in the cash flow statement.
"""

import math


YEARS = (2026, 2027, 2028, 2029, 2030)
GROWTH = 0.018  # Judgment
GROSS_MARGIN = 0.1705  # Judgment
SGA_RATIOS = (0.665, 0.655, 0.645, 0.645, 0.645)  # Judgment
DEPRECIATION_RATIO = 82.4 / 3070.4  # History
IMPAIRMENT = 120.0  # Judgment; non-cash
CAPEX = 250.0  # Guidance for 2026; carrying forward is judgment
TAX_RATE = 0.255  # Judgment; assignment tax convention
INVENTORY_DAYS = 2135.8 / (17999.0 - 3071.7) * 365  # History
FLOOR_PLAN_RATIO = 2027.0 / 2135.8  # History
OTHER_WORKING_CAPITAL_RATIO = 0.008  # Judgment
MINIMUM_CASH = 25.0  # History
REVOLVER_LIMIT = 850.0  # Judgment; maximum outstanding balance
REVOLVER_RATE = 0.06  # Judgment
DEBT_REPAYMENT = 150.0  # Judgment
BUYBACK = 150.0  # Judgment
FLOOR_PLAN_RATE = 0.0467  # History
DEBT_RATE = 0.0544  # History
COST_OF_EQUITY = 0.10  # Judgment
TERMINAL_GROWTH = 0.025  # Judgment
SHARES = 17.951349  # Supplied fact: June 30, 2026 10-Q
TOLERANCE = 1e-7  # USD millions; only accommodates floating-point noise

OPENING = {
    "revenue": 17999.0,
    "inventory": 2135.8,
    "ppe": 3070.4,
    "other_assets": 6371.6,
    "cash": 40.4,
    "floor_plan": 2027.0,
    "debt": 3572.0,
    "revolver": 0.0,
    "other_liabilities": 2127.5,
    "equity": 3891.7,
}


def balance_gap(row):
    assets = row["cash"] + row["inventory"] + row["ppe"] + row["other_assets"]
    liabilities = (
        row["floor_plan"] + row["debt"] + row["revolver"]
        + row["other_liabilities"]
    )
    return assets - liabilities - row["equity"]


def project():
    """Build each year's statements from the prior closing balances."""
    opening_gap = balance_gap(OPENING)
    if not math.isfinite(opening_gap) or abs(opening_gap) > TOLERANCE:
        raise ValueError(f"2025 opening balance sheet gap: {opening_gap:.8f}")
    prior = OPENING.copy()
    projections = []
    for year, sga_ratio in zip(YEARS, SGA_RATIOS):
        row = {"year": year}
        row["revenue"] = prior["revenue"] * (1 + GROWTH)
        row["gross_profit"] = row["revenue"] * GROSS_MARGIN
        row["sga"] = row["gross_profit"] * sga_ratio
        row["depreciation"] = prior["ppe"] * DEPRECIATION_RATIO
        row["impairment"] = IMPAIRMENT
        row["operating_income"] = (
            row["gross_profit"] - row["sga"] - row["depreciation"] - IMPAIRMENT
        )
        row["interest"] = (
            prior["floor_plan"] * FLOOR_PLAN_RATE
            + prior["debt"] * DEBT_RATE
            + prior["revolver"] * REVOLVER_RATE
        )
        row["pretax"] = row["operating_income"] - row["interest"]
        row["tax"] = max(0.0, row["pretax"]) * TAX_RATE
        row["net_income"] = row["pretax"] - row["tax"]

        row["cost_of_sales"] = row["revenue"] - row["gross_profit"]
        row["inventory"] = row["cost_of_sales"] * INVENTORY_DAYS / 365
        row["floor_plan"] = row["inventory"] * FLOOR_PLAN_RATIO
        row["capex"] = CAPEX
        row["ppe"] = prior["ppe"] + CAPEX - row["depreciation"]
        row["change_other_wc"] = (
            OTHER_WORKING_CAPITAL_RATIO * (row["revenue"] - prior["revenue"])
        )
        row["other_assets"] = (
            prior["other_assets"] + row["change_other_wc"] - IMPAIRMENT
        )
        row["repayment"] = DEBT_REPAYMENT
        if row["repayment"] > prior["debt"]:
            raise ValueError(f"{year}: scheduled repayment exceeds opening debt")
        row["debt"] = prior["debt"] - row["repayment"]
        row["other_liabilities"] = prior["other_liabilities"]
        row["buyback"] = BUYBACK
        row["equity"] = prior["equity"] + row["net_income"] - BUYBACK

        row["change_inventory"] = row["inventory"] - prior["inventory"]
        row["change_floor_plan"] = row["floor_plan"] - prior["floor_plan"]
        row["fcfe"] = (
            row["net_income"] + row["depreciation"] + IMPAIRMENT - CAPEX
            - row["change_inventory"] - row["change_other_wc"]
            + row["change_floor_plan"] - row["repayment"]
        )
        cash_before_revolver = prior["cash"] + row["fcfe"] - BUYBACK
        row["revolver_draw"] = min(
            max(0.0, MINIMUM_CASH - cash_before_revolver),
            max(0.0, REVOLVER_LIMIT - prior["revolver"]),
        )
        row["revolver_repayment"] = min(
            prior["revolver"], max(0.0, cash_before_revolver - MINIMUM_CASH)
        )
        row["revolver"] = (
            prior["revolver"] + row["revolver_draw"] - row["revolver_repayment"]
        )
        row["opening_cash"] = prior["cash"]
        row["net_cash_change"] = (
            row["fcfe"] - BUYBACK + row["revolver_draw"] - row["revolver_repayment"]
        )
        row["cash"] = prior["cash"] + row["net_cash_change"]
        row["assets"] = sum(row[k] for k in ("cash", "inventory", "ppe", "other_assets"))
        row["liabilities"] = sum(
            row[k] for k in ("floor_plan", "debt", "revolver", "other_liabilities")
        )
        row["liabilities_equity"] = row["liabilities"] + row["equity"]
        row["balance_gap"] = balance_gap(row)
        row["cash_headroom"] = row["cash"] - MINIMUM_CASH
        projections.append(row)
        prior = row
    return projections


def assert_balanced(projections):
    """Recompute checks so altered balances cannot pass with stale check fields."""
    for row in projections:
        year = row["year"]
        checks = (
            ("assets minus liabilities minus equity", balance_gap(row), False),
            ("cash minus minimum", row["cash"] - MINIMUM_CASH, True),
            ("revolver capacity", REVOLVER_LIMIT - row["revolver"], True),
            ("cash reconciliation", row["cash"] - row["opening_cash"]
             - row["net_cash_change"], False),
        )
        for name, gap, lower_bound in checks:
            failed = gap < -TOLERANCE if lower_bound else abs(gap) > TOLERANCE
            if not math.isfinite(gap) or failed:
                raise ValueError(f"{year}: {name} check failed; gap = {gap:.8f} million")


def print_table(title, lines, projections):
    print(f"\n{title} (USD millions)")
    print(f"{'Line item':<42}" + "".join(f"{r['year']:>14}" for r in projections))
    print("-" * (42 + 14 * len(projections)))
    for label, key, sign in lines:
        values = [sign * row[key] for row in projections]
        # Suppress negative zero in printed check residuals, not calculations.
        print(f"{label:<42}" + "".join(
            f"{(0.0 if abs(value) < TOLERANCE else value):>14,.1f}"
            for value in values
        ))


def value_equity(projections):
    assert_balanced(projections)
    if tuple(row["year"] for row in projections) != YEARS:
        raise ValueError("Valuation requires exactly 2026 through 2030 in order")
    if not all(math.isfinite(x) for x in (COST_OF_EQUITY, TERMINAL_GROWTH, SHARES)):
        raise ValueError("Valuation inputs must be finite")
    if COST_OF_EQUITY <= -1 or TERMINAL_GROWTH <= -1 or TERMINAL_GROWTH >= COST_OF_EQUITY:
        raise ValueError("Require cost of equity > terminal growth > -100%")
    if SHARES <= 0:
        raise ValueError("Shares outstanding must be positive")
    explicit_pv = sum(
        row["fcfe"] / (1 + COST_OF_EQUITY) ** t
        for t, row in enumerate(projections, start=1)
    )
    final = projections[-1]
    terminal_value = (
        (final["fcfe"] + final["repayment"]) * (1 + TERMINAL_GROWTH)
        / (COST_OF_EQUITY - TERMINAL_GROWTH)
    )
    terminal_pv = terminal_value / (1 + COST_OF_EQUITY) ** 5
    equity_value = explicit_pv + terminal_pv
    if not math.isfinite(equity_value) or equity_value == 0:
        raise ValueError("Equity value must be finite and nonzero")
    return equity_value, terminal_pv / equity_value, equity_value / SHARES


def main():
    projections = project()
    print("ABG pro forma: 2026-2030; supplied assignment conventions")
    print_table("INCOME STATEMENT", [
        ("Revenue", "revenue", 1),
        ("Cost of sales", "cost_of_sales", -1),
        ("Gross profit", "gross_profit", 1),
        ("SG&A", "sga", -1),
        ("Depreciation", "depreciation", -1),
        ("Impairment", "impairment", -1),
        ("Operating income", "operating_income", 1),
        ("Interest", "interest", -1),
        ("Pretax income", "pretax", 1),
        ("Tax", "tax", -1),
        ("Net income", "net_income", 1),
    ], projections)
    print_table("BALANCE SHEET", [
        ("Cash", "cash", 1),
        ("Inventory", "inventory", 1),
        ("PP&E", "ppe", 1),
        ("Other assets", "other_assets", 1),
        ("Total assets", "assets", 1),
        ("Floor plan", "floor_plan", 1),
        ("Term debt", "debt", 1),
        ("Revolver", "revolver", 1),
        ("Other liabilities", "other_liabilities", 1),
        ("Total liabilities", "liabilities", 1),
        ("Equity", "equity", 1),
        ("Total liabilities and equity", "liabilities_equity", 1),
    ], projections)
    print_table("CASH FLOW / FCFE BRIDGE", [
        ("Net income", "net_income", 1),
        ("Depreciation add-back", "depreciation", 1),
        ("Impairment add-back", "impairment", 1),
        ("Capital spending", "capex", -1),
        ("Change in inventory (cash effect)", "change_inventory", -1),
        ("Change in other WC (cash effect)", "change_other_wc", -1),
        ("Change in floor plan", "change_floor_plan", 1),
        ("Term debt repayment", "repayment", -1),
        ("FCFE before revolver movements", "fcfe", 1),
        ("Share buyback", "buyback", -1),
        ("Revolver draw", "revolver_draw", 1),
        ("Revolver repayment", "revolver_repayment", -1),
        ("Net change in cash", "net_cash_change", 1),
        ("Opening cash", "opening_cash", 1),
        ("Closing cash", "cash", 1),
    ], projections)
    print_table("CHECKS", [
        ("Assets - liabilities - equity", "balance_gap", 1),
        ("Cash above minimum (must be >= 0)", "cash_headroom", 1),
    ], projections)
    print(f"{'Cash at or above minimum':<42}" + "".join(
        f"{'PASS' if r['cash_headroom'] >= -TOLERANCE else 'FAIL':>14}"
        for r in projections
    ))
    equity_value, terminal_share, per_share = value_equity(projections)
    print(f"\nEquity value (USD millions): {equity_value:,.2f}")
    print(f"Share of value after 2030: {terminal_share:.2%}")
    print(f"Value per share (USD): {per_share:,.2f}")


if __name__ == "__main__":
    main()
