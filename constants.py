score_board = {
    'user_score' : 0,
    'system_score' : 0
}
score_board['user_score'] += 1
print(score_board)

GAME_RULES = {
    ('p', 'r') : 'user',
    ('r', 'p') : 'system',
    ('s', 'p') : 'user',
    ('p', 's') : 'system',
    ('r', 's') : 'user', 
    ('s', 'r') : 'system'
}

GAME_MODES = ('r', 'p', 's')

# def user_currect_input(user_choice, system_choice):
#     if user_choice in GAME_MODES:
#         user_choice = True

#     if system_choice in GAME_MODES:
#         system_choice = True

#     return user_choice and system_choice

def game_ended(user_score, system_score):

    if score_board['user_score'] > 3 or score_board['system_score'] > 3:
        score_board['user_score'] = 0
        score_board['system_score'] = 0 
        
