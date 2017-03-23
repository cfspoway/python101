sentence = input('Please input a sentence')
length = len(sentence)
#print(length)

fc = 0 #first character
pos = 0 #position
print('The word list is:')

while pos < length:
    if sentence[pos] == ' ':
        if pos != fc:
            print(sentence[fc:pos])
        pos = pos + 1
        fc = pos 
    else:
        pos = pos + 1

if pos != fc:
    print(sentence[fc:pos])
    
