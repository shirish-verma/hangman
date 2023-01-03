import random

word_list = ['mango', 'watermelon', 'orange', 'banana', 'grapes']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Enter a single letter: ')
print(guess)