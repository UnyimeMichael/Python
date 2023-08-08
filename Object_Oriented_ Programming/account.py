from decimal import Decimal


class Account:
    def __init__(self, name: str, balance: Decimal):  # contructor
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    # def get_balance(self)
    #     return self.balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("balance cannot be negative")
        self.__balance = amount

    # def set_balance(self, amount):
    #     if amount < 0:
    #         raise ValueError("balance cannot be negative")
    #     self.balance = amount

    def __str__(self):
        return f"{self.name} {self.balance}"

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("You want to scam us")
        self.balance -= amount


# account1 = Account("mariam", Decimal(100.00))
# account1.withdraw(200)
# print(account1)
