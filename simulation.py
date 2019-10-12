#!/usr/bin/env python3

import random
import time

from board import Board
from fields import Fields
from results import Results

def simulation():
    random.seed(time.time_ns())
    runs = 10**4
    results = {
        Results.PLAYER_X_WINS: 0,
        Results.PLAYER_O_WINS: 0,
        Results.DRAW: 0,
    }
    player_x = (Fields.PLAYER_X, middle_corner_random_option_strategy)
    player_o = (Fields.PLAYER_O, corner_random_option_strategy)
    player_starts = player_x
    for run in range(runs):
        board = Board()
        result = Results.UNDECIDED
        player = player_starts
        while result == Results.UNDECIDED:
            position = player[1](board)
            field = player[0]
            board.set(position, field.value)
            player = player_o if player == player_x else player_x
            result = board.result()
        results[result] += 1
        player_starts = player_o if player == player_x else player_x

    print('X wins\t{:4d}'.format(results[Results.PLAYER_X_WINS]))
    print('O wins\t{:4d}'.format(results[Results.PLAYER_O_WINS]))
    print('Draws\t{:4d}'.format(results[Results.DRAW]))


def first_option_strategy(board):
    # always plays first possible move
    return board.empty_fields()[0]


def random_option_strategy(board):
    # always plays a random move
    return random.choice(board.empty_fields())


def middle_random_option_strategy(board):
    options = board.empty_fields()

    # try to put into the middle field
    if 5 in options:
        return 5

    # pick a random option, if not possible
    return random.choice(options)


def corner_random_option_strategy(board):
    options = board.empty_fields()

    corners = [1, 3, 7, 9]
    random.shuffle(corners)
    for corner in corners:
        if corner in options:
            return corner

    return random.choice(options)

def middle_corner_random_option_strategy(board):
    options = board.empty_fields()

    corners = [1, 3, 7, 9]
    random.shuffle(corners)
    if 5 in options:
        return 5
    for corner in corners:
        if corner in options:
            return corner

    return random.choice(options)

if __name__ == '__main__':
    simulation()
