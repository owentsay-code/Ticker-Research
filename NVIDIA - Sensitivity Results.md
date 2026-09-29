# NVIDIA — one-at-a-time sensitivity results

Generated: 2026-09-29T13:56:40.763059-04:00

Source: existing `nvidia_proforma.py`; no new company data. Years 1–5 are rolling annual periods, not fiscal years.

Every run uses a fresh isolated model and a deep copy of `nvidia_base_inputs.json`. Only the named driver path changes; all other independent inputs reset to base. Linked statement quantities recalculate. Ranges are the previously selected ±5 percentage points in all five years.

Outputs: Year 5 operating profit (EBIT) and economic FCFF in USD billions; value per share in USD/share. Changes and spans use unrounded results. Negative flows remain signed. Invalid runs are flagged and excluded from spans; no ranking is produced.

Valuation retains the existing FCFF method: 10% WACC, 3.5% terminal growth, normalized terminal reinvestment, and 24.285 billion shares. These are existing scenario assumptions, not newly verified market inputs.

## Actual input paths

| Run | Annual revenue growth, Years 1–5 (%) | EBIT margin, Years 1–5 (% of revenue) |
| --- | --- | --- |
| Initial base | 45%, 30%, 20%, 15%, 10% | 64%, 62%, 60%, 59%, 58% |
| Revenue growth: lower | 40%, 25%, 15%, 10%, 5% | 64%, 62%, 60%, 59%, 58% |
| Revenue growth: base | 45%, 30%, 20%, 15%, 10% | 64%, 62%, 60%, 59%, 58% |
| Revenue growth: higher | 50%, 35%, 25%, 20%, 15% | 64%, 62%, 60%, 59%, 58% |
| EBIT margin: lower | 45%, 30%, 20%, 15%, 10% | 59%, 57%, 55%, 54%, 53% |
| EBIT margin: base | 45%, 30%, 20%, 15%, 10% | 64%, 62%, 60%, 59%, 58% |
| EBIT margin: higher | 45%, 30%, 20%, 15%, 10% | 69%, 67%, 65%, 64%, 63% |
| Restored base | 45%, 30%, 20%, 15%, 10% | 64%, 62%, 60%, 59%, 58% |

## Results and signed changes from base

| Run | Status | EBIT ($bn) | Δ EBIT ($bn) | FCFF ($bn) | Δ FCFF ($bn) | Value/share ($) | Δ Value/share ($) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Initial base | VALID | 502.818 | +0.000 | 385.972 | +0.000 | 209.28 | +0.00 |
| Revenue growth: lower | VALID | 408.456 | -94.362 | 319.635 | -66.336 | 174.41 | -34.87 |
| Revenue growth: base | VALID | 502.818 | +0.000 | 385.972 | +0.000 | 209.28 | +0.00 |
| Revenue growth: higher | VALID | 613.821 | +111.003 | 462.814 | +76.842 | 249.97 | +40.69 |
| EBIT margin: lower | VALID | 459.472 | -43.346 | 349.994 | -35.977 | 190.42 | -18.86 |
| EBIT margin: base | VALID | 502.818 | +0.000 | 385.972 | +0.000 | 209.28 | +0.00 |
| EBIT margin: higher | VALID | 546.164 | +43.346 | 421.949 | +35.977 | 228.13 | +18.86 |
| Restored base | VALID | 502.818 | +0.000 | 385.972 | +0.000 | 209.28 | +0.00 |

## Output spans

Maximum minus minimum across valid lower/base/higher results for that driver; unavailable valuation results are excluded from value/share spans.

| Driver | EBIT span ($bn) | FCFF span ($bn) | Value/share span ($) | Valid counts: EBIT / FCFF / value |
| --- | ---: | ---: | ---: | --- |
| Revenue growth | 205.365 | 143.178 | 75.56 | 3 / 3 / 3 |
| EBIT margin | 86.693 | 71.955 | 37.71 | 3 / 3 / 3 |

## Base restoration

Final run: **Restored base**. Exact input, statement, and valuation agreement with the initial base: **PASS**.

## Statement and check audit trail

All five years are retained below for every run. All statement fields are USD billions, including the signed FCFF fields. Field names match the existing model: `ebit` = operating profit; `ni` = net income; `da` = depreciation and amortization; `delta_nwc` = investment in operating working capital; `cfo/cfi/cff` = operating/investing/financing cash flow; `fcff` = economic free cash flow to the firm. Expense fields such as `sga`, `rd`, `tax`, and `capex` are positive deductions in their respective formulas.

Check amounts are USD billions. Reconciliation tolerance: 0.00000001. Nonnegative checks show balances, not reconciliation gaps. Full inputs, statements, checks, and valuation bridges are also saved in `nvidia_sensitivity_results.json`.

### Initial base

Changed independent inputs: none.

| Statement field ($bn) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| cash | 195.235 | 427.091 | 707.807 | 1,033.609 | 1,394.188 |
| securities | 76.926 | 76.926 | 76.926 | 76.926 | 76.926 |
| ar | 93.750 | 123.419 | 149.131 | 172.272 | 190.014 |
| inventory | 46.943 | 61.798 | 74.673 | 86.260 | 95.144 |
| prepaid | 5.068 | 6.672 | 8.062 | 9.313 | 10.272 |
| ppe | 22.983 | 34.291 | 47.806 | 61.992 | 77.597 |
| intangibles | 2.207 | 1.179 | 0.000 | 0.000 | 0.000 |
| other_assets | 105.577 | 105.577 | 105.577 | 105.577 | 105.577 |
| ap | 22.388 | 29.473 | 35.614 | 41.140 | 45.377 |
| accrued | 40.082 | 52.766 | 63.759 | 73.653 | 81.238 |
| debt | 33.366 | 33.366 | 33.366 | 33.366 | 33.366 |
| other_liabilities | 15.903 | 15.903 | 15.903 | 15.903 | 15.903 |
| equity | 436.951 | 705.445 | 1,021.341 | 1,381.889 | 1,773.835 |
| revenue | 439.306 | 571.098 | 685.318 | 788.116 | 866.927 |
| opening_cash | 22.443 | 195.235 | 427.091 | 707.807 | 1,033.609 |
| opening_equity | 228.984 | 436.951 | 705.445 | 1,021.341 | 1,381.889 |
| gross | 325.087 | 416.902 | 493.429 | 559.562 | 606.849 |
| cogs | 114.220 | 154.197 | 191.889 | 228.554 | 260.078 |
| sga | 9.753 | 12.507 | 14.803 | 16.787 | 18.205 |
| ebit | 281.156 | 354.081 | 411.191 | 464.988 | 502.818 |
| rd | 34.178 | 50.314 | 67.435 | 77.787 | 85.826 |
| da | 5.272 | 6.853 | 8.224 | 9.457 | 10.403 |
| amortization | 0.791 | 1.028 | 1.179 | 0.000 | 0.000 |
| depreciation | 4.481 | 5.825 | 7.045 | 9.457 | 10.403 |
| interest | 1.335 | 1.335 | 1.335 | 1.335 | 1.335 |
| pretax | 279.822 | 352.746 | 409.856 | 463.654 | 501.483 |
| tax | 47.570 | 59.967 | 69.676 | 78.821 | 85.252 |
| ni | 232.252 | 292.780 | 340.181 | 384.833 | 416.231 |
| capex | 13.179 | 17.133 | 20.560 | 23.643 | 26.008 |
| delta_nwc | 27.267 | 26.358 | 22.844 | 20.560 | 15.762 |
| sbc | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| buybacks | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| dividends | 24.285 | 24.285 | 24.285 | 24.285 | 24.285 |
| net_borrowing | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cfo | 219.921 | 285.838 | 340.638 | 391.069 | 429.944 |
| cfi | -13.179 | -17.133 | -20.560 | -23.643 | -26.008 |
| cff | -33.950 | -36.849 | -39.362 | -41.624 | -43.357 |
| cash_change | 172.792 | 231.856 | 280.716 | 325.802 | 360.579 |
| assets | 548.690 | 836.954 | 1,169.983 | 1,545.950 | 1,949.718 |
| liabilities | 111.739 | 131.508 | 148.642 | 164.062 | 175.884 |
| balance_gap | -0.000 | -0.000 | -0.000 | -0.000 | 0.000 |
| cash_fcfe | 206.742 | 268.706 | 320.078 | 367.426 | 403.937 |
| fcfe | 197.077 | 256.141 | 305.001 | 350.087 | 384.864 |
| fcff | 198.185 | 257.249 | 306.109 | 351.195 | 385.972 |

