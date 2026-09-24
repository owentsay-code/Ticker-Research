"""NVIDIA linked pro forma and assignment report. USD billions unless specified.

Run: python3 nvidia_proforma.py
Prints five annual statements, accounting checks and FCFF value per share.
Standard library only. Inputs and judgments match the September 24 NVIDIA report
in 2026-09-01/NVIDIA Project/DCF Models and Research/.
Forecasts are five rolling annual periods, not NVIDIA fiscal years.
"""
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parent
SOURCES = {
    'K24': 'https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm',
    'K25': 'https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm',
    'K26': 'https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm',
    'Q27': 'https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx',
    'Provider': 'https://stockanalysis.com/stocks/nvda/financials/cash-flow-statement/',
}
# Each annual observation is attributed to that year's own 10-K.
HISTORY = [
    dict(year=2024, source='K24', end='2024-01-28', revenue=60922, gross=44301,
         sga=2654, ni=29760, inventory=5282, ppe=3914, equity=42978,
         dep=894, da=1508, capex=1069, principal=74, tax=4058, pretax=33818,
         prior_revenue=26974, cfo=28090, debt_repaid=1250),
    dict(year=2025, source='K25', end='2025-01-26', revenue=130497, gross=97858,
         sga=3491, ni=72880, inventory=10080, ppe=6283, equity=79327,
         dep=1300, da=1864, capex=3236, principal=129, tax=11146, pretax=84026,
         prior_revenue=60922, cfo=64089, debt_repaid=1250),
    dict(year=2026, source='K26', end='2026-01-25', revenue=215938, gross=153463,
         sga=4579, ni=120067, inventory=21403, ppe=10383, equity=157293,
         dep=2400, da=2843, capex=6042, principal=101, tax=21383, pretax=141450,
         prior_revenue=130497, cfo=102718, debt_repaid=0),
]
BASE_REVENUE = 215.938 + 177.837 - 90.805
OPENING = dict(cash=22.443, securities=76.926, ar=63.059, inventory=31.575,
               prepaid=3.409, ppe=14.285, intangibles=2.998, other_assets=105.577,
               ap=15.059, accrued=26.960, debt=33.366, other_liabilities=15.903,
               equity=228.984, revenue=BASE_REVENUE)
GROWTH = (.45, .30, .20, .15, .10)
MARGINS = (.64, .62, .60, .59, .58)
GROSS_MARGINS = (.74, .73, .72, .71, .70)
TAX, DA_RATIO, CAPEX_RATIO, WC_RATIO = .17, .012, .03, .20
SBC_RATIO, INTEREST_RATE = .022, .04
SHARES, DIVIDENDS = 24.285, 24.285
WACC, TERMINAL_GROWTH = .10, .035
WC_ASSETS, WC_LIABILITIES = ('ar', 'inventory', 'prepaid'), ('ap', 'accrued')
ASSETS = ('cash', 'securities', 'ar', 'inventory', 'prepaid', 'ppe', 'intangibles', 'other_assets')
LIABILITIES = ('ap', 'accrued', 'debt', 'other_liabilities')


def nwc(row):
    return sum(row[k] for k in WC_ASSETS) - sum(row[k] for k in WC_LIABILITIES)


def near(a, b, name):
    if not math.isfinite(a) or not math.isfinite(b) or abs(a-b) > 1e-8:
        raise ValueError(f'{name}: {a} != {b}')


