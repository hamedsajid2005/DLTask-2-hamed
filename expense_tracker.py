print("\n===== EXPENSE TRACKER =====")

total = 0
count = 0

while True:
    expense = input("Enter expense amount (or type 'quit' to finish): ")

    if expense.lower() == "quit":
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("❌ Expense cannot be negative.")
            continue

        total += expense
        count += 1

        print(f"✅ Expense added: ₹{expense:.2f}")
        print(f"Current Total: ₹{total:.2f}")

    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

print("\n----- EXPENSE SUMMARY -----")
print(f"📊 Number of Expenses: {count}")
print(f"Total Spent: ₹{total:.2f}")

if count > 0:
    print(f"Average Expense: ₹{total / count:.2f}")

print("\nThank you for using Expense Tracker!")