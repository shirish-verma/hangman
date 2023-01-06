import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for char in self.word]
        self.num_letters = len(set([*self.word]))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        self.list_of_guesses.append(guess)
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for char in enumerate(self.word):
                if char[1] == guess:
                    self.word_guessed[char[0]] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input('Enter a single letter: ')
            if guess.isalpha() != True or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print(f'You already tried that letter!')
            else:
                return self.check_guess(guess)

""" word_list_1 = ['mango', 'watermelon', 'orange', 'banana', 'grapes']
hm_1 = Hangman(word_list_1)
print(hm_1.word)
print(hm_1.list_of_guesses)
print(hm_1.num_letters, end="\n\n")
hm_1.ask_for_input()
print(hm_1.list_of_guesses)
print(hm_1.word_guessed)
print(hm_1.num_letters) """
