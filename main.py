

from config import get_choice, who_is_won, refresh_score_board
from constants import score_board


#TODO get  user and system value
 
        

    #TODO you want yo play again?

play = True
while play:
    game_choices = get_choice()
    winner = who_is_won(**game_choices)
    score_board_refreshing = refresh_score_board(score_board, winner, play)

    game_end = score_board_refreshing['play']
    
    if not game_end:
        play_again_question = input('wanna play again?\npress n to end')
        if play_again_question == 'n':
            play = False

    user_score = {score_board_refreshing['score_board']['user_score']}
    system_score = {score_board_refreshing['score_board']['system_score']}

    print(f"result : {winner}")
    print(f" user score : {user_score}   system score : {system_score} ")