| Year | Check | Amount ($bn) | Status |
| --- | --- | ---: | --- |
| 0 | Opening balance sheet gap | -0.000000000000 | PASS |
| 1 | Balance sheet gap | -0.000000000000 | PASS |
| 1 | Cash reconciliation gap | -0.000000000000 | PASS |
| 1 | Equity rollforward gap | -0.000000000000 | PASS |
| 1 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 1 | Working capital gap | -0.000000000000 | PASS |
| 1 | Income statement gap | 0.000000000000 | PASS |
| 1 | FCFF formula gap | 0.000000000000 | PASS |
| 1 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 1 | cash nonnegative | 195.235044600000 | PASS |
| 1 | ppe nonnegative | 22.983268700000 | PASS |
| 1 | intangibles nonnegative | 2.207248300000 | PASS |
| 1 | rd nonnegative | 34.178045700000 | PASS |
| 2 | Balance sheet gap | -0.000000000000 | PASS |
| 2 | Cash reconciliation gap | 0.000000000000 | PASS |
| 2 | Equity rollforward gap | 0.000000000000 | PASS |
| 2 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 2 | Working capital gap | 0.000000000000 | PASS |
| 2 | Income statement gap | 0.000000000000 | PASS |
| 2 | FCFF formula gap | 0.000000000000 | PASS |
| 2 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 2 | cash nonnegative | 427.091393670000 | PASS |
| 2 | ppe nonnegative | 34.291018010000 | PASS |
| 2 | intangibles nonnegative | 1.179271090000 | PASS |
| 2 | rd nonnegative | 50.313773445000 | PASS |
| 3 | Balance sheet gap | -0.000000000000 | PASS |
| 3 | Cash reconciliation gap | -0.000000000000 | PASS |
| 3 | Equity rollforward gap | 0.000000000000 | PASS |
| 3 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 3 | Working capital gap | 0.000000000000 | PASS |
| 3 | Income statement gap | 0.000000000000 | PASS |
| 3 | FCFF formula gap | 0.000000000000 | PASS |
| 3 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 3 | cash nonnegative | 707.807411670000 | PASS |
| 3 | ppe nonnegative | 47.806015620000 | PASS |
| 3 | intangibles nonnegative | 0.000000000000 | PASS |
| 3 | rd nonnegative | 67.435304976000 | PASS |
| 4 | Balance sheet gap | -0.000000000000 | PASS |
| 4 | Cash reconciliation gap | -0.000000000000 | PASS |
| 4 | Equity rollforward gap | 0.000000000000 | PASS |
| 4 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 4 | Working capital gap | -0.000000000000 | PASS |
| 4 | Income statement gap | 0.000000000000 | PASS |
| 4 | FCFF formula gap | 0.000000000000 | PASS |
| 4 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 4 | cash nonnegative | 1033.609367903700 | PASS |
| 4 | ppe nonnegative | 61.992101118000 | PASS |
| 4 | intangibles nonnegative | 0.000000000000 | PASS |
| 4 | rd nonnegative | 77.787035480700 | PASS |
| 5 | Balance sheet gap | 0.000000000000 | PASS |
| 5 | Cash reconciliation gap | 0.000000000000 | PASS |
| 5 | Equity rollforward gap | -0.000000000000 | PASS |
| 5 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 5 | Working capital gap | -0.000000000000 | PASS |
| 5 | Income statement gap | 0.000000000000 | PASS |
| 5 | FCFF formula gap | 0.000000000000 | PASS |
| 5 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 5 | cash nonnegative | 1394.188478469840 | PASS |
| 5 | ppe nonnegative | 77.596795165800 | PASS |
| 5 | intangibles nonnegative | 0.000000000000 | PASS |
| 5 | rd nonnegative | 85.825817262900 | PASS |

Valuation bridge: explicit=1102.283477; terminal_fcff=409.726383; terminal=6303.482817; pv_terminal=3913.966891; ev=5016.250368; bridge=66.003000; equity=5082.253368; per_share=209.275411; terminal_share=0.780257. Amounts are USD billions except per_share (USD/share) and terminal_share (fraction).

### Revenue growth: lower

Changed independent inputs: GROWTH.

| Statement field ($bn) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| cash | 190.491 | 407.186 | 658.556 | 937.338 | 1,231.581 |
| securities | 76.926 | 76.926 | 76.926 | 76.926 | 76.926 |
| ar | 90.340 | 114.211 | 132.114 | 145.840 | 153.389 |
| inventory | 45.235 | 57.188 | 66.153 | 73.025 | 76.805 |
| prepaid | 4.884 | 6.174 | 7.142 | 7.884 | 8.292 |
| ppe | 22.683 | 33.181 | 45.254 | 57.509 | 70.185 |
| intangibles | 2.235 | 1.280 | 0.183 | 0.000 | 0.000 |
| other_assets | 105.577 | 105.577 | 105.577 | 105.577 | 105.577 |
| ap | 21.574 | 27.275 | 31.550 | 34.828 | 36.631 |
| accrued | 38.624 | 48.829 | 56.484 | 62.352 | 65.580 |
| debt | 33.366 | 33.366 | 33.366 | 33.366 | 33.366 |
| other_liabilities | 15.903 | 15.903 | 15.903 | 15.903 | 15.903 |
| equity | 428.904 | 676.351 | 954.602 | 1,257.651 | 1,571.277 |
| revenue | 424.158 | 530.197 | 609.727 | 670.700 | 704.235 |
| opening_cash | 22.443 | 190.491 | 407.186 | 658.556 | 937.338 |
| opening_equity | 228.984 | 428.904 | 676.351 | 954.602 | 1,257.651 |
| gross | 313.877 | 387.044 | 439.004 | 476.197 | 492.964 |
| cogs | 110.281 | 143.153 | 170.724 | 194.503 | 211.270 |
| sga | 9.416 | 11.611 | 13.170 | 14.286 | 14.789 |
| ebit | 271.461 | 328.722 | 365.836 | 395.713 | 408.456 |
| rd | 32.999 | 46.710 | 59.997 | 66.198 | 69.719 |
| da | 5.090 | 6.362 | 7.317 | 8.048 | 8.451 |
| amortization | 0.763 | 0.954 | 1.098 | 0.183 | 0.000 |
| depreciation | 4.326 | 5.408 | 6.219 | 7.866 | 8.451 |
| interest | 1.335 | 1.335 | 1.335 | 1.335 | 1.335 |
| pretax | 270.126 | 327.388 | 364.502 | 394.378 | 407.122 |
| tax | 45.922 | 55.656 | 61.965 | 67.044 | 69.211 |
| ni | 224.205 | 271.732 | 302.536 | 327.334 | 337.911 |
| capex | 12.725 | 15.906 | 18.292 | 20.121 | 21.127 |
| delta_nwc | 24.238 | 21.208 | 15.906 | 12.195 | 6.707 |
| sbc | 9.331 | 11.664 | 13.414 | 14.755 | 15.493 |
| buybacks | 9.331 | 11.664 | 13.414 | 14.755 | 15.493 |
| dividends | 24.285 | 24.285 | 24.285 | 24.285 | 24.285 |
| net_borrowing | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cfo | 214.389 | 268.551 | 307.361 | 337.943 | 355.148 |
| cfi | -12.725 | -15.906 | -18.292 | -20.121 | -21.127 |
| cff | -33.616 | -35.949 | -37.699 | -39.040 | -39.778 |
| cash_change | 168.048 | 216.695 | 251.370 | 278.782 | 294.243 |
| assets | 538.371 | 801.724 | 1,091.905 | 1,404.100 | 1,722.756 |
| liabilities | 109.467 | 125.373 | 137.303 | 146.449 | 151.479 |
| balance_gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cash_fcfe | 201.664 | 252.645 | 289.069 | 317.822 | 334.021 |
| fcfe | 192.333 | 240.980 | 275.655 | 303.067 | 318.528 |
| fcff | 193.440 | 242.088 | 276.763 | 304.175 | 319.635 |

