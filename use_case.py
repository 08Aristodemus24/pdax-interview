from uuid import uuid4

from domain import Account, Customer
from infrastructure import AccountRepository, CustomerRepository

class UseCase:
    def __init__(self):
        # we initialize here the "database" of accounts and customers 
        # everytime the application runs in order to create checks and
        # keep track if an account already exists. Should we create an 
        # account initialize account repository to be empty at first
        self.acc_repo = AccountRepository()
        self.cust_repo = CustomerRepository()

    def create_account(self, customer_id: int, name: str, email: str, phone_number: str) -> Account:
        """
        creates a new and returns an Account object.
        customer_id is a primary key so must be unique, not null
        and cannot be duplicated
        name can be duplicated
        email cannot be duplicated
        phone number cannot be duplicated
        """

        # make checks first if customer_id or email or phone number 
        # already exists in customer repo
        all_customers = self.cust_repo.get_all_customers()

        # flags if customer id name, email, and phone number can be permitted
        # to be pushed in customer repo and account repo. Note if customers repo
        # is still empty permit customer and account creation initially 
        cust_permitted = True if len(all_customers) == 0 else False
        acc_permitted = True if len(all_customers) == 0 else False

        # this will loop should there be a customer in the cust repo
        for customer in all_customers:
            if customer.name != name:
                # if a customer with customer id, email, and phone number
                # does not already exist and with a different name create
                # customer and create account
                if customer.customer_id != customer_id and customer.email != email and customer.phone_number != phone_number:
                    cust_permitted = True
                    acc_permitted = True
                else:
                    raise KeyError("Customer and account will not created due to duplicate customer_id, email, or phone number")
                
            else:
                # if a customer with customer id, email, and phone number
                # does not already exist and with a different name create
                # customer and create account
                if customer.customer_id != customer_id and customer.email != email and customer.phone_number != phone_number:
                    cust_permitted = True
                    acc_permitted = True

                # if a customer with same customer id, email, and phone number
                # exists already and with the same name don't create customer
                # but still create account
                elif customer.customer_id == customer_id and customer.email == email and customer.phone_number == phone_number:
                    acc_permitted = True

                else:
                    raise KeyError("Customer and account will not created due to duplicate name, customer_id, email, phone_number")
                
        # should customer information be valid proceed with customer creation
        if cust_permitted:
            # instantiate a customer class
            customer = Customer(
                customer_id=customer_id,
                name=name,
                email=email,
                phone_number=phone_number
            )

            # save customer object
            self.cust_repo.save_customer(customer)
        

        if acc_permitted:
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
        if len(self.acc_repo) == 0:
            raise KeyError("You are attempting to make a transaction without creating yet any account")

        # find account by id
        account = self.acc_repo.find_account_by_id(account_id)
        
        # transaction type
        if transaction_type == "deposit":
            # make deposit
            account.deposit(amount)
        else:
            # make withdrawal transaction
            account.withdraw(amount)

    def generate_account_statements(self, account_id) -> str:
        """
        generates account statements of a customers account, 
        by taking account_id as input and returns a statement
        string containing transaction details for the given account.
        """
        if len(self.acc_repo) == 0:
            raise KeyError("You are attempting to generate an account statement without creating yet any account")

        # find account by id
        account = self.acc_repo.find_account_by_id(account_id)

        # get customer id in the account as the 
        # customer id in the account is a foreign key
        customer_id = account.customer_id
        
        account_num = account.account_num
        balance = account.get_balance()

        # get customer information
        customer = self.cust_repo.find_customer_by_id(customer_id)
        customer_name = customer.name
        customer_email = customer.email
        customer_phone = customer.phone_number

        return f"""
        statement for account {account_id}:
            account number: {account_num}
            name: {customer_name}
            email: {customer_email}
            mobile no.: {customer_phone}

        current balance: {balance}
        """





        


