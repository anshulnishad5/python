class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")

    def get_balance(self):
        return self.balance

# Example usage
account = Bankaccount("Anshul", 1000)
account.deposit(500)  # Deposited 500. New balance is 1500.
account.withdraw(200)  # Withdrew 200. New balance is 1300.
print(f"Current balance: {account.get_balance()}")  # Current balance: 1300
