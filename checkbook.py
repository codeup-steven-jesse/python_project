
import json
from datetime import datetime as dt
now = dt.now()

with open('current_balance.txt') as f:
    balance = f.readlines()

# prompt user to make a choice between view, deposit, withdraw or exit
def get_user_input():
    user_decision = input('''
What would you like to do? \n
1) View current balance
2) Add a debit (withdrawal)
3) Add a credit (deposit)
4) Check transaction history
5) Exit\n
Select an option number:   \n''')

    while not user_decision.isdigit() or int(user_decision) > 5 or int(user_decision) < 1:
        print('Error! "' + user_decision + '" is not a valid option.\nPlease pick a valid number from the list.')
        user_decision = input('''
What would you like to do? \n
1) View current balance
2) Add a debit (withdrawal)
3) Add a credit (deposit)
4) Check transaction history
5) Exit\n
        ''')
    return user_decision

#prompts user for a decision during the course of the session

def new_action():
    new_choice = input('Do you need to do another action? (Yes or No) \n').lower()
    if new_choice == 'yes' or new_choice == 'y':
        program()
    else:
        print('Thank you, come again!')

# define function to make a deposit
def deposit_transaction(amount):
    if amount[:-3].isdigit():
        with open('current_balance.txt', 'a') as f:
                f.write('\n%s' %str(amount))
                # history_of_transactions.append(amount) #+ now)
        print('You deposited ${} on {}'.format(amount, now.strftime("%m/%d/%Y, %H:%M:%S")))
        # print(history_of_transactions)
    else:
        print('Error! "' + amount + '" is not a valid option.\nPlease type a number.')

# define function to make a withdraw
def withdraw_transaction(amount):
    if amount[1:-3].isdigit():    
        with open('current_balance.txt', 'a') as f:
                f.write('\n%s' %str(amount))
                # history_of_transactions.append(str(amount) + str(datetime.datetime.now()))
        print('You withdrew ${} on {}'.format(amount[1:], now.strftime("%m/%d/%Y, %H:%M:%S")))
    else:
        print('Error! "' + amount[1:] + '" is not a valid option.\nPlease type a number.')

# def withdraw_transaction(amount):
#     verify_withdraw(amount)
#     with open('current_balance.txt', 'a') as f:
#         f.write('\n%s' % str(amount))


# def verify_withdraw(amount):
#     amount = str(amount)
#     amount = amount.replace('.','')
#     amount = amount.replace('-','')
#     while not amount.isdigit():
#         print('Error! "' + amount + '" is not a valid number.')
#         amount = input('Please enter a valid number: ')
#     return amount


# def deposit_transaction(amount):
#     verify_deposit(amount)
#     with open('current_balance.txt', 'a') as f:
#         f.write('\n%s' % str(amount))


# def verify_deposit(amount):
#     amount = str(amount)
#     amount = amount.replace('.','')
#     while not amount.isdigit():
#         print('Error! "' + amount + '" is not a valid number.')
#         amount = input('Please enter a valid number: ')
#     return amount


# define function to show the transaction history
def transaction_history():
    with open('current_balance.txt') as f:
        list_of_transactions = f.read()
    print(list_of_transactions)


# main program that runs the functions
def program():
    user_decision = get_user_input()
    if int(user_decision) == 1: #option 1: check the balance
        with open('current_balance.txt') as f:
            balance = f.readlines()
        transactions = [float(i) for i in balance]
        current_balance = sum(transactions)
        print("Your current balance is ${:0.2f}".format(current_balance))
        new_action()

    if int(user_decision) == 2: #option 2: make a withdraw
        withdraw_amount = input('Please enter the amount you wish to withdraw:\n$')
        withdraw_transaction('-' + withdraw_amount)
        new_action()

    if int(user_decision) == 3: #option 3: make a deposit
        deposit_amount = input('Please enter amount you wish to deposit:\n$')
        deposit_transaction(deposit_amount)
        new_action()

    if int(user_decision) == 4: #option 4: see history of transactions
        print('Here is a list of all your transactions: \n')
        transaction_history()
        print('')
        new_action()

    if int(user_decision) == 5: #option 5: exit the program
        print('Thank you, come again!')


# history_of_transactions = []

# history_of_transactions was an attempt to store all the date times of the transactions into a list but this won't work
# becaues it will only keep a history of the transactions done in a single session.


print('\n~~~ Welcome to your terminal checkbook! ~~~')

program()



# --------~~~~~~~~~~ADDITIONAL FEATURES~~~~~~~~~~--------










# create function to run deposits
# def deposit_transaction(amount):
#     # if user_decision == 3:
#         with open('current_balance.txt', 'a') as f:
#                 f.write('\n%s' %str(amount))
#                 # history_of_transactions.append(amount)
#                 if not amount.isdigit():
#                     print('Error! "' + amount + '" is not a valid option.\nPlease type a number.')

# create function to run withdraws

# def withdraw_transaction(amount):
#     # if user_decision == 3:
#     withdraw_amount_function = amount * -1    
#     with open('current_balance.txt', 'a') as f:
#         f.write('\n%s' %str(withdraw_amount_function))
#                 # history_of_transactions.append(amount)
#         if not amount.isdigit():
#             print('Error! "' + amount + '" is not a valid option.\nPlease type a number.')

