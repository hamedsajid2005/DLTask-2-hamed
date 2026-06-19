# Expense Tracker

## Description
Expense Tracker is a simple Python program that helps users record and track their expenses. Users can enter multiple expense amounts, and the program calculates the total amount spent. When the user types "quit", the program displays a summary of all expenses entered.

## Features
- Add multiple expenses
- Calculate total spending
- Display the current total after each entry
- Show expense summary
- Handle invalid inputs using error handling

## How to Run

1. Make sure Python is installed on your system.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python expense_tracker.py
```

## Example Output

```text
----- EXPENSE TRACKER -----

Enter expense amount (or type 'quit' to finish): 100
✅ Expense added: ₹100.00
Current Total: ₹100.00

Enter expense amount (or type 'quit' to finish): 200
✅ Expense added: ₹200.00
Current Total: ₹300.00

Enter expense amount (or type 'quit' to finish): quit

----- EXPENSE SUMMARY -----

📊 Number of Expenses: 2
Total Spent: ₹300.00
Average Expense: ₹150.00

Thank you for using Expense Tracker!
```

## Author

Created as part of the DecodeLabs Python Programming Internship.