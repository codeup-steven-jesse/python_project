
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

    while not user_decision.isdigit() or int(user_decision) > 5 or int(user_decision) < 1:
        print('Error! Please pick a valid option number.')
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
        print(balance)
    else:
        print('End program')







print('\n~~~ Welcome to your terminal checkbook! ~~~')


program()