from uuid import uuid4

from domain import Account, Customer
from infrastructure import AccountRepository

class UseCase:
    def __init__(self, acc_repo):
        # we pass here the "database" everytime the application runs
        # in order to create checks if an account already exists should
        # we create an account
        self.acc_repo = acc_repo

    def create_account(self, customer_id: int, name: str, email: str, phone_number: str) -> Account:
        """
        creates a new and returns an Account object.
        customer_id is a primary key so must be unique, not null
        and cannot be duplicated
        name can be duplicated
        email cannot be duplicated
        phone number can be duplicated
        """

        # instantiate a customer class
        customer = Customer(
            customer_id=customer_id,
            name=name,
            email=email,
            phone_number=phone_number
        )

        # get all accounts of customer through their customer id
        customer_accounts = self.acc_repo.find_accounts_by_customer_id(customer_id)
        all_accounts = self.acc_repo.get_all_accounts()

        # base case is if a customers accounts is empty then set account_num to 1
        if len(customer_accounts) == 0:
            # instantiate Account class
            # make checks first if customer id exists before making account
            # Generate a unique account ID using UUID
            account_id = str(uuid4())
            account_num = 1
        else:
            # this ensures that when the account is created that 
            # it is the maximum plus 1 making it a unique value for the
            # customer
            account_num = max(customer_accounts, key=lambda account: account.account_num).account_num + 1

            while True:
                # if generated account id is still in all accounts of all 
                # customers keep retrying until generated account id is unique
                account_id = str(uuid4())

                # if self.acc_repo.accounts already contains some accounts then only check if 
                # account_id and account_num is unique, if comprehension finds at least one duplicate
                # then the account_num is auto incremented
                if not (len([account for account in all_accounts if account.account_id == account_id]) > 0):
                    break
        
        # a customer can have multiple accounts, these 
        # multiple accounts mmust have unique acc id, and 
        # acc num for a specific user
        account = Account(
            account_id=account_id,
            customer_id=customer.customer_id,
            account_num=account_num)

        return account

    def make_transaction(self, account_id: str, amount: float, transaction_type: str):
        """
        makes a transaction by taking account_id, amount, and 
        transaction_type as input and updates the account 
        balance accordingly
        """

        account_index, account = self.acc_repo.find_account_by_id(account_id)
        
        # make deposit
        if transaction_type == "deposit":
            print(account)
            account.deposit(amount)
            print(account)
            self.acc_repo[account_index] = account

        # make withdrawal transaction
        account.withdraw(amount)
        self.acc_repo[account_index] = account

        print(self.acc_repo)

    def generate_account_statements(self, account_id) -> str:
        """
        generates account statements of a customers account, 
        by taking account_id as input and returns a statement
        string containing transaction details for the given account.
        """


