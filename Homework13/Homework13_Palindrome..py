s = input('Please input any thing here: ')
l = len(s)

mid = int((l-1)/2)
palindrome = True;
for i in range(mid):
    if s[i] != s[len(s)-1-i]:
        palindrome = False;
        break;

if palindrome:
    print(s + ' is palindrome')
else:
    print(s + ' is not palindrome')
