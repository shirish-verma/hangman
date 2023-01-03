# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Code Documentation

Imported the random module to choose random word from a list.
***import random***

Created a word list for the game to pick from.
***word_list = ['mango', 'watermelon', 'orange', 'banana', 'grapes']***

Called the random.choice method to choose a word from the word list, randomly.
***word = random.choice(word_list)***

Created an infinite while loop to get the first guess from the user until the user gets it right. Excepted expected errors with a message.
***while True:***
    ***try:***
        ***guess = input('Enter a single letter: ')***
        ***if guess.isalpha() == True and len(guess) == 1:***
            ***print('Good guess!')***
            ***break***
        ***else:***
            ***raise ValueError***
    ***except ValueError:***
        ***print('Oops! That is not a valid input. Please type a single alphabet.')***
    ***except KeyboardInterrupt:***
        ***print('Oops! That is not a valid input. You typed CTRL + C.')***

Moved the check guess logic to a function.
***def check_guess(guess):***
    ***guess = guess.lower()***
    ***if guess in word:***
        ***print(f'Good guess! {guess} is in the word "{word}"')***
        ***return True***
    ***else:***
        ***print(f'Sorry, {guess} is not in the word "{word}". Try again.')***
        ***return False***


Moved the input a guess logic to a function that returns true or false depending on whether the guess was correct.
***def ask_for_input():***
    ***while True:***
        ***try:***
            ***guess = input('Enter a single letter: ')***
            ***if guess.isalpha() == True and len(guess) == 1:***
                ***break***
            ***else:***
                ***raise ValueError***
        ***except ValueError:***
            ***print('Invalid letter. Please, enter a single alphabetical character.')***
        ***except KeyboardInterrupt:***
            ***print('Oops! You typed CTRL + C. Please, enter a single alphabetical character.')***
    ***if check_guess(guess) == True:***
        ***return True***
    ***else:***
        ***return False***

