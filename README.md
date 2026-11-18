# Compound Interest Calculator

A small Python CLI that shows how savings grow with compound interest.

## What it does
- Future value of a lump sum at a given annual rate
- Optional monthly top-ups and compounding frequency (yearly, monthly, …)
- Year-by-year balance table, plus total invested vs interest earned

## Run it
```bash
python compound_interest.py --principal 100000 --rate 7 --years 10
python compound_interest.py --principal 50000 --rate 5 --years 5 --compounds 12 --monthly 5000
```

## Example
`--principal 100000 --rate 7 --years 10` → future value **196,715.14** (interest earned 96,715.14).

Built by Shivam Kaushik as a daily mini project — Python, no dependencies.
