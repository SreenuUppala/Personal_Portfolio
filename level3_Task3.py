import os
import csv
from datetime import datetime

print("Welcome to Flexible Sales Report Automation Tool")
print("-" * 50)

PROJECT_PATH = os.getcwd()

csv_name = input("Enter CSV file name (example: data.csv): ").strip()
csv_file_path = os.path.join(PROJECT_PATH, csv_name)

if not os.path.exists(csv_file_path):
    print(f"File '{csv_name}' not found in this folder.")
    exit()

try:
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        print("\nCSV Columns Detected:", headers)

        quantity_col = input("Enter the column name for Quantity/Count: ").strip()
        price_col = input("Enter the column name for Price: ").strip()

        if quantity_col not in headers or price_col not in headers:
            print("Column names not found in CSV. Please check spelling.")
            exit()

        total_items = 0
        total_sales = 0

        for row in reader:
            try:
                quantity = float(row[quantity_col])
                price = float(row[price_col])
                total_items += quantity
                total_sales += quantity * price
            except ValueError:
                continue

except Exception as e:
    print("Error reading CSV:", e)
    exit()
report_name = "summary_report.txt"
report_path = os.path.join(PROJECT_PATH, report_name)

with open(report_path, "w", encoding="utf-8") as report:
    report.write("Flexible Sales Report\n")
    report.write("-" * 40 + "\n")
    report.write(f"Date & Time: {datetime.now()}\n")
    report.write(f"Total Items Sold ({quantity_col}): {total_items}\n")
    report.write(f"Total Sales Amount ({price_col}): ₹{total_sales}\n")

print("\nReport generated successfully!")
print(f"Report saved as: {report_name}")
