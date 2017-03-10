# Initialize a global variable
total = 0

def sum(num1, num2):
    # To change global total, must claim it:
    global total
    # Otherwise total is just a local variable
    total = num1 + num2
    print('Total inside function sum: ', total)

print('global total before sum: ', total)
sum(2, 3)
print('global total after sum: ', total)
