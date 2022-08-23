#testing upload to github

from board import board

def game_of_life():
    ask_rows = int(input('how many rows? '))
    ask_col = int(input('how many columns? '))

    game_of_life_board = board(ask_rows,ask_col)
    game_of_life_board.board_draw()

    
    user_action = ''
    while user_action != 'q':
        user_action = input('Press enter to add generation or q to quit:')
        if user_action == '':
            game_of_life_board.update_board()
            game_of_life_board.board_draw()
game_of_life()