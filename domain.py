class Account:
    def __init__(self, account_id: str, customer_id: int, account_num: int, balance: float=0.0):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_num = account_num

        # note initially the balance will be 0.0 when customer creates account
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance
    
    def __repr__(self):
        return f"account {self.account_id} balance: {self.balance}"


class Customer:
    def __init__(self, customer_id: int, name: str, email: str, phone_number: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number



