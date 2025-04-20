class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder  # public attribute
        self._account_type = "Checking"  # protected attribute
        self.__balance = initial_balance  # private attribute

    def get_balance(self):  # return privat attribute
        return self.__balance

    def set_balance(self, new_balance):  # changes privat attribute
        self.__balance = new_balance


new_bank_account = BankAccount("Seth Palmer", 1000)
new_bank_account.get_balance()
new_bank_account.set_balance(1500)
new_bank_account.get_balance()
