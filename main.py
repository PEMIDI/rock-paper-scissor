from random import choice
from constants import GAME_RULES, GAME_MODES, score_board, game_ended



play = True
while play:
    #TODO get  user and system value
    def get_choice():
        
        user_choice = input('Make a choice :  r/p/s\n')
        system_choice = choice((GAME_MODES))
        
        if user_choice in GAME_MODES:
            return {
                'user_choice' : user_choice,
                'system_choice' : system_choice
            }

        print('you entered wrong!')
        return get_choice()

    
    def who_is_won(user_choice, system_choice):
        if user_choice != system_choice:
            result = GAME_RULES[user_choice, system_choice]
            return result
        return 'Draw!'
        
    
    def refresh_score_board(score_board):
        if score_board['user_score'] >= 3 or score_board['system_score'] >= 3:
            score_board['user_score'] = 0
            score_board['system_score'] = 0
            return score_board 

        if winner == 'user':
            score_board["user_score"] += 1
            # print(score_board["user_score"])

        if winner == 'system':
            score_board["system_score"] += 1
            # print(score_board["system_score"]) 

        
        return score_board
        
            

    #TODO you want yo play again?

    game_choices = get_choice()
    winner = who_is_won(**game_choices)
    score_board_refreshing = refresh_score_board(score_board)
    print(winner)
    print(score_board_refreshing)
