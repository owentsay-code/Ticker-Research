"""Offline peer P/E calculator. Requires Python 3.12+; standard library only."""

# EDIT THESE INPUTS. Values supplied by the user:
# December 31, 2024 closing prices (USD) and FY2024 total GAAP diluted EPS.
# Use consistent currencies and diluted EPS periods across all companies.
# Decimal strings preserve your entered precision; use None for missing data.
TARGET = {"symbol": "ABG", "price": "243.03", "diluted_eps": "21.50"}
PEERS = [
    # AutoNation: candidate peer.
    {"symbol": "AN", "price": "169.84", "diluted_eps": "16.92"},
    # Group 1 Automotive: qualified candidate peer.
    {"symbol": "GPI", "price": "421.48", "diluted_eps": "36.81"},
]

from fractions import Fraction
from statistics import median


def positive(value):
    """Return an exact positive rational, or None for unusable input."""
    if value is None or isinstance(value, bool):
        return None
    try:
        number = Fraction(str(value))
    except (ValueError, TypeError, ZeroDivisionError):
        return None
    return number if number > 0 else None


def symbol(row):
    return str(row.get("symbol") or "").strip().upper()


def pe(row):
    price = positive(row.get("price"))
    eps = positive(row.get("diluted_eps"))
    return price / eps if price is not None and eps is not None else None


def dollars(value):
    return f"${value:.2f}"


def main(target=TARGET, peers=PEERS):
    target_symbol = symbol(target)
    target_eps = positive(target.get("diluted_eps"))
    target_pe = pe(target)
    print(f"Target: {target_symbol or '(unnamed)'}")
    print("Target P/E: " + (f"{target_pe:.6f}x" if target_pe is not None
                              else "not meaningful (missing or invalid price/EPS)"))
    if target_eps is None:
        print("Target implied prices: not meaningful (missing or invalid diluted EPS)")
    print("Method: peer P/E × target diluted EPS; no cash/debt adjustment.\n")

    unique = []
    seen = set()
    for row in peers:
        name = symbol(row)
        if not name:
            print("Skipped unnamed peer: identity missing.")
        elif name == target_symbol:
            print(f"Excluded target from peers: {name}")
        elif name in seen:
            print(f"Skipped duplicate peer: {name} (first entry retained)")
        else:
            seen.add(name)
            unique.append((name, pe(row)))

    for name, multiple in unique:
        print(f"{name} P/E: " + (f"{multiple:.6f}x" if multiple is not None
                                 else "not meaningful (missing or invalid price/EPS)"))

    valid = [multiple for _, multiple in unique if multiple is not None]
    full_estimate = None
    if not valid:
        print("\nNo usable peers; peer P/E and implied prices: not meaningful.")
    else:
        mid = median(valid)
        print(f"\nValid peers: {len(valid)}")
        print(f"Median peer P/E: {mid:.6f}x")
        if target_eps is not None:
            full_estimate = mid * target_eps
        if len(valid) == 1:
            print("Reference estimate: " + (dollars(full_estimate)
                  if full_estimate is not None else "not meaningful"))
            print("No range: only one valid peer.")
        else:
            for label, multiple in (("Minimum", min(valid)), ("Median", mid),
                                    ("Maximum", max(valid))):
                price = dollars(multiple * target_eps) if target_eps is not None else "not meaningful"
                print(f"{label} peer P/E: {multiple:.6f}x; implied price: {price}")

    print("\nPeer removal sensitivity (change versus full-peer median estimate):")
    if not unique:
        print("No peers to remove.")
    for removed, _ in unique:
        remaining = [multiple for name, multiple in unique
                     if name != removed and multiple is not None]
        if not remaining:
            print(f"Remove {removed}: no estimate (no usable peers remain)")
        elif target_eps is None:
            print(f"Remove {removed}: implied price and dollar change not meaningful (invalid target EPS)")
        else:
            estimate = median(remaining) * target_eps
            change = estimate - full_estimate
            reference = " (reference estimate; one valid peer remains)" if len(remaining) == 1 else ""
            print(f"Remove {removed}: median-implied price {dollars(estimate)}; "
                  f"dollar change {change:+.2f}{reference}")


if __name__ == "__main__":
    main()
