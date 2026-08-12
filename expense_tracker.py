from datetime import datetime
import json
class Expense:
    def __init__(self, expense_id, date, category, description, amount):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def display(self):
        print("-" * 40)
        print("ID          :", self.expense_id)
        print("Date        :", self.date)
        print("Category    :", self.category)
        print("Description :", self.description)
        print("Amount      :", f"{self.amount:.2f}")
        
expenses = []

#========= Save Expense =========
def save_expenses():
    data = []

    for expense in expenses:
        data.append({
            "expense_id": expense.expense_id,
            "date": expense.date,
            "category": expense.category,
            "description": expense.description,
            "amount": expense.amount
        })

    with open("expenses.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Expenses saved successfully!")
    
#========= Load Expense ==========
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            data = json.load(file)

        expenses.clear()

        for item in data:
            expense = Expense(
                item["expense_id"],
                item["date"],
                item["category"],
                item["description"],
                float(item["amount"])
            )

            expenses.append(expense)

        print("Expenses loaded successfully!")

    except FileNotFoundError:
        print("No saved expenses found.")

    except json.JSONDecodeError:
        print("Error: expenses.json contains invalid data.")
        
#========= Get ID =============
def get_next_expense_id():
    if not expenses:
        return 1

    return max(expense.expense_id for expense in expenses) + 1
    
#=========== Add Expense ==========
def add_expense():
    expense_id = get_next_expense_id()

    #Date
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

    #Category        
    while True:
       category = input("Enter category: ").strip()

       if category == "":
        print("Category cannot be empty.")
       else:
        category = category.title()
        break 

    # Description 
    while True:
        description = input("Enter description: ").strip()

        if description == "":
            print("Description cannot be empty.")
        else:
            description = description.title()
            break

    #Amount 
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number for the amount.")

    expense = Expense(
        expense_id,
        date,
        category,
        description,
        amount
    )

    expenses.append(expense)
     
    save_expenses()
     
    print("Expense added successfully!")
# =========== View Expenses ==========
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n================ ALL EXPENSES ================")

    print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Category':<15}"
        f"{'Description':<20}"
        f"{'Amount':>5}"
    )

    print("-" * 60)

    for expense in expenses:
        print(
            f"{expense.expense_id:<5}"
            f"{expense.date:<15}"
            f"{expense.category:<15}"
            f"{expense.description:<20}"
            f"{expense.amount:>5.2f}"
        )

    print("-" * 60)
 

 # =========== Total Expenses ==========

def total_expenses():
    if not expenses:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        total += expense.amount

    print("\n===== TOTAL EXPENSES =====")
    print(f"Total: {total:.2f}")   
   
   
 # ===== Filter by Category ==========

def filter_by_category():
    category = input("Enter category to search: ").strip()

    found = False

    print(f"\n===== EXPENSES IN {category.upper()} =====")

    for expense in expenses:
        if expense.category.lower() == category.lower():
            expense.display()
            found = True

    if not found:
        print("No expenses found in this category.")

        
 #========== Category Summary =====
def category_summary():
    if not expenses:
        print("No expenses found.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense.category

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense.amount

    print("\n===== CATEGORY SUMMARY =====")

    for category, total in category_totals.items():
        print(f"{category:<20} : {total:.2f}")
        
#============ Update Expense =========
def update_expense():
    try:
        expense_id = int(input("Enter Expense ID to update: "))
    except ValueError:
        print("Expense ID must be a number.")
        return

    for expense in expenses:
        if expense.expense_id == expense_id:

            print("\nExpense found!")
            expense.display()

            # Update Date
            while True:
                date = input("Enter new Date (YYYY-MM-DD): ").strip()

                if date == "":
                    print("Date cannot be empty.")
                    continue

                try:
                    datetime.strptime(date, "%Y-%m-%d")
                    expense.date = date
                    break

                except ValueError:
                    print("Invalid date. Please use YYYY-MM-DD.")

            # Update Category
            while True:
                category = input("Enter new category: ").strip()

                if category == "":
                    print("Category cannot be empty.")
                else:
                    expense.category = category.title()
                    break

            # Update Description
            while True:
                description = input("Enter new description: ").strip()

                if description == "":
                    print("Description cannot be empty.")
                else:
                    expense.description = description.title()
                    break

            # Update Amount
            while True:
                try:
                    amount = float(input("Enter new amount: "))

                    if amount <= 0:
                        print("Amount must be greater than zero.")
                    else:
                        expense.amount = amount
                        break

                except ValueError:
                    print("Please enter a valid number.")

            # Save changes
            save_expenses()

            print("\nExpense updated successfully!")
            expense.display()
            return

    print("Expense not found.")
    
#============ Delete Expense ========
def delete_expense():
    try:
        expense_id = int(input("Enter Expense ID to delete: "))

    except ValueError:
        print("Expense ID must be a number.")
        return

    for expense in expenses:
        if expense.expense_id == expense_id:

            print("\nExpense found!")
            expense.display()

            confirm = input("Are you sure you want to delete it? (yes/no): ").strip().lower()

            if confirm == "yes":
                expenses.remove(expense)
                save_expenses()
                print("Expense deleted successfully!")
            else:
                print("Expense was not deleted.")

            return

    print("Expense not found.")
#========= Expense Report ==========
def expense_report():
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:
        total += expense.amount

        if expense.amount > highest.amount:
            highest = expense

        if expense.amount < lowest.amount:
            lowest = expense

    count = len(expenses)
    average = total / count

    print("\n===== EXPENSE REPORT =====")
    print(f"Total Expenses     : {total:.2f}")
    print(f"Number of Expenses : {count}")
    print(f"Average Expense    : {average:.2f}")
    print(f"Highest Expense    : {highest.amount:.2f}")
    print(f"Lowest Expense     : {lowest.amount:.2f}")

    print("\n===== HIGHEST EXPENSE =====")
    highest.display()

    print("\n===== LOWEST EXPENSE =====")
    lowest.display()
    
# load expense initially   
load_expenses()

#============Menu ============
#Main menu
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("       1. Add Expense")
    print("       2. View Expenses")
    print("       3. Total Expenses")
    print("       4. Search by Category")
    print("       5. Category Summary")
    print("       6. Update Expense")
    print("       7. Delete Expense")
    print("       8. Expense Report")
    print("       9. Exit")

    choice = input("     Enter your choice: ")


 
    if choice == "1":
        print("\nAdd Expense")
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("\nTotal Expenses")
        total_expenses()
    elif choice == "4":
        filter_by_category()
    elif choice == "5":
        category_summary()
    elif choice == "6":
        update_expense()
    elif choice == "7":
        delete_expense()
    elif choice == "8":
        expense_report()
    elif choice == "9":
        save_expenses()
        print("Thank you for using Expense Tracker!")
        break   
    else:
        print("Invalid choice. Please try again.")