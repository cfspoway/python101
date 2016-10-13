# Ask for input of a number
# Give an output of number * 999

# step 1: Ask user to provide a number
inputString = input('Please give a number: ')

# step 2: Computer process the input data
# Convert input string into a real number:
number = float(inputString)
# Computer does the math:
result = number * 999

# step 3: Provide the result to the user
print(str(number) + ' * 999 = ' + str(result))

