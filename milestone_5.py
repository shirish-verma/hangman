import milestone_4 as hm_cls

def play_game(word_list):
    game = hm_cls.Hangman(word_list, 5)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_lives != 0 and game.num_letters == 0:
            print('Congratulations. You won the game!')
            break
        elif game.num_lives > 0:
            game.ask_for_input()

list_1 = ['mango', 'watermelon', 'orange', 'banana', 'grapes']
play_game(list_1)
