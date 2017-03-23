# Class note: 2017-03-23

teams = ['Patriots', 'Chargers', 'USA']

# Using while loop to go through a list
i = 0
while i < len(teams):
   print(teams[i])
   i = i + 1

# One way of using for loop to go through a list (no index)
for team in teams:
   print(team)

# Another way of using for loop (using index)
for i in range(len(teams)):
   print('Index ' + str(i) + ': ' + str(teams[i]))

# Prime number between 2 and 1000
# Convert while loop to for loop
count = 0
for num in range(2, 1000):
   for i in range(2, num):
       if (num % i) == 0:
           # print(str(num) + " is not a prime number")
           break
   else:
       # only be here when the above for loop goes to the end
       print(str(num) + " is a prime number")
       count = count + 1
   
print('There are ' + str(count) + ' primer numbers between 2 and 1000')

