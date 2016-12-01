# Class note 2016-12-01

# Loop
sum = 0
maxnumber = 100
num = 1
while num <= maxnumber:
    # inside the loop
    # print('I am in the loop:' + str(num))
    if num == 50:
        num = num + 1
        continue
    if num > 90:
        break
    sum = sum + num
    num = num + 1
print('the summation is: ' + str(sum))    

import sys

myUserName = 'Gang'
myPassword = 'pass'

maxtry = 3
count = 0

while True:
    userName = input('Please input user name: ')
    passWord = input('Please input password: ')
    
    count = count + 1
    if count > maxtry:
        print('You are trying so many times')
        sys.exit(1)

    # Validate user
    if (userName == myUserName) and (passWord == myPassword):
        print('Welcome ' + userName)
        break
    else:
        # When will we come here?
        # (userName != myUserName) or (passWord != myPassword)
        if (userName == 'Mom'):
            print('Welcome Mom')
            break
        else:
            # When will we come here?
            # ((userName != myUserName) or (passWord != myPassword)) and (userName != 'Mom')
            if (userName == 'Friend'):
                print('Welcome Friend')
                break
            else:
                # When will we come here?
                # ((userName != myUserName) or (passWord != myPassword)) and (userName != 'Mom') and (userName != 'Friend')
                print('Wrong username or password, please try again')
                

# Do something for the appropriate user
print('\n')
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
