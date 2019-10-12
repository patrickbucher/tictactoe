import unittest

from fields import Fields
from board import Board

class BoardTest(unittest.TestCase):

    def test_init_empty(self):
        empty = Fields.EMPTY.value
        empty_board = [
            empty, empty, empty,
            empty, empty, empty,
            empty, empty, empty,
        ]
        board = Board()
        self.assertEqual(board.get_board(), empty_board)


    def test_init_played(self):
        empty = Fields.EMPTY.value
        p_x = Fields.PLAYER_X.value
        p_o = Fields.PLAYER_O.value
        played_board = [
            empty, p_x, empty,
            empty, p_o, empty,
            p_o, p_x, empty,
        ]
        board = Board(played_board)
        self.assertEqual(board.get_board(), played_board)


    def test_init_illegal_fields(self):
        empty = Fields.EMPTY.value
        p_x = Fields.PLAYER_X.value
        p_o = Fields.PLAYER_O.value
        illegal_board = [
            empty, p_x, p_o,
            p_o, empty, p_x,
            '%', empty, empty,
        ]
        with self.assertRaises(ValueError):
            Board(illegal_board)


    def test_draw(self):
        empty = Fields.EMPTY.value
        p_x = Fields.PLAYER_X.value
        p_o = Fields.PLAYER_O.value
        board = [
            p_x, p_o, empty,
            p_x, p_x, empty, 
            p_o, p_o, p_x,
        ]
        board_drawn = '{}{}{}\n{}{}{}\n{}{}{}'.format(*tuple(board))
        self.assertEqual(Board(board).draw(), board_drawn)


    def test_legal_moves(self):
        p_x = Fields.PLAYER_X.value
        p_o = Fields.PLAYER_O.value
        moves = [
            p_x, p_o, p_x,
            p_o, p_x, p_o,
            p_x, p_o, p_x,
        ]
        board = Board()
        for index, move in enumerate(moves):
            position = index + 1
            board.set(position, move)
        self.assertEqual(board.get_board(), moves)


    def test_illegal_move(self):
        p_x = Fields.PLAYER_X.value
        p_o = Fields.PLAYER_O.value
        board = Board()
        board.set(5, p_x)
        board.set(2, p_o)
        board.set(1, p_x)
        board.set(9, p_o)
        with self.assertRaises(ValueError):
            board.set(9, p_x)


    def test_winner(self):
        x = Fields.PLAYER_X.value
        o = Fields.PLAYER_O.value
        e = Fields.EMPTY.value
        winners = [
            ([e, e, e,
              e, e, e,
              e, e, e], None),
            ([e, e, e,
              e, e, e,
              o, o, o], o),
            ([x, x, x,
              o, e, o,
              e, o, o], x),
            ([x, o, e,
              x, e, o,
              x, o, e], x),
            ([x, o, x,
              o, x, o,
              x, o, e], x),
            ([x, e, o,
              e, o, x,
              o, x, e], o),
        ]
        for item in winners:
            board = item[0]
            winner = item[1]
            self.assertEqual(Board(board).winner(), winner)


if __name__ == '__main__':
    unittest.main()
