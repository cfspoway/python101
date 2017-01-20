# Fabonacci sequence

num1 = 0
num2 = 1
print(str(num1) + '\n' + str(num2))
maxnum = 1000
count = 2
while num2 <= maxnum:
   num3 = num1 + num2
   print(str(num3))
   count = count + 1
   num1 = num2
   num2 = num3
    
print('There are ' + str(count) + ' Fabonacci numbers before ' + str(maxnum))
