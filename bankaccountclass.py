class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Deposit must be greater than 0.")
        else:
            self.balance += amount
            print("Deposit successful.")
            print("Amount deposited:", amount)

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Withdrawal must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")
            print("Amount withdrawn:", amount)

    # Check balance
    def check_balance(self):
        print("Current balance:", self.balance)


# Create account
name = input("Enter account holder name: ")

account = BankAccount(name)

print("\nAccount created successfully!")
print("Account holder:", account.name)

# Menu
while True:
    print("\n===== BANK ACCOUNT =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using the Bank Account system.")
        break

    else:
        print("Invalid choice. Please try again.")
   