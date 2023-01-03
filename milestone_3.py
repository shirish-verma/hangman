import random

word_list = ['mango', 'watermelon', 'orange', 'banana', 'grapes']
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word "{word}"')
        return True
    else:
        print(f'Sorry, {guess} is not in the word "{word}". Try again.')
        return False

def ask_for_input():
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
    if check_guess(guess) == True:
        return True
    else:
        return False

ask_for_input()