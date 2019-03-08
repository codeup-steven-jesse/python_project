
import json

with open('current_balance.txt') as f:
    balance = f.readlines()



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

        print('Your balance is $' )
        new_choice = input('Do you need to do any transactions? ')
        if new_choice == 'Yes':
            program()
        else:
            print('Thank you, come again!')
    
    if int(user_decision) == 3:
        deposit_amount = input('Please enter amount: ')
        deposit_transaction(deposit_amount)
        new_choice = input('Do you need to do another transaction? ')
        if new_choice == 'Yes':
            program()
        else:
            print('Thank you, come again!')
    if int(user_decision) == 4:
        print('Thank you, come again!')



#create a function to handle numerical calculations

# def calculator():


# create function to run credit (addition/deposit)
def deposit_transaction(amount):
    # if user_decision == 3:
        with open('current_balance.txt', 'a') as f:
                f.write('\n%s' %str(amount))
                # transactions.append(amount)
                if not amount.isdigit():
                    print('Error! "' + amount + '" is not a valid option.\nPlease type a number.')
        


# deposit_transaction(200)





transactions = []

# create function to run deposits
# def deposit_transaction(amount):
#     # if user_decision == 3:
#         with open('current_balance.txt', 'a') as f:
#                 f.write('\n%s' %str(amount))
#                 # transactions.append(amount)
#                 if not amount.isdigit():
#                     print('Error! "' + amount + '" is not a valid option.\nPlease type a number.')




# create function to run withdraws


def withdraw_transaction(amount):
    # if user_decision == 3:
        with open('current_balance.txt', 'a') as f:
                f.write('\n%s' %str(amount))
                # transactions.append(amount)
                if not amount.isdigit():
                    print('Error! "' + amount + '" is not a valid option.\nPlease type a number.')







# --------~~~~~~~~~~ADDITIONAL FEATURES~~~~~~~~~~--------

historical_dates_times = []
print('\n~~~ Welcome to your terminal checkbook! ~~~')


program()