| Year | Check | Amount ($bn) | Status |
| --- | --- | ---: | --- |
| 0 | Opening balance sheet gap | -0.000000000000 | PASS |
| 1 | Balance sheet gap | 0.000000000000 | PASS |
| 1 | Cash reconciliation gap | -0.000000000000 | PASS |
| 1 | Equity rollforward gap | -0.000000000000 | PASS |
| 1 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 1 | Working capital gap | 0.000000000000 | PASS |
| 1 | Income statement gap | 0.000000000000 | PASS |
| 1 | FCFF formula gap | 0.000000000000 | PASS |
| 1 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 1 | cash nonnegative | 190.490534400000 | PASS |
| 1 | ppe nonnegative | 22.683328400000 | PASS |
| 1 | intangibles nonnegative | 2.234515600000 | PASS |
| 1 | rd nonnegative | 32.999492400000 | PASS |
| 2 | Balance sheet gap | 0.000000000000 | PASS |
| 2 | Cash reconciliation gap | 0.000000000000 | PASS |
| 2 | Equity rollforward gap | 0.000000000000 | PASS |
| 2 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 2 | Working capital gap | 0.000000000000 | PASS |
| 2 | Income statement gap | 0.000000000000 | PASS |
| 2 | FCFF formula gap | 0.000000000000 | PASS |
| 2 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 2 | cash nonnegative | 407.185961700000 | PASS |
| 2 | ppe nonnegative | 33.181238900000 | PASS |
| 2 | intangibles nonnegative | 1.280160100000 | PASS |
| 2 | rd nonnegative | 46.710399750000 | PASS |
| 3 | Balance sheet gap | 0.000000000000 | PASS |
| 3 | Cash reconciliation gap | -0.000000000000 | PASS |
| 3 | Equity rollforward gap | 0.000000000000 | PASS |
| 3 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 3 | Working capital gap | 0.000000000000 | PASS |
| 3 | Income statement gap | 0.000000000000 | PASS |
| 3 | FCFF formula gap | 0.000000000000 | PASS |
| 3 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 3 | cash nonnegative | 658.556305500000 | PASS |
| 3 | ppe nonnegative | 45.253835975000 | PASS |
| 3 | intangibles nonnegative | 0.182651275000 | PASS |
| 3 | rd nonnegative | 59.997149100000 | PASS |
| 4 | Balance sheet gap | 0.000000000000 | PASS |
| 4 | Cash reconciliation gap | 0.000000000000 | PASS |
| 4 | Equity rollforward gap | -0.000000000000 | PASS |
| 4 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 4 | Working capital gap | 0.000000000000 | PASS |
| 4 | Income statement gap | 0.000000000000 | PASS |
| 4 | FCFF formula gap | 0.000000000000 | PASS |
| 4 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 4 | cash nonnegative | 937.338125148750 | PASS |
| 4 | ppe nonnegative | 57.509084325000 | PASS |
| 4 | intangibles nonnegative | 0.000000000000 | PASS |
| 4 | rd nonnegative | 66.198073961250 | PASS |
| 5 | Balance sheet gap | 0.000000000000 | PASS |
| 5 | Cash reconciliation gap | 0.000000000000 | PASS |
| 5 | Equity rollforward gap | -0.000000000000 | PASS |
| 5 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 5 | Working capital gap | 0.000000000000 | PASS |
| 5 | Income statement gap | 0.000000000000 | PASS |
| 5 | FCFF formula gap | 0.000000000000 | PASS |
| 5 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 5 | cash nonnegative | 1231.580795506125 | PASS |
| 5 | ppe nonnegative | 70.185311253750 | PASS |
| 5 | intangibles nonnegative | 0.000000000000 | PASS |
| 5 | rd nonnegative | 69.719248108125 | PASS |

Valuation bridge: explicit=990.087663; terminal_fcff=332.834761; terminal=5120.534782; pv_terminal=3179.449232; ev=4169.536895; bridge=66.003000; equity=4235.539895; per_share=174.409714; terminal_share=0.762543. Amounts are USD billions except per_share (USD/share) and terminal_share (fraction).

### Revenue growth: base

Changed independent inputs: none.

| Statement field ($bn) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| cash | 195.235 | 427.091 | 707.807 | 1,033.609 | 1,394.188 |
| securities | 76.926 | 76.926 | 76.926 | 76.926 | 76.926 |
| ar | 93.750 | 123.419 | 149.131 | 172.272 | 190.014 |
| inventory | 46.943 | 61.798 | 74.673 | 86.260 | 95.144 |
| prepaid | 5.068 | 6.672 | 8.062 | 9.313 | 10.272 |
| ppe | 22.983 | 34.291 | 47.806 | 61.992 | 77.597 |
| intangibles | 2.207 | 1.179 | 0.000 | 0.000 | 0.000 |
| other_assets | 105.577 | 105.577 | 105.577 | 105.577 | 105.577 |
| ap | 22.388 | 29.473 | 35.614 | 41.140 | 45.377 |
| accrued | 40.082 | 52.766 | 63.759 | 73.653 | 81.238 |
| debt | 33.366 | 33.366 | 33.366 | 33.366 | 33.366 |
| other_liabilities | 15.903 | 15.903 | 15.903 | 15.903 | 15.903 |
| equity | 436.951 | 705.445 | 1,021.341 | 1,381.889 | 1,773.835 |
| revenue | 439.306 | 571.098 | 685.318 | 788.116 | 866.927 |
| opening_cash | 22.443 | 195.235 | 427.091 | 707.807 | 1,033.609 |
| opening_equity | 228.984 | 436.951 | 705.445 | 1,021.341 | 1,381.889 |
| gross | 325.087 | 416.902 | 493.429 | 559.562 | 606.849 |
| cogs | 114.220 | 154.197 | 191.889 | 228.554 | 260.078 |
| sga | 9.753 | 12.507 | 14.803 | 16.787 | 18.205 |
| ebit | 281.156 | 354.081 | 411.191 | 464.988 | 502.818 |
| rd | 34.178 | 50.314 | 67.435 | 77.787 | 85.826 |
| da | 5.272 | 6.853 | 8.224 | 9.457 | 10.403 |
| amortization | 0.791 | 1.028 | 1.179 | 0.000 | 0.000 |
| depreciation | 4.481 | 5.825 | 7.045 | 9.457 | 10.403 |
| interest | 1.335 | 1.335 | 1.335 | 1.335 | 1.335 |
| pretax | 279.822 | 352.746 | 409.856 | 463.654 | 501.483 |
| tax | 47.570 | 59.967 | 69.676 | 78.821 | 85.252 |
| ni | 232.252 | 292.780 | 340.181 | 384.833 | 416.231 |
| capex | 13.179 | 17.133 | 20.560 | 23.643 | 26.008 |
| delta_nwc | 27.267 | 26.358 | 22.844 | 20.560 | 15.762 |
| sbc | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| buybacks | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| dividends | 24.285 | 24.285 | 24.285 | 24.285 | 24.285 |
| net_borrowing | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cfo | 219.921 | 285.838 | 340.638 | 391.069 | 429.944 |
| cfi | -13.179 | -17.133 | -20.560 | -23.643 | -26.008 |
| cff | -33.950 | -36.849 | -39.362 | -41.624 | -43.357 |
| cash_change | 172.792 | 231.856 | 280.716 | 325.802 | 360.579 |
| assets | 548.690 | 836.954 | 1,169.983 | 1,545.950 | 1,949.718 |
| liabilities | 111.739 | 131.508 | 148.642 | 164.062 | 175.884 |
| balance_gap | -0.000 | -0.000 | -0.000 | -0.000 | 0.000 |
| cash_fcfe | 206.742 | 268.706 | 320.078 | 367.426 | 403.937 |
| fcfe | 197.077 | 256.141 | 305.001 | 350.087 | 384.864 |
| fcff | 198.185 | 257.249 | 306.109 | 351.195 | 385.972 |

