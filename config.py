from random import choice
from constants import GAME_RULES, GAME_MODES


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
    

def refresh_score_board(score_board, winner,play):
    Play = True
    if score_board['user_score'] >= 3 or score_board['system_score'] >= 3:
        score_board['user_score'] = 0
        score_board['system_score'] = 0
        return {
            'score_board' : score_board,
            'play' : False
        } 

    if winner == 'user':
        score_board["user_score"] += 1
        # print(score_board["user_score"])

    elif winner == 'system':
        score_board["system_score"] += 1
        # print(score_board["system_score"]) 
    
    return {
        'score_board' : score_board,
        'play' : True
    }
   