def project(growth=GROWTH):
    near(sum(OPENING[k] for k in ASSETS), 320.272, 'Opening assets')
    near(sum(OPENING[k] for k in LIABILITIES) + OPENING['equity'], 320.272, 'Opening balance')
    prior = OPENING.copy()
    rows = []
    for t, (growth_rate, margin, gross_margin) in enumerate(zip(growth, MARGINS, GROSS_MARGINS), 1):
        r = prior.copy()
        r.update(year=t, opening_cash=prior['cash'], opening_equity=prior['equity'])
        r['revenue'] = prior['revenue'] * (1+growth_rate)
        r['gross'] = r['revenue'] * gross_margin
        r['cogs'] = r['revenue'] - r['gross']
        r['sga'] = r['gross'] * .03
        r['ebit'] = r['revenue'] * margin
        r['rd'] = r['gross'] - r['sga'] - r['ebit']
        r['da'] = r['revenue'] * DA_RATIO
        r['amortization'] = min(prior['intangibles'], r['da'] * .15)
        r['depreciation'] = r['da'] - r['amortization']
        r['interest'] = prior['debt'] * INTEREST_RATE
        r['pretax'] = r['ebit'] - r['interest']
        r['tax'] = max(0, r['pretax']) * TAX
        r['ni'] = r['pretax'] - r['tax']
        r['capex'] = r['revenue'] * CAPEX_RATIO
        r['ppe'] = prior['ppe'] + r['capex'] - r['depreciation']
        r['intangibles'] = prior['intangibles'] - r['amortization']
        delta_nwc = (r['revenue']-prior['revenue']) * WC_RATIO
        for k in WC_ASSETS + WC_LIABILITIES:
            r[k] = prior[k] + delta_nwc * OPENING[k] / nwc(OPENING)
        r['delta_nwc'] = nwc(r) - nwc(prior)
        r['sbc'] = r['revenue'] * SBC_RATIO
        r['buybacks'] = r['sbc']
        r['dividends'] = DIVIDENDS
        r['net_borrowing'] = 0.0
        r['cfo'] = r['ni'] + r['da'] + r['sbc'] - r['delta_nwc']
        r['cfi'] = -r['capex']
        r['cff'] = r['net_borrowing'] - r['buybacks'] - r['dividends']
        r['cash_change'] = r['cfo'] + r['cfi'] + r['cff']
        r['cash'] = prior['cash'] + r['cash_change']
        r['equity'] = prior['equity'] + r['ni'] + r['sbc'] - r['buybacks'] - r['dividends']
        r['assets'] = sum(r[k] for k in ASSETS)
        r['liabilities'] = sum(r[k] for k in LIABILITIES)
        r['balance_gap'] = r['assets'] - r['liabilities'] - r['equity']
        r['cash_fcfe'] = r['cfo'] - r['capex'] + r['net_borrowing']
        r['fcfe'] = r['cash_fcfe'] - r['sbc']
        r['fcff'] = r['ebit'] * (1-TAX) + r['da'] - r['capex'] - r['delta_nwc']
        near(r['balance_gap'], 0, f'Year {t} balance sheet')
        near(r['cash']-prior['cash'], r['cash_change'], f'Year {t} cash')
        near(r['equity']-prior['equity'], r['ni']+r['sbc']-r['buybacks']-r['dividends'], f'Year {t} equity')
        near(r['delta_nwc'], delta_nwc, f'Year {t} working capital')
        near(r['ppe']+r['intangibles'], prior['ppe']+prior['intangibles']+r['capex']-r['da'], f'Year {t} assets rollforward')
        # This bridge presumes a positive taxable profit (true in this base case).
        if r['pretax'] >= 0:
            near(r['fcfe'], r['fcff']-r['interest']*(1-TAX), f'Year {t} FCFE bridge')
        if r['cash'] < 0 or r['ppe'] < 0 or r['intangibles'] < 0:
            raise ValueError(f'Year {t}: negative cash or fixed assets; revise financing assumptions')
        rows.append(r)
        prior = r
    return rows


def value(rows, wacc=WACC, growth=TERMINAL_GROWTH):
    if wacc <= growth:
        raise ValueError('Discount rate must exceed terminal growth')
    last = rows[-1]
    next_revenue = last['revenue'] * (1+growth)
    terminal_fcff = next_revenue * (MARGINS[-1]*(1-TAX)+DA_RATIO-CAPEX_RATIO) - WC_RATIO*last['revenue']*growth
    if terminal_fcff <= 0:
        raise ValueError('Nonpositive terminal FCFF: stable positive cash flow must be established first')
    explicit = sum(r['fcff']/(1+wacc)**r['year'] for r in rows)
    terminal = terminal_fcff/(wacc-growth)
    pv_terminal = terminal/(1+wacc)**5
    ev = explicit + pv_terminal
    bridge = OPENING['cash'] + OPENING['securities'] - OPENING['debt']
    return dict(explicit=explicit, terminal_fcff=terminal_fcff, terminal=terminal,
                pv_terminal=pv_terminal, ev=ev, bridge=bridge, equity=ev+bridge,
                per_share=(ev+bridge)/SHARES, terminal_share=pv_terminal/ev)



def print_table(title, fields, rows):
    print("\n" + title + " (USD billions)")
    print(f"{'Line item':<39}" + "".join(f"{'Year ' + str(r['year']):>15}" for r in rows))
    for label, key, sign in fields:
        print(f"{label:<39}" + "".join(f"{r[key]*sign:>15,.3f}" for r in rows))


