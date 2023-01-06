import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for char in self.word]
        self.num_letters = 0
        self.list_of_guesses = []
    


word_list_1 = ['mango', 'watermelon', 'orange', 'banana', 'grapes']

hm_1 = Hangman(word_list_1)

print(hm_1.word)