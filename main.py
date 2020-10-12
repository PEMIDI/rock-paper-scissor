from config import get_choice, who_is_won, refresh_score_board
from constants import score_board
from decorators import timer

@timer
def rock_paper_scissor():
        play = True
        while play:

            play = True
            game_choices = get_choice()
            winner = who_is_won(**game_choices)
            score_board_refreshing = refresh_score_board(score_board, winner, play)
            check_game_ending = score_board_refreshing['play']
            

            def end_game(play = True):
    
                if not check_game_ending:

                    play_again_question = input('wanna play again? y/n  \n').lower()
                    if play_again_question == 'y':
                        rock_paper_scissor()

                    elif play_again_question == 'n':
                        play = False
                    
                    else:
                        print('×× you entered wrong ××')
                        end_game(play)

                    return play


            user_score = {score_board_refreshing['score_board']['user_score']}
            system_score = {score_board_refreshing['score_board']['system_score']}
            print(f"result : {winner}")
            print(f" user score : {user_score}   system score : {system_score} ")
        
            play = False if end_game(play) else True

                        
rock_paper_scissor()