def check_block(rows):
    print("\nCHECK BLOCK (gaps in USD billions; tolerance 0.00000001)")
    prior = OPENING
    for r in rows:
        year = r['year']
        checks = {
            'Balance sheet gap': sum(r[k] for k in ASSETS) - sum(r[k] for k in LIABILITIES) - r['equity'],
            'Cash reconciliation gap': r['cash'] - prior['cash'] - r['cfo'] - r['cfi'] - r['cff'],
            'Equity rollforward gap': r['equity'] - prior['equity'] - r['ni'] - r['sbc'] + r['buybacks'] + r['dividends'],
            'Fixed asset rollforward gap': r['ppe'] + r['intangibles'] - prior['ppe'] - prior['intangibles'] - r['capex'] + r['da'],
            'Working capital gap': nwc(r) - nwc(prior) - WC_RATIO*(r['revenue']-prior['revenue']),
        }
        for name, gap in checks.items():
            near(gap, 0, f'Year {year} {name}')
            print(f'Year {year} | {name:<29} | {gap: .12f} | PASS')
        if not math.isfinite(r['cash']) or r['cash'] < 0:
            raise ValueError(f'Year {year}: cash below zero; gap = {r["cash"]:.12f}')
        print(f'Year {year} | Cash at or above zero         | {r["cash"]: .12f} | PASS')
        print(f'Year {year} | ' + ('negative FCFE' if r['fcfe'] < 0 else 'Positive FCFE'))
        prior = r


def main():
    rows = project()
    print('NVIDIA Corporation (NVDA) — five-year rolling pro forma')
    print('Opening balance sheet: July 26, 2026. Assumptions: September 24, 2026 report.')
    print_table('INCOME STATEMENT', [
        ('Revenue','revenue',1), ('Cost of revenue','cogs',-1), ('Gross profit','gross',1),
        ('SG&A','sga',-1), ('R&D','rd',-1), ('Operating income','ebit',1),
        ('Interest expense','interest',-1), ('Pretax income','pretax',1),
        ('Tax expense','tax',-1), ('Net income','ni',1)], rows)
    print_table('BALANCE SHEET', [
        ('Cash','cash',1), ('Marketable securities','securities',1), ('Accounts receivable','ar',1),
        ('Inventory','inventory',1), ('Prepaid assets','prepaid',1), ('PP&E net','ppe',1),
        ('Intangibles net','intangibles',1), ('Other assets','other_assets',1), ('Total assets','assets',1),
        ('Accounts payable','ap',1), ('Accrued liabilities','accrued',1), ('Debt','debt',1),
        ('Other liabilities','other_liabilities',1), ('Total liabilities','liabilities',1),
        ('Shareholders equity','equity',1)], rows)
    print_table('CASH FLOW STATEMENT', [
        ('Net income','ni',1), ('D&A add back','da',1), ('Stock compensation add back','sbc',1),
        ('Change in working capital','delta_nwc',-1), ('Operating cash flow','cfo',1),
        ('Capital expenditure / investing','cfi',1), ('Net borrowing','net_borrowing',1),
        ('Buybacks','buybacks',-1), ('Dividends','dividends',-1), ('Financing cash flow','cff',1),
        ('Net cash change','cash_change',1), ('Opening cash','opening_cash',1), ('Closing cash','cash',1)], rows)
    print_table('CHANGES IN EQUITY', [
        ('Opening equity','opening_equity',1), ('Net income','ni',1), ('Stock compensation','sbc',1),
        ('Buybacks','buybacks',-1), ('Dividends','dividends',-1), ('Closing equity','equity',1)], rows)
    print_table('FREE CASH FLOW', [
        ('Cash FCFE before distributions','cash_fcfe',1), ('Stock compensation economic cost','sbc',-1),
        ('Economic FCFE','fcfe',1), ('Economic FCFF','fcff',1)], rows)
    check_block(rows)
    result = value(rows)
    print('\nVALUATION — economic FCFF discounted at WACC, not FCFE')
    print(f'WACC: {WACC:.1%}; terminal growth: {TERMINAL_GROWTH:.1%}')
    print(f'PV of five years of FCFF: ${result["explicit"]:,.3f} billion')
    print(f'PV of terminal value: ${result["pv_terminal"]:,.3f} billion')
    print(f'Enterprise value: ${result["ev"]:,.3f} billion')
    print(f'Equity value: ${result["equity"]:,.3f} billion')
    print(f'Diluted share proxy: {SHARES:,.3f} billion')
    print(f'VALUE PER SHARE: ${result["per_share"]:,.2f}')


if __name__ == '__main__':
    main()
