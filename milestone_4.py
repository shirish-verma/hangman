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
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            return True
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            return False

    def ask_for_input(self):
        while True:
            guess = input('Enter a single letter: ')
            if guess.isalpha() != True or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print(f'You already tried that letter!')
            else:
                if self.check_guess(guess) == True:
                    self.list_of_guesses.append(guess)
                    return True
                else:
                    return False
    
word_list_1 = ['mango', 'watermelon', 'orange', 'banana', 'grapes']

hm_1 = Hangman(word_list_1)
print(hm_1.word)
print(hm_1.num_letters, end="\n\n")
hm_1.ask_for_input()
print(hm_1.list_of_guesses)