#!/usr/bin/env python3

from board import Board
from fields import Fields
from results import Results

def tictactoe():
    board = Board()
    p_one = Fields.PLAYER_X
    p_two = Fields.PLAYER_O
    player = p_one
    result = Results.UNDECIDED
    while result == Results.UNDECIDED:
        print(board.render())
        turn_done = False
        while not turn_done:
            choice = input('{}: '.format(player.value))
            try:
                position = int(choice)
                board.set(position, player.value)
                turn_done = True
            except ValueError:
                print('please pick an empty field (1-9)')
        player = p_two if player == p_one else p_one
        result = board.result()
    print(board.render())
    print('game ended: {}'.format(result))


if __name__ == '__main__':
    tictactoe()
