
import json

with open('current_balance.txt') as f:
    balance = f.readlines()



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

def new_action():
    new_choice = input('Do you need to do another action? (Yes or No) \n').lower()
    if new_choice == 'yes' or new_choice == 'y':
        program()
    else:
            print('Thank you, come again!')

def deposit_transaction(amount):
    # if user_decision == 3:
        with open('current_balance.txt', 'a') as f:
                f.write('\n%s' %str(amount))
                # transactions.append(amount)
                if not amount.isdigit():
                    print('Error! "' + amount + '" is not a valid option.\nPlease type a number.')


def withdraw_transaction(amount):
    with open('current_balance.txt', 'a') as f:
        f.write('\n%s' % str(amount))
        if amount.isdigit():
            print('Error! "' + amount + '" is not a valid option.\nPlease type a number.')

def transaction_history():
    with open('current_balance.txt') as f:
        list_of_transactions = f.read()
    print(list_of_transactions)


def program():
    user_decision = get_user_input()
    if int(user_decision) == 1:
        with open('current_balance.txt') as f:
            balance = f.readlines()
        transactions = [float(i) for i in balance]
        current_balance = sum(transactions)
        print("Your balance is ${:0.2f}\n".format(current_balance))
        new_action()

    if int(user_decision) == 2:
        withdraw_amount = input('Please enter the amount you withdrew: $\n')
        withdraw_transaction('-' + withdraw_amount)
        new_action()

    if int(user_decision) == 3:
        deposit_amount = input('Please enter amount you deposited: $\n')
        deposit_transaction(deposit_amount)
        new_action()

    if int(user_decision) == 4:
        print('Here is a list of all your transactions: \n')
        transaction_history()
        new_action()


    if int(user_decision) == 5:
        print('Thank you, come again!')



print('\n~~~ Welcome to your terminal checkbook! ~~~')

program()




