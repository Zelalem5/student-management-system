# Expense Tracker 💰

A simple command-line Expense Tracker built with Python.

This project allows users to record, view, update, delete, search, and analyze their personal expenses. Expense data is stored permanently in a JSON file.

## 🚀 Features

- Add new expenses
- Automatically generate Expense IDs
- Validate expense dates
- Validate categories and descriptions
- Validate expense amounts
- View all expenses
- Calculate total expenses
- Search expenses by category
- Generate category summaries
- Update existing expenses
- Delete expenses
- Generate expense reports
- Find highest and lowest expenses
- Calculate average expense
- Save expenses to a JSON file
- Load expenses from a JSON file
- Handle invalid user input
- Handle missing or invalid JSON files

## 🛠️ Technologies Used

- Python 3
- JSON
- `datetime` module

## 📂 Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
├── expenses.json
├── README.md
└── .gitignore

▶️ How to Run
Make sure Python 3 is installed.
Open a terminal in the project folder and run:
python expense_tracker.py
📋 Main Menu
===== EXPENSE TRACKER =====

1. Add Expense
2. View Expenses
3. Total Expenses
4. Search by Category
5. Category Summary
6. Update Expense
7. Delete Expense
8. Expense Report
9. Exit

💾 Data Storage
The application stores expense information in:

    expenses.json
    
The data is saved automatically when:

 - A new expense is added
 
 - An expense is updated
 
 - An expense is deleted
 
 - The program is exited

Example JSON data:

   [
    {
        "expense_id": 1,
        "date": "2026-08-12",
        "category": "Food",
        "description": "Lunch",
        "amount": 250.0
    }
]

📊 Expense Report

The Expense Report provides:

 - Total expenses
 
 - Number of expenses
 
 - Average expense
 
 - Highest expense
 
 - Lowest expense
 
Example:
      
     ===== EXPENSE REPORT =====

Total Expenses     : 3500.00
Number of Expenses : 8
Average Expense    : 437.50
Highest Expense    : 1200.00
Lowest Expense     : 100.00 


🔍 Search by Category

Users can search for expenses by category.

For example:

      Enter category to search: food
      
The program finds expenses regardless of capitalization.

   Food
   food
   FOOD
   
are treated as the same category.

🛡️ Input Validation

The program validates user input to prevent common errors.

Date

Dates must use: YYYY-MM-DD

Example: 2026-08-12

Amount
The amount must be greater than zero.
Category

The category cannot be empty.

Description
The description cannot be empty.

Expense ID
The program checks that the entered Expense ID is a number.

⚠️ Error Handling
The program uses try/except to handle invalid input.

For example:
    
    try:
    amount = float(input("Enter amount: "))
except ValueError:
    print("Please enter a valid number.")
    
It also handles problems with the JSON file:

except FileNotFoundError:
    print("No saved expenses found.")

except json.JSONDecodeError:
    print("Error: expenses.json contains invalid data.")
    
🎯 Learning Objectives

This project demonstrates several important Python concepts:

  - Classes and objects
  - Lists
  - Dictionaries
  - Functions
  - Loops
  - Conditional statements
  - Exception handling
  - File handling
  - JSON data storage
  - String formatting
  - Date validation
  - CRUD operations
  - Searching and filtering
  - Basic data analysis
  
🔄 CRUD Operations

The project implements the basic CRUD 
operations:

    Operation       Feature
      Create      Add Expense
      Read        View/Search Expenses       Update       Update Expense
      Delete      Delete Expense

🔮 Future Improvements
Possible future versions could include:
  - Monthly expense reports
  - Date-range filtering
  - Budget management
  - Income tracking
  - Balance calculation
  - Graphical user interface (GUI)
  - SQLite database
  - User authentication
  - Export reports to CSV
  - Web-based version
  
  
👨‍💻 Author

Zelalem

This project was created as part of my Python programming and portfolio development journey