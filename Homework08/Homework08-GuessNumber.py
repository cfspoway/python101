# Homework #08
# Guess the number

guesses_made = 0

name = input('Hello! What is your name? ')

number = 100

print('Well, ' + name + ' I am thinking of a number')

while guesses_made < 5:

    guess = int(input('Take a guess: '))

    guesses_made = guesses_made + 1

    if guess < number:
        print('Your guess is too low.')
        continue
    elif guess > number:
        print('Your guess is too high.')
        continue
    else:
        # guess == number:
        break

if guess == number:
    if guesses_made > 1:
        s1 = 'Good job '
        s2 = ' guesses!'
    else:
        s1 = 'Great job '
        s2 = ' guess!'
    print(s1 + name + ', you guessed my number in ' + str(guesses_made) + s2)
else:
    print('Nope. The number I was thinking of was ' + str(number))
