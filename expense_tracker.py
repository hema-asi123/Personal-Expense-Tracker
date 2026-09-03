

def add_expense():
    print("Add Expense")
    expense_name = input("Enter name: ")
    expense_amount = int(input("Enter amount: "))

    expense_list = [expense_name, expense_amount]
    print(expense_list)

    with open("expenses.txt", "a") as file:
        file.write(f"{expense_name} - {expense_amount}\n")

    print("Expense added successfully!")


def show_expenses():
    total = 0

    print("\n===== YOUR EXPENSES =====")

    with open("expenses.txt", "r") as file:
        for number, expense in enumerate(file, start=1):
            expense = expense.strip()

            parts = expense.split(" - ")
            amount = int(parts[1])

            print(f"{number}. {expense}")
            total = total + amount
    print(f"\nTotal Expense: ₹{total}")
def delete_expense():
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()

    if not expenses:
        print("No expenses found.")
        return

    print("\n===== DELETE EXPENSE =====")

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense.strip()}")

    choice = int(input("Enter expense number to delete: "))

    if 1 <= choice <= len(expenses):
        deleted = expenses.pop(choice - 1)

        with open("expenses.txt", "w") as file:
            file.writelines(expenses)

        print(f"Deleted: {deleted.strip()}")
    else:
        print("Invalid expense number.")
while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    print("4. Delete Expense")

    pick = input("Enter your choice: ")

    if pick == "1":
        add_expense()

    elif pick == "2":
        show_expenses()

    elif pick == "3":
        print("Exit")
        break

    elif pick == "4":
        delete_expense()

    else:
        print("Invalid Choice")