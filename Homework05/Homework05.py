# Homework #05

# Part 1
print('99 != 99 is ' + str(99 != 99))
print('not (100 > 101) is ' + str(not (100 > 101)))
print('9**2 >= (100-15) is ' + str(9**2 >= (100-15)))
print('(100 > 101) or (not (100 >= 101)) is' + str((100 > 101) or (not (100 >= 101))))
print("not 'Alice' == 'Alice' is " + str(not 'Alice' == 'Alice'))
print("'Alice' == 'Alice' and 'Jack' != 'jack' is " + str('Alice' == 'Alice' and 'Jack' != 'jack'))
print('True and True is ' + str(True and True))
print('True and False is ' + str(True and False))
print('False and True is ' + str(False and True))
print('False and False is ' + str(False and False))
print('True or True is ' + str(True and True))
print('True or False is ' + str(True and False))
print('False or True is ' + str(False or True))
print('False or False is ' + str(False or False))
print('not True is ' + str(not True))
print('not False is ' + str(not False))

# Part 2: compare two numbers
# Get input string and convert it to real number
num1 = float(input('Please input a number: '))
num2 = float(input('Please input another number: '))

# Compare num1 and num2
if (num1 > num2) :
    print(str(num1) + ' is larger than ' + str(num2))
else:
    if (num1 < num2):
        print(str(num2) + ' is larger than ' + str(num1))
    else:
        print(str(num1) + ' is equal to ' + str(num2))

# Another way of doing this        
if (num1 > num2) :
    print(str(num1) + ' is larger than ' + str(num2))
elif (num1 < num2):
    print(str(num2) + ' is larger than ' + str(num1))
else:
    print(str(num1) + ' is equal to ' + str(num2))
    
print("This is the end of the program")
