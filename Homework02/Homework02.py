# Homework 02

# Part 1: Hangman
hangman_pic = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
print(hangman_pic)

# Part 2: input name
yourName = input('What is your name? ')
print('Hi', yourName, ', nice to meet you')
# or
print('Hi ' + yourName + ', nice to meet you')
# or
print('Hi ', end='')
print(yourName, end='')
print(', nice to meet you')


