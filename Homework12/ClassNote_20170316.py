# string list
s = 'Patriots'
length = len(s)
print('string=' + s + ' has length ' + str(length))

# the index of a list always starts at 0
print(s[0])

i = 0
while i < len(s):
    print('position ' + str(i) + ' is: ' + s[i])
    i = i + 1

print(s[1:6])
print(s[1:])
print(s[-1])
print(s[-3:-1])
print(s[0:-2])
print(s[1:-1])

s2=s[1:-1]
print(s2)

# general list
list = ['abc', 'de', 1, '3']
print(list)
i = 0
while i < len(list):
    print('position ' + str(i) + ' is: ' + str(list[i]))
    i = i + 1
print(list[0:1])
print(list[2:-1])

