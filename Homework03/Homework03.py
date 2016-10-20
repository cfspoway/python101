# Homework 03

#--------------------------------------
# Part 1: do the math
print("Homework #03, Part 1: do the math")

# step 1: Ask user to provide a number
inputString1 = input('Please input a number: ')
inputString2 = input('Please input another number: ')

# step 2: Computer process the input data
# Convert input string into a real number:
number1 = float(inputString1)
number2 = float(inputString2)

# Real calculation
result1 = number1 + number2
result2 = number1 - number2
result3 = number1 * number2
result4 = number1 / number2

# step 3: Print results to the user
print(str(number1) + ' + ' + str(number2) + ' = ' + str(result1))
print(str(number1) + ' - ' + str(number2) + ' = ' + str(result2))
print(str(number1) + ' * ' + str(number2) + ' = ' + str(result3))
print(str(number1) + ' / ' + str(number2) + ' = ' + str(result4))
print('\n')

#--------------------------------------
# Part 2: area of a triangle
print("Homework #03, Part 2: area of a triangle")

# step 1: Ask user to input edges
inputString2 = input('Please input first edge length: ')
inputString2 = input('Please input second edge length: ')
inputString3 = input('Please input third edge length: ')

# step 2: Computer process the input data
# Convert input string into a real number:
a = float(inputString1)
b = float(inputString2)
c = float(inputString3)
s = (a + b + c) / 2
area = (s * (s - a)*(s - b)*(s - c)) ** 0.5

# step 3: Print the result to user
print('The area of this triangle is:', area)

