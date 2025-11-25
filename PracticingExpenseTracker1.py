import csv
import os
from datetime import datetime

# File to store expenses
FILENAME = "expenses.csv"

def init_file():
    """Create file if it doesn't exist with headers"""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    """Add a new expense to the CSV file"""
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g. Food, Rent, Gas): ").strip().title()
    description = input("Enter description: ").strip()
    
    while True:
        try:
            amount = float(input("Enter amount ($): "))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Write to CSV
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, f"{amount:.2f}"])
    print(f"✅ Added expense: {category} - ${amount:.2f}")

def view_expenses():
    """View all saved expenses"""
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return
    
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        print("\n--- Expense History ---")
        for row in reader:
            print(f"{row[0]} | {row[1]:<10} | {row[2]:<20} | ${row[3]}")

def summary():
    """Show total and breakdown by category"""
    if not os.path.exists(FILENAME):
        print("No data to summarize.")
        return
    
    totals = {}
    overall = 0
    
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            overall += amount
            totals[category] = totals.get(category, 0) + amount
    
    print("\n--- Summary ---")
    for cat, amt in totals.items():
        print(f"{cat:<10}: ${amt:.2f}")
    print(f"\nTotal spent: ${overall:.2f}")

def main():
    """Main menu loop"""
    init_file()
    
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
