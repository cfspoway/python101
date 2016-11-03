# Class note: 2016-11-03

import sys

#step 1: get input string and convert it to real number
num1 = float(input('Please input a number: '))
num2 = float(input('Please input another number: '))

# Calulate num1 / num2
if (num2 != 0) :
    # Only execuated when if comparison is True
    # Note the way that we use print command
    print(str(num1) + '/' + str(num2) + ' is ' + str(num1/num2))
else:
    # Only execuated when if comparison is False
    print('denumenator has to be non-zero')
    # Program will exit
    sys.exit(1)

# Out of if-else, program continues
print('Program completed')

