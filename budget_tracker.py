import json

def total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    return sum

def current_balance(expenses, budget):
    return budget - total_expenses(expenses)

def show_budget_details(expenses, budget):
    print(f"Total budget: {budget}")
    print("Expenses")
    for index, expense in enumerate(expenses):
        print(f"{index + 1}) {expense['description']}: {expense['amount']}")
    print(f"Total money spent: {total_expenses(expenses)}")
    print(f"Remaining Budget: {current_balance(expenses, budget)}")


def add_expense(expenses, description, amount):
    expenses.append({'description': description, 'amount': amount})
    print("Expense Added")
    print(f"Description: {description}, Amount: {amount}")

def load_budget_details(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return data['initial_budget'], data['exepenses']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def save_budget_details(filepath, expenses, budget):
    data = {
        'initial_budget': budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print("Welcome to the budget tracker App")
    filepath = "budget_data1.json"
    initial_budget, expenses = load_budget_details(filepath)
    initial_budget = float(input("What is your budget?"))
    budget = initial_budget
    expenses = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice. 1,2 or 3:")

        if choice == "1":
            description = input("Enter expense description")
            amount = float(input("Enter expense amount"))
            add_expense(expenses, description, amount)
        elif choice == "2":
            show_budget_details(expenses, budget)
        elif choice == "3":
            save_budget_details(filepath, expenses, budget)
            print("Exiting the budget app. Bye for now.")
            break
        else:
            print("Invalid option selected. Try again.")

if __name__ == '__main__':
    main()