| Year | Check | Amount ($bn) | Status |
| --- | --- | ---: | --- |
| 0 | Opening balance sheet gap | -0.000000000000 | PASS |
| 1 | Balance sheet gap | -0.000000000000 | PASS |
| 1 | Cash reconciliation gap | -0.000000000000 | PASS |
| 1 | Equity rollforward gap | -0.000000000000 | PASS |
| 1 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 1 | Working capital gap | -0.000000000000 | PASS |
| 1 | Income statement gap | 0.000000000000 | PASS |
| 1 | FCFF formula gap | 0.000000000000 | PASS |
| 1 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 1 | cash nonnegative | 195.235044600000 | PASS |
| 1 | ppe nonnegative | 22.983268700000 | PASS |
| 1 | intangibles nonnegative | 2.207248300000 | PASS |
| 1 | rd nonnegative | 34.178045700000 | PASS |
| 2 | Balance sheet gap | -0.000000000000 | PASS |
| 2 | Cash reconciliation gap | 0.000000000000 | PASS |
| 2 | Equity rollforward gap | 0.000000000000 | PASS |
| 2 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 2 | Working capital gap | 0.000000000000 | PASS |
| 2 | Income statement gap | 0.000000000000 | PASS |
| 2 | FCFF formula gap | 0.000000000000 | PASS |
| 2 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 2 | cash nonnegative | 427.091393670000 | PASS |
| 2 | ppe nonnegative | 34.291018010000 | PASS |
| 2 | intangibles nonnegative | 1.179271090000 | PASS |
| 2 | rd nonnegative | 50.313773445000 | PASS |
| 3 | Balance sheet gap | -0.000000000000 | PASS |
| 3 | Cash reconciliation gap | -0.000000000000 | PASS |
| 3 | Equity rollforward gap | 0.000000000000 | PASS |
| 3 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 3 | Working capital gap | 0.000000000000 | PASS |
| 3 | Income statement gap | 0.000000000000 | PASS |
| 3 | FCFF formula gap | 0.000000000000 | PASS |
| 3 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 3 | cash nonnegative | 707.807411670000 | PASS |
| 3 | ppe nonnegative | 47.806015620000 | PASS |
| 3 | intangibles nonnegative | 0.000000000000 | PASS |
| 3 | rd nonnegative | 67.435304976000 | PASS |
| 4 | Balance sheet gap | -0.000000000000 | PASS |
| 4 | Cash reconciliation gap | -0.000000000000 | PASS |
| 4 | Equity rollforward gap | 0.000000000000 | PASS |
| 4 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 4 | Working capital gap | -0.000000000000 | PASS |
| 4 | Income statement gap | 0.000000000000 | PASS |
| 4 | FCFF formula gap | 0.000000000000 | PASS |
| 4 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 4 | cash nonnegative | 1033.609367903700 | PASS |
| 4 | ppe nonnegative | 61.992101118000 | PASS |
| 4 | intangibles nonnegative | 0.000000000000 | PASS |
| 4 | rd nonnegative | 77.787035480700 | PASS |
| 5 | Balance sheet gap | 0.000000000000 | PASS |
| 5 | Cash reconciliation gap | 0.000000000000 | PASS |
| 5 | Equity rollforward gap | -0.000000000000 | PASS |
| 5 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 5 | Working capital gap | -0.000000000000 | PASS |
| 5 | Income statement gap | 0.000000000000 | PASS |
| 5 | FCFF formula gap | 0.000000000000 | PASS |
| 5 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 5 | cash nonnegative | 1394.188478469840 | PASS |
| 5 | ppe nonnegative | 77.596795165800 | PASS |
| 5 | intangibles nonnegative | 0.000000000000 | PASS |
| 5 | rd nonnegative | 85.825817262900 | PASS |

Valuation bridge: explicit=1102.283477; terminal_fcff=409.726383; terminal=6303.482817; pv_terminal=3913.966891; ev=5016.250368; bridge=66.003000; equity=5082.253368; per_share=209.275411; terminal_share=0.780257. Amounts are USD billions except per_share (USD/share) and terminal_share (fraction).

### Revenue growth: higher

Changed independent inputs: GROWTH.

| Statement field ($bn) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| cash | 199.980 | 447.446 | 759.486 | 1,137.510 | 1,574.931 |
| securities | 76.926 | 76.926 | 76.926 | 76.926 | 76.926 |
| ar | 97.160 | 132.967 | 167.495 | 202.022 | 233.097 |
| inventory | 48.650 | 66.579 | 83.868 | 101.157 | 116.717 |
| prepaid | 5.253 | 7.188 | 9.055 | 10.921 | 12.601 |
| ppe | 23.283 | 35.431 | 50.311 | 66.875 | 85.925 |
| intangibles | 2.180 | 1.076 | 0.000 | 0.000 | 0.000 |
| other_assets | 105.577 | 105.577 | 105.577 | 105.577 | 105.577 |
| ap | 23.203 | 31.754 | 39.999 | 48.245 | 55.666 |
| accrued | 41.540 | 56.848 | 71.610 | 86.372 | 99.657 |
| debt | 33.366 | 33.366 | 33.366 | 33.366 | 33.366 |
| other_liabilities | 15.903 | 15.903 | 15.903 | 15.903 | 15.903 |
| equity | 444.998 | 735.319 | 1,091.839 | 1,517.103 | 2,001.182 |
| revenue | 454.455 | 613.514 | 766.893 | 920.271 | 1,058.312 |
| opening_cash | 22.443 | 199.980 | 447.446 | 759.486 | 1,137.510 |
| opening_equity | 228.984 | 444.998 | 735.319 | 1,091.839 | 1,517.103 |
| gross | 336.297 | 447.865 | 552.163 | 653.393 | 740.818 |
| cogs | 118.158 | 165.649 | 214.730 | 266.879 | 317.494 |
| sga | 10.089 | 13.436 | 16.565 | 19.602 | 22.225 |
| ebit | 290.851 | 380.379 | 460.136 | 542.960 | 613.821 |
| rd | 35.357 | 54.051 | 75.462 | 90.831 | 104.773 |
| da | 5.453 | 7.362 | 9.203 | 11.043 | 12.700 |
| amortization | 0.818 | 1.104 | 1.076 | 0.000 | 0.000 |
| depreciation | 4.635 | 6.258 | 8.127 | 11.043 | 12.700 |
| interest | 1.335 | 1.335 | 1.335 | 1.335 | 1.335 |
| pretax | 289.517 | 379.044 | 458.801 | 541.625 | 612.486 |
| tax | 49.218 | 64.438 | 77.996 | 92.076 | 104.123 |
| ni | 240.299 | 314.607 | 380.805 | 449.549 | 508.364 |
| capex | 13.634 | 18.405 | 23.007 | 27.608 | 31.749 |
| delta_nwc | 30.297 | 31.812 | 30.676 | 30.676 | 27.608 |
| sbc | 9.998 | 13.497 | 16.872 | 20.246 | 23.283 |
| buybacks | 9.998 | 13.497 | 16.872 | 20.246 | 23.283 |
| dividends | 24.285 | 24.285 | 24.285 | 24.285 | 24.285 |
| net_borrowing | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cfo | 225.453 | 303.654 | 376.204 | 450.163 | 516.738 |
| cfi | -13.634 | -18.405 | -23.007 | -27.608 | -31.749 |
| cff | -34.283 | -37.782 | -41.157 | -44.531 | -47.568 |
| cash_change | 177.537 | 247.467 | 312.040 | 378.024 | 437.421 |
| assets | 559.009 | 873.190 | 1,252.717 | 1,700.989 | 2,205.774 |
| liabilities | 114.011 | 137.871 | 160.878 | 183.885 | 204.592 |
| balance_gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cash_fcfe | 211.820 | 285.249 | 353.197 | 422.555 | 484.989 |
| fcfe | 201.822 | 271.752 | 336.325 | 402.309 | 461.706 |
| fcff | 202.929 | 272.859 | 337.433 | 403.416 | 462.814 |

