class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient."""
        if amount > self.account_balance:
            return False  # Insufficient funds
        elif amount > 0:
            self.account_balance -= amount
            return True
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")
            return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")

