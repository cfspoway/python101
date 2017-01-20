# Prime number

num = 2
count = 0
while num <= 1000:
   i = 2
   while i < num:
       if (num % i) == 0:
           # print(str(num) + " is not a prime number")
           break
       i = i + 1

   if i >= num:
       print(str(num) + " is a prime number")
       count = count + 1

   num = num + 1
   
print('There are ' + str(count) + ' primer numbers between 1 and 1000')
