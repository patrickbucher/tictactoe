from enum import Enum

class Fields(Enum):
    EMPTY = '-'
    PLAYER_X = 'x'
    PLAYER_O = 'o'

    def all():
        return [Fields.EMPTY.value, Fields.PLAYER_X.value, Fields.PLAYER_O.value]

    def players():
        return [Fields.PLAYER_X.value, Fields.PLAYER_O.value]
