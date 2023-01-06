# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Code Documentation

# Imported the random module to choose random word from a list.
# Created a word list for the game to pick from.
# Called the random.choice method to choose a word from the word list, randomly.

# Moved the check guess logic to a function.
Built the guess logic function to check whether the user's input matches with one of the characters of the word to be guessed. 

# Moved the input a guess logic to a function that returns true or false depending on whether the guess was correct.

Created an infinite while loop to get the first guess from the user until the user gets it right. Excepted expected errors with a message.

# Created Hangman class and moved all the relevant functions made above within the class. Initialized new variables needed for the game logic. (milestone_4.py)

Defined the class and initiated the attributes. Used self to instantiate the attributes and assign the arguments. Created methods, i.e. functions, by moving the ask input and check guess functions within the class.

# Created a new file milestone_5.py and imported milestone 4 to use the class.
# Created a new function that uses the hangman object and game logic to complete the game.
# Tons of room for improvement in user communication to let them know where they stand at different stages of the game.