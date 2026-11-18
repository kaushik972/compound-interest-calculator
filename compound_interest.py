"""Compound interest calculator.

Usage:
    python compound_interest.py --principal 100000 --rate 7 --years 10
    python compound_interest.py --principal 50000 --rate 5 --years 5 --compounds 12 --monthly 5000

Prints the future value and a year-by-year balance table.
"""
import argparse


def future_value(principal, annual_rate, years, compounds_per_year=1, monthly=0.0):
    r = annual_rate / 100.0
    balance = principal
    yearly = []
    for year in range(1, years + 1):
        for _ in range(compounds_per_year):
            balance += balance * r / compounds_per_year
            balance += monthly
        yearly.append((year, round(balance, 2)))
    return round(balance, 2), yearly


def main():
    p = argparse.ArgumentParser(description="Compound interest calculator")
    p.add_argument("--principal", type=float, default=100000)
    p.add_argument("--rate", type=float, default=7.0, help="Annual interest rate in %")
    p.add_argument("--years", type=int, default=10)
    p.add_argument("--compounds", type=int, default=1, help="Compounding periods per year")
    p.add_argument("--monthly", type=float, default=0.0, help="Extra deposit each period")
    a = p.parse_args()
    total, yearly = future_value(a.principal, a.rate, a.years, a.compounds, a.monthly)
    invested = a.principal + a.monthly * a.compounds * a.years
    print(f"Principal: {a.principal:,.0f} | Rate: {a.rate}% | Years: {a.years}")
    print(f"Total invested: {invested:,.2f}")
    print(f"Future value: {total:,.2f}")
    print(f"Interest earned: {total - invested:,.2f}")
    print("\nYear | Balance")
    for year, balance in yearly:
        print(f"{year:>4} | {balance:>15,.2f}")


if __name__ == "__main__":
    main()
