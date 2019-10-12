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
            'S', empty, empty,
        ]
        with self.assertRaises(ValueError):
            Board(illegal_board)

if __name__ == '__main__':
    unittest.main()
