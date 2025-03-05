import csv
from datetime import datetime

# Function to handle user input with validation
def get_valid_input(prompt, error_message, cast_to=str):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Input cannot be empty.")
            if cast_to == float:
                return float(user_input)
            elif cast_to == int:
                return int(user_input)
            elif cast_to == "date":
                # Attempt to parse the date
                datetime.strptime(user_input, "%Y-%m-%d")
                return user_input
            else:
                return user_input
        except ValueError:
            print(error_message)

# Function to choose or add a category
def choose_category():
    """
    This function allows the user to select an existing category or add a new one dynamically.
    """
    print("\n--- Categories ---")
    categories = ["food", "transportation", "entertainment", "other"]  # Initial default categories
    while True:
        # Display the current list of categories
        print("Available categories:", ", ".join(categories))
        category = input("Enter a category (or type a new one to add it): ").strip()
        
        if category:  # Check if input is not empty
            if category not in categories:
                # Add the new category to the list
                categories.append(category)
                print(f"New category '{category}' added!")
            return category
        else:
            print("Category cannot be empty. Please try again.")

# Function to add a new expense
def add_expense():
    print("\n--- Add a New Expense ---")
    date = get_valid_input("Enter date (YYYY-MM-DD): ", "Invalid date format. Please try again.", cast_to="date")
    amount = get_valid_input("Enter amount spent: ", "Invalid amount. Please enter a numeric value.", cast_to=float)
    category = choose_category()
    description = get_valid_input("Enter a brief description: ", "Description cannot be empty.")
    return {"date": date, "amount": amount, "category": category, "description": description}

# Function to save an expense to a CSV file
def save_expense(expense, filename="expenses.csv"):
    try:
        file_exists = False
        with open(filename, "r") as file:
            file_exists = True
    except FileNotFoundError:
        pass  # File doesn't exist yet, so it will be created.

    try:
        with open(filename, "a", newline="") as file:
            fieldnames = ["date", "amount", "category", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(expense)
        print(f"Expense saved successfully!\n")
    except Exception as e:
        print(f"Error saving expense: {e}")

# Function to view expenses
def view_expenses(filename="expenses.csv"):
    print("\n--- View Expenses ---")
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
            if not expenses:
                print("No expenses recorded yet.")
                return
            for expense in expenses:
                print(f"Date: {expense['date']},\nAmount: {expense['amount']}, \nCategory: {expense['category']}, \nDescription: {expense['description']}")
                print()
    except FileNotFoundError:
        print("No expense file found. Add some expenses first!")
    except Exception as e:
        print(f"Error viewing expenses: {e}")

# Function to analyze expenses by category
def analyze_expenses(filename="expenses.csv"):
    print("\n--- Analyze Expenses ---")
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            category_totals = {}
            for expense in reader:
                category = expense["category"]
                amount = float(expense["amount"])
                category_totals[category] = category_totals.get(category, 0) + amount
            for category, total in category_totals.items():
                print(f"Total spent on {category}: {total}")
    except FileNotFoundError:
        print("No expense file found. Add some expenses first!")
    except Exception as e:
        print(f"Error analyzing expenses: {e}")

# Main menu function
def main():
    print("Welcome to the Expense Tracker!")
    while True:
        print("\n--- Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            expense = add_expense()
            if expense:
                save_expense(expense)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_expenses()
        elif choice == "4":
            print("Termination Of The Program!")
            print('+-------------------------------------------------+')
            print('+----------THANKS FOR USING OUR APPLICATION-------+')
            print('+-------------------------------------------------+')


            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
#main function (driver function)the programs starts from main() functions
            
main()
