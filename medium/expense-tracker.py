# Predefined categories with initial values as 0
categories = {
    "groceries": 0.0,
    "food": 0.0,
    "fuel": 0.0,
    "college": 0.0
}


# Function to add an expense
def add_expense():
    print("\nChoose a category:")
    # Show existing categories with numbers
    for i, cat in enumerate(categories.keys(), start=1):
        print(f"{i}. {cat.capitalize()}")
    # Option to add a custom category
    print(f"{len(categories) + 1}. Add Custom Category")

    try:
        # Take category choice from user
        choice = int(input("Enter choice: "))

        if 1 <= choice <= len(categories):
            # Select an existing category
            category = list(categories.keys())[choice - 1]
        elif choice == len(categories) + 1:
            # Add a new custom category
            category = input("Enter new category name: ").lower()
            if category not in categories:
                categories[category] = 0.0
        else:
            print("Invalid choice.")
            return

        # Take expense amount
        amount = float(input("Enter amount: "))
        categories[category] += amount  # Update category total
        print("Expense added successfully!")

    except ValueError:
        print("Invalid input! Please enter numbers where required.")


# Function to view total expenses across all categories
def view_total():
    total = sum(categories.values())
    print(f"\nTotal spent: {total}")


# Function to view expenses per category
def view_breakdown():
    # Check if there are any expenses recorded
    if not any(amount > 0 for amount in categories.values()):
        print("No expenses recorded yet.")
        return
    print("\nExpenses by Category:")
    for category, amount in categories.items():
        print(f"{category.capitalize()}: {amount}")


# Main menu loop
while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Total Spent")
    print("3. View Per-Category Breakdown")
    print("4. Exit")

    # Take user choice
    choice = input("Enter choice: ")

    # Call functions based on choice
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_total()
    elif choice == "3":
        view_breakdown()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again!")
