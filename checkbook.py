
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
4) Exit
        ''')
    # validation for correct input; only numbers (1-4) are acceptable; asks for a number if the wrong input is given
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

# main program that runs the functions
def program():
    user_decision = get_user_input()
    if int(user_decision) == 1: #option 1: check the balance
        with open('current_balance.txt') as f:
            balance = f.readlines()
        transactions = [float(i) for i in balance]
        current_balance = sum(transactions)
        print("Your current balance is ${:0.2f}".format(current_balance))
        new_choice = input('Do you need to do any transactions? ')
        if new_choice == 'Yes':
            program()
        else:
            print('Thank you, come again!')
    if int(user_decision) == 2: #option 2: make a withdraw
        withdraw_amount = input('Please enter amount: ')
        withdraw_transaction('-' + withdraw_amount)
        new_choice = input('Do you need to do another transaction? ')
        if new_choice == 'Yes':
            program()
        else:
            print('Thank you, come again!')

    if int(user_decision) == 3: #option 3: make a deposit
        deposit_amount = input('Please enter amount: ')
        deposit_transaction(deposit_amount)
        new_choice = input('Do you need to do another transaction? ')
        if new_choice == 'Yes':
            program()
        else:
            print('Thank you, come again!')
    if int(user_decision) == 4: #option 4: exit the program
        print('Thank you, come again!')



# history_of_transactions was an attempt to store all the date times of the transactions into a list but this won't work
# history_of_transactions = []


# define function to make a deposit
def deposit_transaction(amount):
    if amount.isdigit():
        with open('current_balance.txt', 'a') as f:
                f.write('\n%s' %str(amount))
                # history_of_transactions.append(amount) #+ now)
        print('You deposited ${} on {}'.format(amount, now.strftime("%m/%d/%Y, %H:%M:%S")))
        # print(history_of_transactions)
    else:
        print('Error! "' + amount + '" is not a valid option.\nPlease type a number.')
        
# create function to run withdraws
def withdraw_transaction(amount):
        with open('current_balance.txt', 'a') as f:
                f.write('\n%s' %str(amount))
                # history_of_transactions.append(str(amount) + str(datetime.datetime.now()))
                if amount.isdigit():
                    print('Error! "' + amount + '" is not a valid option.\nPlease type a number.')

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

