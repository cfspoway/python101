# All sample answers to Homework #8 can be found at:
# https://github.com/cfspoway/python101/tree/master/Homework08

# Sample answer to Homework #8 part 2
# Prime numbers
pNum = 2
numAm = 0
while pNum < 1000:
    div = 2
    while div <= pNum - 1:
        if (pNum % div == 0):
            # pNum is not a prime number
            break
        # remainder is non-zero
        div = div + 1
    # outside internal loop
    # 2 possibilities:
    # number 1: div > pNum -1
    if div > pNum -1:
        # This is a prime
        print(pNum)
        numAm = numAm + 1
    # number 2: because of break, not prime
    # do nothing if it is not prime    
    pNum = pNum + 1
# outside the external while loop
print('The number of prime numbers is: ' + str(numAm))

# Random number
import random
c=0
while c<10:
    # get a random integer number between 0 and 1
    x = random.randint(0,1)
    if x==0:
        print('Head')
    else:
        print('Tail')
    c=c+1

