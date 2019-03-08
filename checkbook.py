
from json import load

with open('current_balance.txt') as f:
    balance = f.read()


def validate_user_input(user_decision):
    while not user_decision.isdigit() or int(user_decision) > 5 or input(user_decision) < 1:
        return user_decision
    else:
        user_decision = input('What would you like to do? \n')


def program(user_decision):
    if user_decision == 1:
        print('Your current balance is $' + balance + '.')
    # elif user_decision == 2:
    #
    # elif user_decision == 3:

    else:
        print('End program')













































transactions = []

# create function to run credit (addition/deposit)
def calculate_transaction(amount):
    # if user_decision == 3:
        with open('current_balance.txt', 'a') as f:
                f.write(str(amount))
                # transactions.append()

calculate_transaction(200)


# create function to run debit (subtraction/withdrawl)










# --------~~~~~~~~~~ADDITIONAL FEATURES~~~~~~~~~~--------

historical_dates_times = []
print('\n~~~ Welcome to your terminal checkbook! ~~~')

user_decision = int(input('''
    What would you like to do? \n
    1) View current balance\n
    2) Add a debit (withdrawal)\n
    3) Add a credit (deposit)\n
    4) Exit \n 
    '''))


program(user_decision)
