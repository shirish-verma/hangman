import random

word_list = ['mango', 'watermelon', 'orange', 'banana', 'grapes']
word = random.choice(word_list)

while True:
    try:
        guess = input('Enter a single letter: ')
        if guess.isalpha() == True and len(guess) == 1:
            break
        else:
            raise ValueError
    except ValueError:
        print('Invalid letter. Please, enter a single alphabetical character.')
    except KeyboardInterrupt:
        print('Oops! You typed CTRL + C. Please, enter a single alphabetical character.')

