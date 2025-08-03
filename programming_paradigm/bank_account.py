class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated balance attribute
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self._account_balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw amount must be non-negative.")
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
