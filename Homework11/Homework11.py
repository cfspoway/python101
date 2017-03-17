# Homework #11
# Banking

balance = 0

def printbalance():
    global balance
    print('Current balance = ' + str(balance))
    
def deposit(money):
    global balance
    balance += money     # same as: balance = balance + money
    print('Deposit: ' + str(money))
    
def withdraw(money):
    global balance
    actualmoney = money
    if (balance >= money):
        balance -= money
    else:
        printbalance()
        print('Not enough balance to withdraw ' + str(money) + \
              ', so only withdraw ' + str(balance))
        actualmoney = balance
        balance = 0
    print('Withdraw: ' + str(actualmoney))

while True:
    printbalance()
    userinput = ''
    while userinput != 'deposit' and userinput != 'withdraw' and userinput != 'exit':
        userinput = input('Please choose deposit or withraw: ')
    if userinput == 'exit':
        print('Thank you, bye')
        break
    money = 0
    while money <=0:
        money = int(input('Please input the amount of money to ' + userinput + ': '))
    if userinput == 'deposit':
        deposit(money)
    else:
        withdraw(money)

