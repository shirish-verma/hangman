import random

word_list = ['mango', 'watermelon', 'orange', 'banana', 'grapes']
print(word_list)

word = random.choice(word_list)
print(word)

while True:
    try:
        guess = input('Enter a single letter: ')
        if guess.isalpha() == True and len(guess) == 1:
            print('Good guess!')
            break
        else:
            raise ValueError
    except ValueError:
        print('Oops! That is not a valid input. Please type a single alphabet.')
    except KeyboardInterrupt:
        print('Oops! That is not a valid input. You typed CTRL + C.')

