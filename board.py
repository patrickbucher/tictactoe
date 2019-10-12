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


    def draw(self):
        output = ''
        for row in range(0, 3):
            for col in range(0, 3):
                output += self.board[col + row * 3]
            output += '\n'
        return output


    def set(self, pos, player):
        index = pos - 1
        if self.board[index] == Fields.EMPTY.value and player in Fields.players():
            self.board[index] = player
        else:
            raise ValueError('cannot set {:s} to {:d}'.format(player, pos))
