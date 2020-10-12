

score_board = {
    'user_score' : 0,
    'system_score' : 0,
    'play' : True,
    'game_ending' : False
}


GAME_RULES = {
    ('p', 'r') : 'user',
    ('r', 'p') : 'system',
    ('s', 'p') : 'user',
    ('p', 's') : 'system',
    ('r', 's') : 'user', 
    ('s', 'r') : 'system'
}

GAME_MODES = ('r', 'p', 's')


        
