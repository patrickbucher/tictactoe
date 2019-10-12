from fields import Fields

class Board:
    def __init__(self, board=None):
        if board is None:
            self.board = ['-' for _ in range(0, 9)]
        else:
            fields = len(board)
            if fields != 9:
                raise ValueError('9 fields required, has {:d}'.format(fields))
            for field in board:
                if field not in Fields.all():
                    raise ValueError('illegal field value "{:s}"'.format(field))
            self.board = board

    def get_board(self):
        return self.board


    def render(self):
        output = ''
        for row in range(0, 3):
            for col in range(0, 3):
                output += self.board[col + row * 3]
            if row < 2:
                output += '\n'
        return output


    def set(self, pos, player):
        index = pos - 1
        if self.board[index] == Fields.EMPTY.value and player in Fields.players():
            self.board[index] = player
        else:
            raise ValueError('cannot set {:s} to {:d}'.format(player, pos))


    def winner(self):
        return self.row_winner() or self.col_winner() or self.cross_winner() or None;


    def row_winner(self):
        rows = [[j for j in range(i, i+3)] for i in range(0, 9, 3)]
        return self.sublist_with_all_of_same(rows)


    def col_winner(self):
        cols = [[j for j in range(i, 9, 3)] for i in range(0, 3)]
        return self.sublist_with_all_of_same(cols)


    def cross_winner(self):
        crosses = [[0, 4, 8], [2, 4, 6]]
        return self.sublist_with_all_of_same(crosses)


    def sublist_with_all_of_same(self, lists):
        for player in Fields.players():
            for sublist in lists:
                if self.all_of_same(sublist, player):
                    return player
        return None


    def all_of_same(self, sublist, player):
        for index in sublist:
            if self.board[index] != player:
                return False
        return True


    def is_draw(self):
        return self.is_full() and self.winner() is None


    def is_full(self):
        for field in self.board:
            if field == Fields.EMPTY.value:
                return False
        return True
