# App usage:
* initial prompt will be to enter task you want to do this can either be making an account, depositing or withdrawing to and from an existing account, and generating an account statement from an existing account
* if you want to create an account enter your unique customer id, name, email, and phone number. Note there can be cases where a customer can have multiple accounts. The ff. are other cases that are accepted when creating an account (order follows customer id, name, email, and phone number respectively):
- if (1, larry, test@gmail.com, 0998) already exists and (1, larry, test@gmail.com, 0998) is entered, this will not be permitted in creating a customer but will be permitted in creating an account with a different account id
- if (1, larry, test@gmail.com, 0998) already exists and (2, joe, test@gmail.com, 0970) is entered, this will not be permitted in creating a customer and in creating an account due to duplicate emails in the customers repository
- however (if 1, larry, test@gmail.com, 0998) already exists and (2, joe, test2@gmail.com, 0970) is entered since customer id, email, and phone number is unique regardless of the name this will be permitted in customer and account creation 
- if (1, larry, test@gmail.com, 0998) already exists and (2, larry, test2@gmail.com, 0970) is entered, this may seem that this will not be permitted in creating a customer and in creating an account due but because customer id, email, and phone number is unique, even with the same name this can be permitted in customer creation and in account creation\

# File structure:
```
|- utilities
    |- __init__.py
    |- utils.py
|- domain.py
|- use_case.py
|- infrastructure.py
|- main.py
|- .env
|- .gitignore
|- upload_changes.sh
|- Python Backend Exam.pdf
|- readme.md
```