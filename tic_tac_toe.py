'''
Two player Tic Tac Toe
'''
import random

def choose_symbol():
    '''
    takes input x or o
    returns list of choices ordered by input
    '''
    while True:
        symbol_choice = input('Player 1 choose a symbol! x or o:  ')
        if symbol_choice.lower() == 'x':
            return ['x', 'o']
            
        elif symbol_choice.lower() == 'o':
            return ['o', 'x']
        else:
            print('Please choose either x or o')

def draw_board(board):
    '''
    
    '''
    print(f'{board[7]}|{board[8]}|{board[9]}')
    print(f'-|-|-')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print(f'-|-|-')
    print(f'{board[1]}|{board[2]}|{board[3]}')

def place_symbol(board):
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split():
        position = input('Choose a position to place your symbol (1-9): ')
    return int(position)

def random_player():
    starting_player = choice(['player1', 'player2'])

board = [' '] * 10
draw_board(board)

player_symbols = choose_symbol() 
print(player_symbols)

position = place_symbol(board)
print(position)
board[position] = position
draw_board(board)