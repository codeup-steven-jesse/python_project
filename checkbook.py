
from json import load

with open('current_balance.txt') as f:
    balance = f.read()



def get_user_input():
    user_decision = input('''
What would you like to do? \n
1) View current balance
2) Add a debit (withdrawal)
3) Add a credit (deposit)
4) Exit
        ''')

    while not user_decision.isdigit() or int(user_decision) > 4 or int(user_decision) < 1:
        print('Error! "' + user_decision + '" is not a valid option.\nPlease pick a valid number from the list.')
        user_decision = input('''
What would you like to do? \n
1) View current balance
2) Add a debit (withdrawal)
3) Add a credit (deposit)
4) Exit\n
        ''')
    return user_decision





def program():
    user_decision = get_user_input()
    if int(user_decision) == 1:
        print('Your balance is $' + balance)
        new_choice = input('Do you need to do any transactions? ')
        if new_choice == 'Yes':
            program()
        else:
            print('Thank you, come again!')
    if int(user_decision) == 4:
        print('Thank you, come again!')




# create function to run credit (addition/deposit)
def calculate_transaction(amount):
    # if user_decision == 3:
        with open('current_balance.txt', 'a') as f:
                f.write(str(amount),'\n')
                # transactions.append()






































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


print('\n~~~ Welcome to your terminal checkbook! ~~~')


program()