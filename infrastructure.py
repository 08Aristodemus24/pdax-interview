# import pandas as pd

class AccountRepository:
    """
    a class for persisting and
    retrieving account data. 
    """

    def __init__(self):
        self.accounts = [
            # dictionary representation of the account object
            # {"account_id": <some num>, "customer_id": <some num>, "account_num": <some num>, "balance": <some num>}
        ]

    def save_account(self, account):
        """
        saves an account given the Account object
        """

        self.accounts.append(account)

    def find_account_by_id(self, account_id: str):
        """
        retrieves an account through the account id
        """

        matches = [i for i, account in enumerate(self.accounts) if account.account_id == account_id]
        if len(matches) == 0:
            raise KeyError("You are attempting to generate an account statement with a non-existent account id") 
        
        account_index = matches[-1]
        return self.accounts[account_index]

    def find_accounts_by_customer_id(self, customer_id) -> list:
        """
        get all accounts of customer through their customer id
        """
        
        customer_accounts = [account for account in self.accounts if account.customer_id == customer_id]
        return customer_accounts

    def get_all_accounts(self):
        return self.accounts

    def __len__(self):
        return len(self.accounts)
    
    def __getitem__(self, key):
        return self.accounts[key]
    
    def __setitem__(self, key, value):
        self.accounts[key] = value

    def __repr__(self):
        accounts_str = "\n".join([str(account.__dict__) for account in self.accounts])
        log = f"\ncurrent accounts: \n{accounts_str}"
        return log

class CustomerRepository:
    def __init__(self):
        self.customers = []

    def save_customer(self, customer):
        """
        saves a customer given the Customer object
        """

        self.customers.append(customer)

    def find_customer_by_id(self, customer_id: int):
        """
        retrieves a customer through the customer id
        """

        matches = [i for i, customer in enumerate(self.customers) if customer.customer_id == customer_id]
        customer_index = matches[-1]

        return self.customers[customer_index]
    
    def get_all_customers(self):
        return self.customers
    
    def __len__(self):
        return len(self.customers)
    
    def __getitem__(self, key):
        return self.customers[key]
    
    def __setitem__(self, key, value):
        self.customers[key] = value

    def __repr__(self):
        customers_str = "\n".join([str(customer.__dict__) for customer in self.customers])
        log = f"\ncurrent customers: \n{customers_str}"
        return log