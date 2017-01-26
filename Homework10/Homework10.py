import random

maxn = 1000000
count = 0
i = 0
while i < maxn:
    x1 = random.randint(1,6)
    x2 = random.randint(1,6)
    x3 = random.randint(1,6)
    sum = x1 + x2 + x3
    if sum >= 10:
        count = count + 1
    i = i + 1
print(str(count/maxn*100) + '% out of ' + str(maxn) + ' is combined at least 10')
