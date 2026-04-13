import uuid


class BankAccount:
    def __init__(self, owner):
        self.account_number = uuid.uuid4()
        self.owner = owner
        self._balance = 0
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self._balance += amount
        self.history.append((amount, 'deposit'))
        print(f"Amount {amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")

        if amount > self._balance:
            raise ValueError(
                f"Withdrawal amount must be less than current balance.")

        self._balance -= amount
        self.history.append((amount, 'withdraw'))
        print(f"Amount {amount} withdrawn successfully.")

    def get_balance(self):
        return self._balance

    def display_history(self):
        print("\nTransactions History:")
        for amount, transaction_type in self.history:
            print(f"Amount: {amount:<8} Type: {transaction_type}")

    def __str__(self):
        return f"Account Number: {self.account_number} Owner Name: {self.owner:<15} Current Balance: {self._balance}"


class SavingsAccount(BankAccount):
    interest_rate = 0.05

    def apply_interest(self):
        interest_amount = self._balance * self.interest_rate
        self._balance += interest_amount
        self.history.append((interest_amount, 'interest'))
        print("Interest of 5% is applied successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self._balance * 0.5:
            raise ValueError(
                "Cannot withdraw more than 50% of balance.")
        super().withdraw(amount)


class CurrentAccount(BankAccount):
    overdraft_limit = 500

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if self._balance - amount < -self.overdraft_limit:
            raise ValueError(
                "Cannot exceed overdraft limit.")

        self._balance -= amount
        self.history.append((amount, 'withdraw'))
        print(
            f"Amount {amount} withdrawn successfully from your current account.")


def main():
    print(f"{'=' * 80}")
    print("Normal Account")
    print(f"{'=' * 80}\n\n")
    normal_account = BankAccount("Shahzad")

    try:
        normal_account.deposit(500)
        normal_account.deposit(0)
    except ValueError as e:
        print(e)

    try:
        normal_account.withdraw(50)
        normal_account.withdraw(1000)
    except ValueError as e:
        print(e)

    balance = normal_account.get_balance()
    print(f"My normal account current balance is {balance}.")

    normal_account.display_history()

    print(normal_account)

    print(f"\n\n{'=' * 80}")
    print("Savings Account")
    print(f"{'=' * 80}\n\n")
    savings_account = SavingsAccount("Ali")

    try:
        savings_account.deposit(10000)
        savings_account.deposit(-1000)
    except ValueError as e:
        print(e)

    savings_account.apply_interest()

    try:
        savings_account.withdraw(100)
        savings_account.withdraw(6000)
    except ValueError as e:
        print(e)

    savings_account.display_history()
    print(savings_account)

    print(f"\n\n{'=' * 80}")
    print("Current Account")
    print(f"{'=' * 80}\n\n")
    current_account = CurrentAccount("Ahmed")

    try:
        current_account.deposit(200)
        current_account.deposit(500)
        current_account.deposit(400)
        current_account.deposit(0)
    except ValueError as e:
        print(e)

    try:
        current_account.withdraw(300)
        current_account.withdraw(600)
        current_account.withdraw(400)
        current_account.withdraw(700)
    except ValueError as e:
        print(e)

    print(f"My current account balance is {current_account.get_balance()}")

    current_account.display_history()

    print(current_account)


if __name__ == "__main__":
    main()
