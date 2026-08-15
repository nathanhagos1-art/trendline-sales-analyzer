A small Python command-line tool that reads retail sales transaction data and produces a summary report: total revenue, revenue by category, best-selling products, and stock risk alerts (oversold or low-stock items).
This is a code-based companion to my TrendLine Sales Dashboard (built in Excel), for the same fictional retail client, TrendLine. Where the Excel version demonstrates the reporting logic through formulas and conditional formatting, this version demonstrates the same logic in code: reading raw data, aggregating it, and flagging what needs attention.
What it does
Given a CSV of daily sales transactions (sales_data.csv), the script:
Loads and parses the data
Calculates total revenue across all transactions
Breaks down revenue by product category, highest first
Ranks the top 3 products by units sold
Flags stock risk alerts: products that are oversold (negative stock) or running low (fewer than 10 units remaining)
Example output
=======================================================
TRENDLINE SALES REPORT
=======================================================
Rows analysed: 20
Total revenue: £9,487.63

Revenue by category:
  Tops            £3,869.58
  Bottoms         £3,303.86
  Outerwear       £1,319.78
  Accessories     £994.41

Top 3 products by units sold:
  Cotton T-Shirt       242 units
  Running Shorts       73 units
  Denim Jeans          41 units

Stock risk alerts (3):
  [OVERSOLD] Cotton T-Shirt: -80 units remaining
  [LOW STOCK] Denim Jacket: 1 units remaining
  [OVERSOLD] Leather Belt: -3 units
  Running it
Code
python analyze_sales.py sales_data.csv
Requires only the Python standard library — no external packages.
Why I built this
The Excel dashboard project taught me a lot about structuring reporting logic (lookups, conditional flags, category breakdowns). I wanted to see the same logic expressed in code rather than formulas, partly to understand it more deeply, and partly because so much of real-world reporting and data work happens in code, not spreadsheets.
