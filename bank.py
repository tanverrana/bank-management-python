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
