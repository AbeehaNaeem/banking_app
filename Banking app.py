accounts = []
account_number = 1000
def create_account():
    global account_number
    account_name = input("Enter your name: ")
    try:
        account_password = int(input("Enter your PIN: "))
    except ValueError:
        print("Invalid input. Please try again.")
        return
    print("Welcome, " + account_name, "Your account number is", account_number)
    balance = 0
    transactions = []
    account = [
        account_number,
        account_name,
        account_password,
        balance,
        transactions
    ]
    accounts.append(account)
    account_number = account_number + 1
current_account = None
def login():
    global current_account
    try:
        entered_account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your PIN: "))
    except ValueError:
        print("Invalid input. Please try again.")
        return
    found = False
    for account in accounts:
        if account[0] == entered_account_number and account[2] == pin:
            found = True
            print("Welcome back, ",account[1])
            current_account = account
    if not found:
        print("Incorrect account or PIN. Please try again.")
        return
def deposit_money():
    global current_account
    if current_account is None:
        print("Please login first")
        return
    try:
        amount = int(input("Enter your deposit amount: "))
    except ValueError:
        print("Invalid input. Please try again.")
        return
    if amount <= 0:
        print("PLease enter a number greater than 0.")
        return
    current_account[3] = current_account[3] + amount
    print("Amount deposited successfully!")
    current_account[4].append(f"Deposited {amount}")


def withdraw_money():
    global current_account
    if current_account is None:
        print("Please login first")
        return
    try:
        amount = int(input("Enter your withdraw amount: "))
    except ValueError:
        print("Invalid input. Please try again.")
        return
    if amount <= 0:
        print("PLease enter a number greater than 0.")
        return
    if amount > current_account[3]:
        print("Your balance is insufficient.")
        return
    current_account[3] -= amount
    print("Amount withdrawn successfully!")
    current_account[4].append(f"Withdrawn {amount}")


def check_balance():
    global current_account
    if current_account is None:
        print("Please login first")
        return
    print("Your current balance is", current_account[3])
    return

def transaction_history():
    global current_account
    if current_account is None:
        print("Please login first")
        return
    for transaction in current_account[4]:
        print(transaction)

def logout():
    global current_account
    current_account = None
    print("Logged out successfully!")

def exit_program():
    print("Thank you for using Banking App")

while True:
    print("""
What do you want to do?
1. Create Account
2. Login
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. View Transaction History
7. Logout
8. Exit""")
    try:
        choice = int(input("Press a number between 1 and 8: "))
    except ValueError:
        print("Invalid input. Please try again.")
        continue
    if choice == 1:
        create_account()

    elif choice == 2:
        login()

    elif choice == 3:
        deposit_money()

    elif choice == 4:
        withdraw_money()

    elif choice == 5:
        check_balance()

    elif choice == 6:
        transaction_history()

    elif choice == 7:
        logout()

    elif choice == 8:
        exit_program()
        break

    else:
        print("Invalid input. Please try again.")







