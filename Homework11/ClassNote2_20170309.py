# Multiple function definitions
# How to return from a function

def sum(num1, num2):
    t = num1 + num2
    return t

def calc(num1, num2):
    t1 = sum(num1, num2)
    t2 = num1 - num2
    return t1, t2

add, sub = calc(2, 3)
print('Addition=', str(add), \
      ', Substraction=', str(sub))
