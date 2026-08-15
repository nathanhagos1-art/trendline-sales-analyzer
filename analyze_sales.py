"""
TrendLine Sales Analyzer
-------------------------
A small command-line tool that reads retail sales transaction data
(CSV) and produces a summary report: total revenue, revenue by
category, best-selling products, and stock risk alerts.

Usage:
    python analyze_sales.py sales_data.csv

Requires only the Python standard library.
"""

import csv
import sys
from collections import defaultdict


LOW_STOCK_THRESHOLD = 10


def load_transactions(path):
    """Read the CSV file and return a list of transaction dicts
    with numeric fields converted to int/float."""
    transactions = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["units_sold"] = int(row["units_sold"])
            row["unit_price"] = float(row["unit_price"])
            row["stock_remaining"] = int(row["stock_remaining"])
            transactions.append(row)
    return transactions


def total_revenue(transactions):
    return sum(t["units_sold"] * t["unit_price"] for t in transactions)


def revenue_by_category(transactions):
    totals = defaultdict(float)
    for t in transactions:
        totals[t["category"]] += t["units_sold"] * t["unit_price"]
    # highest revenue first
    return sorted(totals.items(), key=lambda item: item[1], reverse=True)


def top_products_by_units(transactions, top_n=3):
    units = defaultdict(int)
    for t in transactions:
        units[t["product"]] += t["units_sold"]
    ranked = sorted(units.items(), key=lambda item: item[1], reverse=True)
    return ranked[:top_n]


def stock_risk_alerts(transactions):
    """Flag the latest known stock level per product: negative stock
    (oversold) or fewer than LOW_STOCK_THRESHOLD units remaining."""
    latest_stock = {}
    for t in transactions:
        # later rows overwrite earlier ones, giving the most recent
        # stock_remaining figure per product
        latest_stock[t["product"]] = t["stock_remaining"]

    alerts = []
    for product, stock in latest_stock.items():
        if stock < 0:
            alerts.append(("OVERSOLD", product, stock))
        elif stock < LOW_STOCK_THRESHOLD:
            alerts.append(("LOW STOCK", product, stock))
    return alerts


def print_report(transactions):
    bar = "=" * 55
    print(bar)
    print("TRENDLINE SALES REPORT")
    print(bar)
    print(f"Rows analysed: {len(transactions)}")
    print(f"Total revenue: £{total_revenue(transactions):,.2f}")

    print("\nRevenue by category:")
    for category, revenue in revenue_by_category(transactions):
        print(f"  {category:<15} £{revenue:,.2f}")

    print("\nTop 3 products by units sold:")
    for product, units in top_products_by_units(transactions):
        print(f"  {product:<20} {units} units")

    alerts = stock_risk_alerts(transactions)
    print(f"\nStock risk alerts ({len(alerts)}):")
    for kind, product, stock in alerts:
        print(f"  [{kind}] {product}: {stock} units remaining")

    print(bar)


def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze_sales.py <sales_data.csv>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        transactions = load_transactions(path)
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        sys.exit(1)

    if not transactions:
        print("No transactions found in file.")
        sys.exit(0)

    print_report(transactions)


if __name__ == "__main__":
    main()
