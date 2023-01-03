# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Code Documentation

***import random***
Imported the random module to choose random word from a list.

***word_list = ['mango', 'watermelon', 'orange', 'banana', 'grapes']***
Created a word list for the game to pick from.

***word = random.choice(word_list)***
Called the random.choice method to choose a word from the word list, randomly.

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
Created an infinite while loop to get the first guess from the user until the user gets it right. Excepted expected errors with a message.




