#!/usr/bin/env python3

from board import Board

if __name__ == '__main__':
    init_state = [
        'o', '-', 'o',
        '-', 'x', '-',
        'x', '-', '-',
    ]
    board = Board(board=init_state)
    board.set(2, 'x')
    board.output()

