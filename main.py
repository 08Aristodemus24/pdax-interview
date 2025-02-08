from use_case import UseCase
from infrastructure import AccountRepository, CustomerRepository
import ast   
from argparse import ArgumentParser

def run_app():
    
    # while is_running is true app will keep running
    is_running = True

    # instantiate use case object as well so that as user
    # keeps on making transactions the use case account repository
    # is also updated
    use_case = UseCase()

    while is_running:
        try:
            # prompt user what task they would want to do
            task = int(input("\nwhat would you like to accomplish?\n0 to create account\n1 to make transaction\n2 to generate account statements\nanswer: "))
            
            if task == 0:
                # if a user decides to create an account for given
                # a customer id
                customer_id = int(input("\nenter your customer_id (any number): "))
                name = input("enter your name (larry): ")
                email = input("enter your email (michaelaveuc571@gmail.com): ")
                phone_number = input("enter your phone number (09938238207): ")

                # create account 
                # if no account is reated account will be None
                account = use_case.create_account(customer_id, name, email, phone_number)

                if account != None:
                    # save newly created account
                    use_case.acc_repo.save_account(account)
                    
                print(use_case.acc_repo)

            elif task == 1:
                # if a user decides to make a transactions
                account_id = input("\nenter your account_id (your account id): ")
                amount = float(input("enter the amount for your transaction (100.00): "))
                transaction_type = input("enter transaction type (deposit|withdraw): ")

                # make transaction
                # note that after transaction the  
                use_case.make_transaction(account_id, amount, transaction_type)

                print(use_case.acc_repo)

            elif task == 2:
                # if user decides to generate an accounts statement
                account_id = input("\nenter your account_id (your account id): ")

                # geneerate account statement
                statement = use_case.generate_account_statements(account_id)

                # print statement
                print(statement)

            is_running = False if input("\nwould you like to end transaction (yes|no)? ") == "yes" else True
        except ValueError as e:
            print(f"\nError {e} occured.\n")

        except KeyError as e:
            print(f"\nError {e} occured.\n")


if __name__ == "__main__":
    # run app
    run_app()

    

