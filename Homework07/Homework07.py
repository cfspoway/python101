# Homework #7

import sys

# Part 1: sort three numbers from the largest to the smallest
# Get input string and convert it to real number
a = float(input('Please input a: '))
b = float(input('Please input b: '))
c = float(input('Please input c: '))

if (a > b) :
    if (a > c):
        # a > b and a > c
        if (b > c):
            # a > b > c
            print(str(a) + ', ' + str(b) + ', ' + str(c))
        else:
            # a > c >= b
            print(str(a) + ', ' + str(c) + ', ' + str(b))
    else:
        # c >= a > b
        print(str(c) + ', ' + str(a) + ', ' + str(b))
else:
    # b >= a
    if (c > b):
        # c > b >= a
        print(str(c) + ', ' + str(b) + ', ' + str(a))
    else:
        # b >= a and b >= c
        if (a > c):
            # b >= a > c
            print(str(b) + ', ' + str(a) + ', ' + str(c))
        else:
            # b >= c >= a
            print(str(b) + ', ' + str(c) + ', ' + str(a))

           
# Part 2: leap year
year = int(input('\nPlease input a year number: '))

if year <= 0:
    print("Year number must be positive")
    sys.exit(1)
    
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a leap year.")
        else:
            print(str(year) + " is not a leap year.")
    else:
        print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")
