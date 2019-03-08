
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
        transactions = [float(i) for i in balance]
        current_balance = sum(transactions)
        print("Your balance is ${:0.2f}".format(current_balance))
        new_choice = input('Do you need to do any transactions? ')
        if new_choice == 'Yes':
            program()
        else:
            print('Thank you, come again!')
    if int(user_decision) == 4:
        print('Thank you, come again!')








print('\n~~~ Welcome to your terminal checkbook! ~~~')

program()