| Year | Check | Amount ($bn) | Status |
| --- | --- | ---: | --- |
| 0 | Opening balance sheet gap | -0.000000000000 | PASS |
| 1 | Balance sheet gap | 0.000000000000 | PASS |
| 1 | Cash reconciliation gap | 0.000000000000 | PASS |
| 1 | Equity rollforward gap | -0.000000000000 | PASS |
| 1 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 1 | Working capital gap | 0.000000000000 | PASS |
| 1 | Income statement gap | 0.000000000000 | PASS |
| 1 | FCFF formula gap | 0.000000000000 | PASS |
| 1 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 1 | cash nonnegative | 199.979554800000 | PASS |
| 1 | ppe nonnegative | 23.283209000000 | PASS |
| 1 | intangibles nonnegative | 2.179981000000 | PASS |
| 1 | rd nonnegative | 35.356599000000 | PASS |
| 2 | Balance sheet gap | 0.000000000000 | PASS |
| 2 | Cash reconciliation gap | 0.000000000000 | PASS |
| 2 | Equity rollforward gap | 0.000000000000 | PASS |
| 2 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 2 | Working capital gap | 0.000000000000 | PASS |
| 2 | Income statement gap | 0.000000000000 | PASS |
| 2 | FCFF formula gap | 0.000000000000 | PASS |
| 2 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 2 | cash nonnegative | 447.446130150000 | PASS |
| 2 | ppe nonnegative | 35.430791150000 | PASS |
| 2 | intangibles nonnegative | 1.075655350000 | PASS |
| 2 | rd nonnegative | 54.050605425000 | PASS |
| 3 | Balance sheet gap | 0.000000000000 | PASS |
| 3 | Cash reconciliation gap | 0.000000000000 | PASS |
| 3 | Equity rollforward gap | 0.000000000000 | PASS |
| 3 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 3 | Working capital gap | 0.000000000000 | PASS |
| 3 | Income statement gap | 0.000000000000 | PASS |
| 3 | FCFF formula gap | 0.000000000000 | PASS |
| 3 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 3 | cash nonnegative | 759.486216450000 | PASS |
| 3 | ppe nonnegative | 50.310517125000 | PASS |
| 3 | intangibles nonnegative | 0.000000000000 | PASS |
| 3 | rd nonnegative | 75.462252750000 | PASS |
| 4 | Balance sheet gap | 0.000000000000 | PASS |
| 4 | Cash reconciliation gap | 0.000000000000 | PASS |
| 4 | Equity rollforward gap | -0.000000000000 | PASS |
| 4 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 4 | Working capital gap | -0.000000000000 | PASS |
| 4 | Income statement gap | 0.000000000000 | PASS |
| 4 | FCFF formula gap | 0.000000000000 | PASS |
| 4 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 4 | cash nonnegative | 1137.509760337500 | PASS |
| 4 | ppe nonnegative | 66.875401875000 | PASS |
| 4 | intangibles nonnegative | 0.000000000000 | PASS |
| 4 | rd nonnegative | 90.830784712500 | PASS |
| 5 | Balance sheet gap | 0.000000000000 | PASS |
| 5 | Cash reconciliation gap | -0.000000000000 | PASS |
| 5 | Equity rollforward gap | 0.000000000000 | PASS |
| 5 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 5 | Working capital gap | -0.000000000000 | PASS |
| 5 | Income statement gap | 0.000000000000 | PASS |
| 5 | FCFF formula gap | 0.000000000000 | PASS |
| 5 | FCFE to FCFF bridge gap | -0.000000000000 | PASS |
| 5 | cash nonnegative | 1574.930686338750 | PASS |
| 5 | ppe nonnegative | 85.925019337500 | PASS |
| 5 | intangibles nonnegative | 0.000000000000 | PASS |
| 5 | rd nonnegative | 104.772896043750 | PASS |

Valuation bridge: explicit=1226.412686; terminal_fcff=500.178398; terminal=7695.052270; pv_terminal=4778.022036; ev=6004.434723; bridge=66.003000; equity=6070.437723; per_share=249.966552; terminal_share=0.795749. Amounts are USD billions except per_share (USD/share) and terminal_share (fraction).

### EBIT margin: lower

Changed independent inputs: MARGINS.

| Statement field ($bn) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| cash | 177.004 | 385.160 | 637.435 | 930.530 | 1,255.132 |
| securities | 76.926 | 76.926 | 76.926 | 76.926 | 76.926 |
| ar | 93.750 | 123.419 | 149.131 | 172.272 | 190.014 |
| inventory | 46.943 | 61.798 | 74.673 | 86.260 | 95.144 |
| prepaid | 5.068 | 6.672 | 8.062 | 9.313 | 10.272 |
| ppe | 22.983 | 34.291 | 47.806 | 61.992 | 77.597 |
| intangibles | 2.207 | 1.179 | 0.000 | 0.000 | 0.000 |
| other_assets | 105.577 | 105.577 | 105.577 | 105.577 | 105.577 |
| ap | 22.388 | 29.473 | 35.614 | 41.140 | 45.377 |
| accrued | 40.082 | 52.766 | 63.759 | 73.653 | 81.238 |
| debt | 33.366 | 33.366 | 33.366 | 33.366 | 33.366 |
| other_liabilities | 15.903 | 15.903 | 15.903 | 15.903 | 15.903 |
| equity | 418.720 | 663.514 | 950.969 | 1,278.809 | 1,634.778 |
| revenue | 439.306 | 571.098 | 685.318 | 788.116 | 866.927 |
| opening_cash | 22.443 | 177.004 | 385.160 | 637.435 | 930.530 |
| opening_equity | 228.984 | 418.720 | 663.514 | 950.969 | 1,278.809 |
| gross | 325.087 | 416.902 | 493.429 | 559.562 | 606.849 |
| cogs | 114.220 | 154.197 | 191.889 | 228.554 | 260.078 |
| sga | 9.753 | 12.507 | 14.803 | 16.787 | 18.205 |
| ebit | 259.191 | 325.526 | 376.925 | 425.583 | 459.472 |
| rd | 56.143 | 78.869 | 101.701 | 117.193 | 129.172 |
| da | 5.272 | 6.853 | 8.224 | 9.457 | 10.403 |
| amortization | 0.791 | 1.028 | 1.179 | 0.000 | 0.000 |
| depreciation | 4.481 | 5.825 | 7.045 | 9.457 | 10.403 |
| interest | 1.335 | 1.335 | 1.335 | 1.335 | 1.335 |
| pretax | 257.856 | 324.191 | 375.590 | 424.248 | 458.137 |
| tax | 43.836 | 55.113 | 63.850 | 72.122 | 77.883 |
| ni | 214.021 | 269.079 | 311.740 | 352.126 | 380.254 |
| capex | 13.179 | 17.133 | 20.560 | 23.643 | 26.008 |
| delta_nwc | 27.267 | 26.358 | 22.844 | 20.560 | 15.762 |
| sbc | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| buybacks | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| dividends | 24.285 | 24.285 | 24.285 | 24.285 | 24.285 |
| net_borrowing | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cfo | 201.690 | 262.138 | 312.197 | 358.362 | 393.967 |
| cfi | -13.179 | -17.133 | -20.560 | -23.643 | -26.008 |
| cff | -33.950 | -36.849 | -39.362 | -41.624 | -43.357 |
| cash_change | 154.561 | 208.156 | 252.275 | 293.095 | 324.602 |
| assets | 530.459 | 795.022 | 1,099.610 | 1,442.871 | 1,810.662 |
| liabilities | 111.739 | 131.508 | 148.642 | 164.062 | 175.884 |
| balance_gap | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cash_fcfe | 188.511 | 245.005 | 291.637 | 334.719 | 367.959 |
| fcfe | 178.846 | 232.441 | 276.560 | 317.380 | 348.887 |
| fcff | 179.954 | 233.549 | 277.668 | 318.488 | 349.994 |

| Year | Check | Amount ($bn) | Status |
| --- | --- | ---: | --- |
| 0 | Opening balance sheet gap | -0.000000000000 | PASS |
| 1 | Balance sheet gap | 0.000000000000 | PASS |
| 1 | Cash reconciliation gap | 0.000000000000 | PASS |
| 1 | Equity rollforward gap | -0.000000000000 | PASS |
| 1 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 1 | Working capital gap | -0.000000000000 | PASS |
| 1 | Income statement gap | 0.000000000000 | PASS |
| 1 | FCFF formula gap | 0.000000000000 | PASS |
| 1 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 1 | cash nonnegative | 177.003824850000 | PASS |
| 1 | ppe nonnegative | 22.983268700000 | PASS |
| 1 | intangibles nonnegative | 2.207248300000 | PASS |
| 1 | rd nonnegative | 56.143370700000 | PASS |
| 2 | Balance sheet gap | 0.000000000000 | PASS |
| 2 | Cash reconciliation gap | 0.000000000000 | PASS |
| 2 | Equity rollforward gap | 0.000000000000 | PASS |
| 2 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 2 | Working capital gap | 0.000000000000 | PASS |
| 2 | Income statement gap | 0.000000000000 | PASS |
| 2 | FCFF formula gap | 0.000000000000 | PASS |
| 2 | FCFE to FCFF bridge gap | -0.000000000000 | PASS |
| 2 | cash nonnegative | 385.159588245000 | PASS |
| 2 | ppe nonnegative | 34.291018010000 | PASS |
| 2 | intangibles nonnegative | 1.179271090000 | PASS |
| 2 | rd nonnegative | 78.868695945000 | PASS |
| 3 | Balance sheet gap | 0.000000000000 | PASS |
| 3 | Cash reconciliation gap | 0.000000000000 | PASS |
| 3 | Equity rollforward gap | -0.000000000000 | PASS |
| 3 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 3 | Working capital gap | 0.000000000000 | PASS |
| 3 | Income statement gap | 0.000000000000 | PASS |
| 3 | FCFF formula gap | 0.000000000000 | PASS |
| 3 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 3 | cash nonnegative | 637.434903435000 | PASS |
| 3 | ppe nonnegative | 47.806015620000 | PASS |
| 3 | intangibles nonnegative | 0.000000000000 | PASS |
| 3 | rd nonnegative | 101.701211976000 | PASS |
| 4 | Balance sheet gap | 0.000000000000 | PASS |
| 4 | Cash reconciliation gap | -0.000000000000 | PASS |
| 4 | Equity rollforward gap | 0.000000000000 | PASS |
| 4 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 4 | Working capital gap | -0.000000000000 | PASS |
| 4 | Income statement gap | 0.000000000000 | PASS |
| 4 | FCFF formula gap | 0.000000000000 | PASS |
| 4 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 4 | cash nonnegative | 930.530051437200 | PASS |
| 4 | ppe nonnegative | 61.992101118000 | PASS |
| 4 | intangibles nonnegative | 0.000000000000 | PASS |
| 4 | rd nonnegative | 117.192828530700 | PASS |
| 5 | Balance sheet gap | 0.000000000000 | PASS |
| 5 | Cash reconciliation gap | -0.000000000000 | PASS |
| 5 | Equity rollforward gap | -0.000000000000 | PASS |
| 5 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 5 | Working capital gap | -0.000000000000 | PASS |
| 5 | Income statement gap | 0.000000000000 | PASS |
| 5 | FCFF formula gap | 0.000000000000 | PASS |
| 5 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 5 | cash nonnegative | 1255.131672948690 | PASS |
| 5 | ppe nonnegative | 77.596795165800 | PASS |
| 5 | intangibles nonnegative | 0.000000000000 | PASS |
| 5 | rd nonnegative | 129.172189617900 | PASS |

