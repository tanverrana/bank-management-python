class Bank:
    bank_balance = 0
    total_loan_amount = 0
    loan_feature_enabled = True

    @staticmethod
    def check_bank_balance():
        return Bank.bank_balance

    @staticmethod
    def check_total_loan_amount():
        return Bank.total_loan_amount


class User:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        Bank.bank_balance += amount
        self.transaction_history.append(f'Deposited amount: {amount}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            Bank.bank_balance -= amount
            self.transaction_history.append(f'Withdrew amount: {amount}')
        else:
            print("Insufficient funds! So please keep dollar in your own account")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(
                f'Transferred {amount} to account {recipient.account_number}')
            recipient.transaction_history.append(
                f'Received {amount} from account {self.account_number}')
        else:
            print("Insufficient funds!")

    def check_balance(self):
        return self.balance

    def take_loan(self):
        if Bank.loan_feature_enabled:
            loan_limit = self.balance * 2
            if Bank.total_loan_amount < loan_limit:
                self.balance += self.balance
                Bank.bank_balance += self.balance
                self.transaction_history.append(
                    f'Took a loan of amount: {self.balance}')
                Bank.total_loan_amount += self.balance
            else:
                print("Loan limit crossed!")
        else:
            print("The loan feature is currently disabled.So waiting...")

    def check_transaction_history(self):
        return self.transaction_history


class Admin:
    def create_user_account(self, name, account_number, initial_deposit=0):
        return User(name, account_number, initial_deposit)

    @staticmethod
    def check_bank_balance():
        return Bank.check_bank_balance()

    @staticmethod
    def check_total_loan_amount():
        return Bank.check_total_loan_amount()

    @staticmethod
    def loan_feature_on():
        Bank.loan_feature_enabled = True
        print("Loan feature On.")

    @staticmethod
    def loan_feature_off():
        Bank.loan_feature_enabled = False
        print("Loan feature off.")


admin = Admin()
user1 = admin.create_user_account('Tanver Rana', 101, initial_deposit=15000)
user2 = admin.create_user_account('Abdur Sobur', 102, initial_deposit=12000)
print('_______User Details__________')
print("Name:", user1.name, '->', "Account Number:", user1.account_number)
print("Name:", user2.name, '->', "Account Number:", user2.account_number)

user1.deposit(5000)
user2.deposit(10000)
print("_________After Deposit_________")
print(user1.name, "balance: ", user1.check_balance())
print(user2.name, "balance: ", user2.check_balance())
user1.withdraw(2000)
user2.withdraw(5000)
print("_________After Withdraw__________")
print(user1.name, "balance: ", user1.check_balance())
print(user2.name, "balance: ", user2.check_balance())

user2.transfer(user1, 4000)
print("_________After Transfer__________")
print("Send", user2.name, "and received ", user1.name)
print(user1.name, "balance: ", user1.check_balance())
print(user2.name, "balance: ", user2.check_balance())
