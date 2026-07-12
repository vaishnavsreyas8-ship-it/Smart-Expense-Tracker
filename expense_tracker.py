expenses = []

def add_expense():
    try:
        amount = float(input("Enter expense amount: ₹"))
        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense List ---")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. ₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")


while True:
    print("\n===== SMART EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Thank you for using Smart Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
