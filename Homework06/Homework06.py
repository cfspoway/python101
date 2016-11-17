# Homework #6

import sys

# Part 1: area of a triangle
print('Part 1:')
a = float(input('Please input first edge length: '))
b = float(input('Please input second edge length: '))
c = float(input('Please input third edge length: '))

# Check if inputs are valid
if a <= 0 or b <= 0 or c <= 0:
    print('edge length must be positive')
    sys.exit(1)

if (a+b) < c or (b+c) < a or (a+c) < b:
    print('Input is not valid for a triangle')
    sys.exit(1)

# Now the inputs are valid for a triangle
s = (a + b + c) / 2
area = (s * (s - a)*(s - b)*(s - c)) ** 0.5

# step 3: Print the result to user
print('The area of this triangle is:', area)


# Part 2: find the largest number of 3
# Get input string and convert it to real number
print('\nPart 2:')
a = float(input('Please input a: '))
b = float(input('Please input b: '))
c = float(input('Please input c: '))

if a > b and a > c:
    print('The largest number is a ' + str(a))
elif b > a and b > c:
    print('The largest number is b ' + str(b))
elif c > a and c > b:
    print('The largest number is c ' + str(c))
elif a == b and b > c:
    print('The largest numbers are a ' + str(a) + ' and b ' + str(b))
elif b == c and c > a:
    print('The largest numbers are b ' + str(b) + ' and c ' + str(c))
elif a == c and c > b:
    print('The largest numbers are a ' + str(a) + ' and c ' + str(c))
else:
    print('All three numbers are equal')
