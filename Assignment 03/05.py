class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = int(input("Enter the account number (Ex: 123456789): "))
        self.name = input("Enter the account holder name: ")
        self.balance = int(input("Enter the opening balance: "))
    def Deposit(self, amount):
        self.balance += amount

    def Withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def bankFees(self):
        self.balance -= self.balance * 0.05

    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Holder: {self.name}")
        print(f"Account Balance: {self.balance}")

account = BankAccount(123456789, "John Doe", 10000)

account.display()

account.Deposit(5000)
account.Withdrawal(2000)
account.bankFees()

print("Updated with 5 percent bank fees")
account.display()