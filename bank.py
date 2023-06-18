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
    def __init__(self, account_number, balance=0):
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
    def create_user_account(self, account_number, initial_deposit=0):
        return User(account_number, initial_deposit)
