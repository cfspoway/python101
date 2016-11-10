# Class note 2016-11-10
# Continue to practice if-else

# Prepare to start the program
import sys

myUserName = 'Gang'
myPassword = 'pass'

userName = input('Please input user name: ')
passWord = input('Please input password: ')

# Validate user
if (userName == myUserName) and (passWord == myPassword):
    print('Welcome ' + userName)
else:
    # When will we come here?
    # (userName != myUserName) or (passWord != myPassword)
    if (userName == 'Mom'):
        print('Welcome Mom')
    else:
        # When will we come here?
        # ((userName != myUserName) or (passWord != myPassword)) and (userName != 'Mom')
        if (userName == 'Friend'):
            print('Welcome Friend')
        else:
            # When will we come here?
            # ((userName != myUserName) or (passWord != myPassword)) and (userName != 'Mom') and (userName != 'Friend')
            print('Wrong username or password, please try again')
            sys.exit(1)

# Do something for the appropriate user
num1 = float(input('Please input a number: '))
num2 = float(input('Please input another number: '))
if (num1 > num2) :
    print(str(num1) + ' is larger than ' + str(num2))
else:
    if (num1 < num2):
        print(str(num2) + ' is larger than ' + str(num1))
    else:
        print(str(num1) + ' is equal to ' + str(num2))

# Prepare to finish the program
print('Program is done')
