#!/usr/bin/env python3
import json
import csv
import sys
import os

def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])

def process_data(data):
    """Analyzes the data, looking for maximums.
    Returns a list of lines that summarize the information.
    """
    max_sales = {"total_sales": 0}
    max_revenue = {"revenue": 0}
    car_year_sales = {} # Replaced defaultdict with standard dict for portability

    for item in data:
        # Convert "$1234.56" into float 1234.56
        # Using standard float() instead of locale for better compatibility
        item_price = float(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        
        # Calculate Revenue
        item["revenue"] = item_revenue
        if item_revenue > max_revenue["revenue"]:
            max_revenue = item

        # Calculate Sales
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales = item
            
        # Calculate Popular Year
        year = item["car"]["car_year"]
        car_year_sales[year] = car_year_sales.get(year, 0) + item["total_sales"]

    # Find the year with the most sales
    # Using 'key' argument for max() is cleaner than the loop
    popular_year = max(car_year_sales, key=car_year_sales.get)
    popular_sales = car_year_sales[popular_year]

    summary = []
    summary.append("The {} generated the most revenue: ${:,.2f}".format(
        format_car(max_revenue["car"]), max_revenue["revenue"]))
    summary.append("The {} had the most sales: {}".format(
        format_car(max_sales["car"]), max_sales["total_sales"]))
    summary.append("The most popular year was {} with {} sales.".format(
        popular_year, popular_sales))

    return summary

def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return table_data

def generate_csv_report(table_data):
    """Generates a CSV report instead of PDF for portability."""
    output_file = 'sales_summary_report.csv'
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(table_data)
    print(f"[✓] Detailed report generated: {output_file}")

def send_email_simulation(summary):
    """Simulates sending an email by printing to console."""
    print("\n--- [SIMULATING EMAIL SEND] ---")
    print("To: manager@example.com")
    print("Subject: Sales summary for last month")
    print("Body:")
    print("\n".join(summary))
    print("-------------------------------\n")

def main():
    json_file = "car_sales.json"
    data = load_data(json_file)
    summary = process_data(data)
    table_data = cars_dict_to_table(data)

    # 1. Print Summary to Console (Email Simulation)
    send_email_simulation(summary)

    # 2. Generate CSV Attachment
    generate_csv_report(table_data)

if __name__ == "__main__":
    main()