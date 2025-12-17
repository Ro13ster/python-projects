import sqlite3

def main():
    connections = sqlite3.connect("finance_tracker.db")
    cursor = connections.cursor()
    results = ""
    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total spending")
        print("4. Spending by category")
        print("5. Eixt")
        choice = input("Choose a number: ")
        if choice == "1":
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter a description: ")
            date = input("Enter the date: ")
            cursor.execute(f"INSERT INTO expenses (amount, category, description, date) VALUES ('{amount}', '{category}', '{description}', '{date}')")
            connections.commit()
            print("Expense added")
        elif choice == "2":
            cursor.execute("SELECT * FROM expenses;")
            expenses = cursor.fetchall()
            for expense in expenses:
                print(f"Here's your expenses: {expense}")  
        elif choice == "3":
            cursor.execute("SELECT SUM(amount) FROM expenses;")
            sum = cursor.fetchall()
            for expense in sum:
                print(f"Here's the sum: {expense}")
        elif choice == "4":
            cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
            sum_by_category = cursor.fetchall()
            for expense in sum_by_category:
                print(f"Here's the sum expenses based on category: {expense}")
        elif choice == "5":
            break
        else:
            print("Choose a correct number!")

main()