Valuation bridge: explicit=1000.076079; terminal_fcff=372.489682; terminal=5730.610492; pv_terminal=3558.258248; ev=4558.334327; bridge=66.003000; equity=4624.337327; per_share=190.419491; terminal_share=0.780605. Amounts are USD billions except per_share (USD/share) and terminal_share (fraction).

### EBIT margin: base

Changed independent inputs: none.

| Statement field ($bn) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| cash | 195.235 | 427.091 | 707.807 | 1,033.609 | 1,394.188 |
| securities | 76.926 | 76.926 | 76.926 | 76.926 | 76.926 |
| ar | 93.750 | 123.419 | 149.131 | 172.272 | 190.014 |
| inventory | 46.943 | 61.798 | 74.673 | 86.260 | 95.144 |
| prepaid | 5.068 | 6.672 | 8.062 | 9.313 | 10.272 |
| ppe | 22.983 | 34.291 | 47.806 | 61.992 | 77.597 |
| intangibles | 2.207 | 1.179 | 0.000 | 0.000 | 0.000 |
| other_assets | 105.577 | 105.577 | 105.577 | 105.577 | 105.577 |
| ap | 22.388 | 29.473 | 35.614 | 41.140 | 45.377 |
| accrued | 40.082 | 52.766 | 63.759 | 73.653 | 81.238 |
| debt | 33.366 | 33.366 | 33.366 | 33.366 | 33.366 |
| other_liabilities | 15.903 | 15.903 | 15.903 | 15.903 | 15.903 |
| equity | 436.951 | 705.445 | 1,021.341 | 1,381.889 | 1,773.835 |
| revenue | 439.306 | 571.098 | 685.318 | 788.116 | 866.927 |
| opening_cash | 22.443 | 195.235 | 427.091 | 707.807 | 1,033.609 |
| opening_equity | 228.984 | 436.951 | 705.445 | 1,021.341 | 1,381.889 |
| gross | 325.087 | 416.902 | 493.429 | 559.562 | 606.849 |
| cogs | 114.220 | 154.197 | 191.889 | 228.554 | 260.078 |
| sga | 9.753 | 12.507 | 14.803 | 16.787 | 18.205 |
| ebit | 281.156 | 354.081 | 411.191 | 464.988 | 502.818 |
| rd | 34.178 | 50.314 | 67.435 | 77.787 | 85.826 |
| da | 5.272 | 6.853 | 8.224 | 9.457 | 10.403 |
| amortization | 0.791 | 1.028 | 1.179 | 0.000 | 0.000 |
| depreciation | 4.481 | 5.825 | 7.045 | 9.457 | 10.403 |
| interest | 1.335 | 1.335 | 1.335 | 1.335 | 1.335 |
| pretax | 279.822 | 352.746 | 409.856 | 463.654 | 501.483 |
| tax | 47.570 | 59.967 | 69.676 | 78.821 | 85.252 |
| ni | 232.252 | 292.780 | 340.181 | 384.833 | 416.231 |
| capex | 13.179 | 17.133 | 20.560 | 23.643 | 26.008 |
| delta_nwc | 27.267 | 26.358 | 22.844 | 20.560 | 15.762 |
| sbc | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| buybacks | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| dividends | 24.285 | 24.285 | 24.285 | 24.285 | 24.285 |
| net_borrowing | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cfo | 219.921 | 285.838 | 340.638 | 391.069 | 429.944 |
| cfi | -13.179 | -17.133 | -20.560 | -23.643 | -26.008 |
| cff | -33.950 | -36.849 | -39.362 | -41.624 | -43.357 |
| cash_change | 172.792 | 231.856 | 280.716 | 325.802 | 360.579 |
| assets | 548.690 | 836.954 | 1,169.983 | 1,545.950 | 1,949.718 |
| liabilities | 111.739 | 131.508 | 148.642 | 164.062 | 175.884 |
| balance_gap | -0.000 | -0.000 | -0.000 | -0.000 | 0.000 |
| cash_fcfe | 206.742 | 268.706 | 320.078 | 367.426 | 403.937 |
| fcfe | 197.077 | 256.141 | 305.001 | 350.087 | 384.864 |
| fcff | 198.185 | 257.249 | 306.109 | 351.195 | 385.972 |

| Year | Check | Amount ($bn) | Status |
| --- | --- | ---: | --- |
| 0 | Opening balance sheet gap | -0.000000000000 | PASS |
| 1 | Balance sheet gap | -0.000000000000 | PASS |
| 1 | Cash reconciliation gap | -0.000000000000 | PASS |
| 1 | Equity rollforward gap | -0.000000000000 | PASS |
| 1 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 1 | Working capital gap | -0.000000000000 | PASS |
| 1 | Income statement gap | 0.000000000000 | PASS |
| 1 | FCFF formula gap | 0.000000000000 | PASS |
| 1 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 1 | cash nonnegative | 195.235044600000 | PASS |
| 1 | ppe nonnegative | 22.983268700000 | PASS |
| 1 | intangibles nonnegative | 2.207248300000 | PASS |
| 1 | rd nonnegative | 34.178045700000 | PASS |
| 2 | Balance sheet gap | -0.000000000000 | PASS |
| 2 | Cash reconciliation gap | 0.000000000000 | PASS |
| 2 | Equity rollforward gap | 0.000000000000 | PASS |
| 2 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 2 | Working capital gap | 0.000000000000 | PASS |
| 2 | Income statement gap | 0.000000000000 | PASS |
| 2 | FCFF formula gap | 0.000000000000 | PASS |
| 2 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 2 | cash nonnegative | 427.091393670000 | PASS |
| 2 | ppe nonnegative | 34.291018010000 | PASS |
| 2 | intangibles nonnegative | 1.179271090000 | PASS |
| 2 | rd nonnegative | 50.313773445000 | PASS |
| 3 | Balance sheet gap | -0.000000000000 | PASS |
| 3 | Cash reconciliation gap | -0.000000000000 | PASS |
| 3 | Equity rollforward gap | 0.000000000000 | PASS |
| 3 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 3 | Working capital gap | 0.000000000000 | PASS |
| 3 | Income statement gap | 0.000000000000 | PASS |
| 3 | FCFF formula gap | 0.000000000000 | PASS |
| 3 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 3 | cash nonnegative | 707.807411670000 | PASS |
| 3 | ppe nonnegative | 47.806015620000 | PASS |
| 3 | intangibles nonnegative | 0.000000000000 | PASS |
| 3 | rd nonnegative | 67.435304976000 | PASS |
| 4 | Balance sheet gap | -0.000000000000 | PASS |
| 4 | Cash reconciliation gap | -0.000000000000 | PASS |
| 4 | Equity rollforward gap | 0.000000000000 | PASS |
| 4 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 4 | Working capital gap | -0.000000000000 | PASS |
| 4 | Income statement gap | 0.000000000000 | PASS |
| 4 | FCFF formula gap | 0.000000000000 | PASS |
| 4 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 4 | cash nonnegative | 1033.609367903700 | PASS |
| 4 | ppe nonnegative | 61.992101118000 | PASS |
| 4 | intangibles nonnegative | 0.000000000000 | PASS |
| 4 | rd nonnegative | 77.787035480700 | PASS |
| 5 | Balance sheet gap | 0.000000000000 | PASS |
| 5 | Cash reconciliation gap | 0.000000000000 | PASS |
| 5 | Equity rollforward gap | -0.000000000000 | PASS |
| 5 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 5 | Working capital gap | -0.000000000000 | PASS |
| 5 | Income statement gap | 0.000000000000 | PASS |
| 5 | FCFF formula gap | 0.000000000000 | PASS |
| 5 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 5 | cash nonnegative | 1394.188478469840 | PASS |
| 5 | ppe nonnegative | 77.596795165800 | PASS |
| 5 | intangibles nonnegative | 0.000000000000 | PASS |
| 5 | rd nonnegative | 85.825817262900 | PASS |

