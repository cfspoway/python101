import random

def sum3dice(startnumber, maxnumber):
    if startnumber > maxnumber:
        print('function sum3dice input is wrong')
        return -1
    x1 = random.randint(startnumber, maxnumber)
    x2 = random.randint(startnumber, maxnumber)
    x3 = random.randint(startnumber, maxnumber)
    sum = x1 + x2 + x3
    return sum

maxn = 100
count = 0
i = 0
while i < maxn:
    sum1 = sum3dice(1, 4)
    sum2 = sum3dice(2, 5)
    sum3 = sum3dice(1, 3)
    if sum1 > sum2:
        count = count + 1
    i = i + 1
print(count)
