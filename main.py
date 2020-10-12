from config import get_choice, who_is_won, refresh_score_board
from constants import score_board
from decorators import timer


def one_hand_game():
    score_board['play'] = True
    while score_board['play']:

        play = True
        game_choices = get_choice()
        winner = who_is_won(**game_choices)
        score_board_refreshing = refresh_score_board(score_board, winner)

        if score_board['play']:
            user_score = score_board['user_score']
            system_score = score_board['system_score']
            print(f"result : {winner}")
            print(f" user score : {user_score}   system score : {system_score} ")

        end_game()


def end_game():
    if not score_board['play']:

        play_again_question = input('wanna play again? y/n  \n').lower()
        if play_again_question == 'n':
            score_board['play'] = False

        elif play_again_question == 'y':
            one_hand_game()

        else:
            print('×× you entered wrong ××')


@timer
def play_again():
    one_hand_game()




play_again()