Valuation bridge: explicit=1102.283477; terminal_fcff=409.726383; terminal=6303.482817; pv_terminal=3913.966891; ev=5016.250368; bridge=66.003000; equity=5082.253368; per_share=209.275411; terminal_share=0.780257. Amounts are USD billions except per_share (USD/share) and terminal_share (fraction).

### EBIT margin: higher

Changed independent inputs: MARGINS.

| Statement field ($bn) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| cash | 213.466 | 469.023 | 778.180 | 1,136.689 | 1,533.245 |
| securities | 76.926 | 76.926 | 76.926 | 76.926 | 76.926 |
| ar | 93.750 | 123.419 | 149.131 | 172.272 | 190.014 |
| inventory | 46.943 | 61.798 | 74.673 | 86.260 | 95.144 |
| prepaid | 5.068 | 6.672 | 8.062 | 9.313 | 10.272 |
| ppe | 22.983 | 34.291 | 47.806 | 61.992 | 77.597 |
| intangibles | 2.207 | 1.179 | 0.000 | 0.000 | 0.000 |
| other_assets | 105.577 | 105.577 | 105.577 | 105.577 | 105.577 |
| ap | 22.388 | 29.473 | 35.614 | 41.140 | 45.377 |
| accrued | 40.082 | 52.766 | 63.759 | 73.653 | 81.238 |
| debt | 33.366 | 33.366 | 33.366 | 33.366 | 33.366 |
| other_liabilities | 15.903 | 15.903 | 15.903 | 15.903 | 15.903 |
| equity | 455.182 | 747.377 | 1,091.714 | 1,484.968 | 1,912.892 |
| revenue | 439.306 | 571.098 | 685.318 | 788.116 | 866.927 |
| opening_cash | 22.443 | 213.466 | 469.023 | 778.180 | 1,136.689 |
| opening_equity | 228.984 | 455.182 | 747.377 | 1,091.714 | 1,484.968 |
| gross | 325.087 | 416.902 | 493.429 | 559.562 | 606.849 |
| cogs | 114.220 | 154.197 | 191.889 | 228.554 | 260.078 |
| sga | 9.753 | 12.507 | 14.803 | 16.787 | 18.205 |
| ebit | 303.121 | 382.636 | 445.457 | 504.394 | 546.164 |
| rd | 12.213 | 21.759 | 33.169 | 38.381 | 42.479 |
| da | 5.272 | 6.853 | 8.224 | 9.457 | 10.403 |
| amortization | 0.791 | 1.028 | 1.179 | 0.000 | 0.000 |
| depreciation | 4.481 | 5.825 | 7.045 | 9.457 | 10.403 |
| interest | 1.335 | 1.335 | 1.335 | 1.335 | 1.335 |
| pretax | 301.787 | 381.301 | 444.122 | 503.060 | 544.830 |
| tax | 51.304 | 64.821 | 75.501 | 85.520 | 92.621 |
| ni | 250.483 | 316.480 | 368.621 | 417.539 | 452.209 |
| capex | 13.179 | 17.133 | 20.560 | 23.643 | 26.008 |
| delta_nwc | 27.267 | 26.358 | 22.844 | 20.560 | 15.762 |
| sbc | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| buybacks | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| dividends | 24.285 | 24.285 | 24.285 | 24.285 | 24.285 |
| net_borrowing | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cfo | 238.152 | 309.539 | 369.078 | 423.776 | 465.922 |
| cfi | -13.179 | -17.133 | -20.560 | -23.643 | -26.008 |
| cff | -33.950 | -36.849 | -39.362 | -41.624 | -43.357 |
| cash_change | 191.023 | 255.557 | 309.157 | 358.509 | 396.557 |
| assets | 566.921 | 878.885 | 1,240.355 | 1,649.030 | 2,088.775 |
| liabilities | 111.739 | 131.508 | 148.642 | 164.062 | 175.884 |
| balance_gap | 0.000 | -0.000 | 0.000 | 0.000 | 0.000 |
| cash_fcfe | 224.973 | 292.406 | 348.519 | 400.132 | 439.914 |
| fcfe | 215.308 | 279.842 | 333.442 | 382.794 | 420.842 |
| fcff | 216.416 | 280.950 | 334.549 | 383.902 | 421.949 |

| Year | Check | Amount ($bn) | Status |
| --- | --- | ---: | --- |
| 0 | Opening balance sheet gap | -0.000000000000 | PASS |
| 1 | Balance sheet gap | 0.000000000000 | PASS |
| 1 | Cash reconciliation gap | 0.000000000000 | PASS |
| 1 | Equity rollforward gap | -0.000000000000 | PASS |
| 1 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 1 | Working capital gap | -0.000000000000 | PASS |
| 1 | Income statement gap | 0.000000000000 | PASS |
| 1 | FCFF formula gap | 0.000000000000 | PASS |
| 1 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 1 | cash nonnegative | 213.466264350000 | PASS |
| 1 | ppe nonnegative | 22.983268700000 | PASS |
| 1 | intangibles nonnegative | 2.207248300000 | PASS |
| 1 | rd nonnegative | 12.212720700000 | PASS |
| 2 | Balance sheet gap | -0.000000000000 | PASS |
| 2 | Cash reconciliation gap | -0.000000000000 | PASS |
| 2 | Equity rollforward gap | 0.000000000000 | PASS |
| 2 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 2 | Working capital gap | 0.000000000000 | PASS |
| 2 | Income statement gap | 0.000000000000 | PASS |
| 2 | FCFF formula gap | 0.000000000000 | PASS |
| 2 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 2 | cash nonnegative | 469.023199095000 | PASS |
| 2 | ppe nonnegative | 34.291018010000 | PASS |
| 2 | intangibles nonnegative | 1.179271090000 | PASS |
| 2 | rd nonnegative | 21.758850945000 | PASS |
| 3 | Balance sheet gap | 0.000000000000 | PASS |
| 3 | Cash reconciliation gap | 0.000000000000 | PASS |
| 3 | Equity rollforward gap | -0.000000000000 | PASS |
| 3 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 3 | Working capital gap | 0.000000000000 | PASS |
| 3 | Income statement gap | 0.000000000000 | PASS |
| 3 | FCFF formula gap | 0.000000000000 | PASS |
| 3 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 3 | cash nonnegative | 778.179919905000 | PASS |
| 3 | ppe nonnegative | 47.806015620000 | PASS |
| 3 | intangibles nonnegative | 0.000000000000 | PASS |
| 3 | rd nonnegative | 33.169397976000 | PASS |
| 4 | Balance sheet gap | 0.000000000000 | PASS |
| 4 | Cash reconciliation gap | -0.000000000000 | PASS |
| 4 | Equity rollforward gap | -0.000000000000 | PASS |
| 4 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 4 | Working capital gap | -0.000000000000 | PASS |
| 4 | Income statement gap | 0.000000000000 | PASS |
| 4 | FCFF formula gap | 0.000000000000 | PASS |
| 4 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 4 | cash nonnegative | 1136.688684370200 | PASS |
| 4 | ppe nonnegative | 61.992101118000 | PASS |
| 4 | intangibles nonnegative | 0.000000000000 | PASS |
| 4 | rd nonnegative | 38.381242430700 | PASS |
| 5 | Balance sheet gap | 0.000000000000 | PASS |
| 5 | Cash reconciliation gap | -0.000000000000 | PASS |
| 5 | Equity rollforward gap | -0.000000000000 | PASS |
| 5 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 5 | Working capital gap | -0.000000000000 | PASS |
| 5 | Income statement gap | 0.000000000000 | PASS |
| 5 | FCFF formula gap | 0.000000000000 | PASS |
| 5 | FCFE to FCFF bridge gap | -0.000000000000 | PASS |
| 5 | cash nonnegative | 1533.245283990990 | PASS |
| 5 | ppe nonnegative | 77.596795165800 | PASS |
| 5 | intangibles nonnegative | 0.000000000000 | PASS |
| 5 | rd nonnegative | 42.479444907900 | PASS |

Valuation bridge: explicit=1204.490875; terminal_fcff=446.963084; terminal=6876.355143; pv_terminal=4269.675533; ev=5474.166408; bridge=66.003000; equity=5540.169408; per_share=228.131332; terminal_share=0.779968. Amounts are USD billions except per_share (USD/share) and terminal_share (fraction).

### Restored base

Changed independent inputs: none.

| Statement field ($bn) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| cash | 195.235 | 427.091 | 707.807 | 1,033.609 | 1,394.188 |
| securities | 76.926 | 76.926 | 76.926 | 76.926 | 76.926 |
| ar | 93.750 | 123.419 | 149.131 | 172.272 | 190.014 |
| inventory | 46.943 | 61.798 | 74.673 | 86.260 | 95.144 |
| prepaid | 5.068 | 6.672 | 8.062 | 9.313 | 10.272 |
| ppe | 22.983 | 34.291 | 47.806 | 61.992 | 77.597 |
| intangibles | 2.207 | 1.179 | 0.000 | 0.000 | 0.000 |
| other_assets | 105.577 | 105.577 | 105.577 | 105.577 | 105.577 |
| ap | 22.388 | 29.473 | 35.614 | 41.140 | 45.377 |
| accrued | 40.082 | 52.766 | 63.759 | 73.653 | 81.238 |
| debt | 33.366 | 33.366 | 33.366 | 33.366 | 33.366 |
| other_liabilities | 15.903 | 15.903 | 15.903 | 15.903 | 15.903 |
| equity | 436.951 | 705.445 | 1,021.341 | 1,381.889 | 1,773.835 |
| revenue | 439.306 | 571.098 | 685.318 | 788.116 | 866.927 |
| opening_cash | 22.443 | 195.235 | 427.091 | 707.807 | 1,033.609 |
| opening_equity | 228.984 | 436.951 | 705.445 | 1,021.341 | 1,381.889 |
| gross | 325.087 | 416.902 | 493.429 | 559.562 | 606.849 |
| cogs | 114.220 | 154.197 | 191.889 | 228.554 | 260.078 |
| sga | 9.753 | 12.507 | 14.803 | 16.787 | 18.205 |
| ebit | 281.156 | 354.081 | 411.191 | 464.988 | 502.818 |
| rd | 34.178 | 50.314 | 67.435 | 77.787 | 85.826 |
| da | 5.272 | 6.853 | 8.224 | 9.457 | 10.403 |
| amortization | 0.791 | 1.028 | 1.179 | 0.000 | 0.000 |
| depreciation | 4.481 | 5.825 | 7.045 | 9.457 | 10.403 |
| interest | 1.335 | 1.335 | 1.335 | 1.335 | 1.335 |
| pretax | 279.822 | 352.746 | 409.856 | 463.654 | 501.483 |
| tax | 47.570 | 59.967 | 69.676 | 78.821 | 85.252 |
| ni | 232.252 | 292.780 | 340.181 | 384.833 | 416.231 |
| capex | 13.179 | 17.133 | 20.560 | 23.643 | 26.008 |
| delta_nwc | 27.267 | 26.358 | 22.844 | 20.560 | 15.762 |
| sbc | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| buybacks | 9.665 | 12.564 | 15.077 | 17.339 | 19.072 |
| dividends | 24.285 | 24.285 | 24.285 | 24.285 | 24.285 |
| net_borrowing | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| cfo | 219.921 | 285.838 | 340.638 | 391.069 | 429.944 |
| cfi | -13.179 | -17.133 | -20.560 | -23.643 | -26.008 |
| cff | -33.950 | -36.849 | -39.362 | -41.624 | -43.357 |
| cash_change | 172.792 | 231.856 | 280.716 | 325.802 | 360.579 |
| assets | 548.690 | 836.954 | 1,169.983 | 1,545.950 | 1,949.718 |
| liabilities | 111.739 | 131.508 | 148.642 | 164.062 | 175.884 |
| balance_gap | -0.000 | -0.000 | -0.000 | -0.000 | 0.000 |
| cash_fcfe | 206.742 | 268.706 | 320.078 | 367.426 | 403.937 |
| fcfe | 197.077 | 256.141 | 305.001 | 350.087 | 384.864 |
| fcff | 198.185 | 257.249 | 306.109 | 351.195 | 385.972 |

| Year | Check | Amount ($bn) | Status |
| --- | --- | ---: | --- |
| 0 | Opening balance sheet gap | -0.000000000000 | PASS |
| 1 | Balance sheet gap | -0.000000000000 | PASS |
| 1 | Cash reconciliation gap | -0.000000000000 | PASS |
| 1 | Equity rollforward gap | -0.000000000000 | PASS |
| 1 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 1 | Working capital gap | -0.000000000000 | PASS |
| 1 | Income statement gap | 0.000000000000 | PASS |
| 1 | FCFF formula gap | 0.000000000000 | PASS |
| 1 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 1 | cash nonnegative | 195.235044600000 | PASS |
| 1 | ppe nonnegative | 22.983268700000 | PASS |
| 1 | intangibles nonnegative | 2.207248300000 | PASS |
| 1 | rd nonnegative | 34.178045700000 | PASS |
| 2 | Balance sheet gap | -0.000000000000 | PASS |
| 2 | Cash reconciliation gap | 0.000000000000 | PASS |
| 2 | Equity rollforward gap | 0.000000000000 | PASS |
| 2 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 2 | Working capital gap | 0.000000000000 | PASS |
| 2 | Income statement gap | 0.000000000000 | PASS |
| 2 | FCFF formula gap | 0.000000000000 | PASS |
| 2 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 2 | cash nonnegative | 427.091393670000 | PASS |
| 2 | ppe nonnegative | 34.291018010000 | PASS |
| 2 | intangibles nonnegative | 1.179271090000 | PASS |
| 2 | rd nonnegative | 50.313773445000 | PASS |
| 3 | Balance sheet gap | -0.000000000000 | PASS |
| 3 | Cash reconciliation gap | -0.000000000000 | PASS |
| 3 | Equity rollforward gap | 0.000000000000 | PASS |
| 3 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 3 | Working capital gap | 0.000000000000 | PASS |
| 3 | Income statement gap | 0.000000000000 | PASS |
| 3 | FCFF formula gap | 0.000000000000 | PASS |
| 3 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 3 | cash nonnegative | 707.807411670000 | PASS |
| 3 | ppe nonnegative | 47.806015620000 | PASS |
| 3 | intangibles nonnegative | 0.000000000000 | PASS |
| 3 | rd nonnegative | 67.435304976000 | PASS |
| 4 | Balance sheet gap | -0.000000000000 | PASS |
| 4 | Cash reconciliation gap | -0.000000000000 | PASS |
| 4 | Equity rollforward gap | 0.000000000000 | PASS |
| 4 | Fixed asset rollforward gap | 0.000000000000 | PASS |
| 4 | Working capital gap | -0.000000000000 | PASS |
| 4 | Income statement gap | 0.000000000000 | PASS |
| 4 | FCFF formula gap | 0.000000000000 | PASS |
| 4 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 4 | cash nonnegative | 1033.609367903700 | PASS |
| 4 | ppe nonnegative | 61.992101118000 | PASS |
| 4 | intangibles nonnegative | 0.000000000000 | PASS |
| 4 | rd nonnegative | 77.787035480700 | PASS |
| 5 | Balance sheet gap | 0.000000000000 | PASS |
| 5 | Cash reconciliation gap | 0.000000000000 | PASS |
| 5 | Equity rollforward gap | -0.000000000000 | PASS |
| 5 | Fixed asset rollforward gap | -0.000000000000 | PASS |
| 5 | Working capital gap | -0.000000000000 | PASS |
| 5 | Income statement gap | 0.000000000000 | PASS |
| 5 | FCFF formula gap | 0.000000000000 | PASS |
| 5 | FCFE to FCFF bridge gap | 0.000000000000 | PASS |
| 5 | cash nonnegative | 1394.188478469840 | PASS |
| 5 | ppe nonnegative | 77.596795165800 | PASS |
| 5 | intangibles nonnegative | 0.000000000000 | PASS |
| 5 | rd nonnegative | 85.825817262900 | PASS |

Valuation bridge: explicit=1102.283477; terminal_fcff=409.726383; terminal=6303.482817; pv_terminal=3913.966891; ev=5016.250368; bridge=66.003000; equity=5082.253368; per_share=209.275411; terminal_share=0.780257. Amounts are USD billions except per_share (USD/share) and terminal_share (fraction).
