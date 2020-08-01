from move import Move


class Player:
    def __init__(self):
        self.hand = []
        self.score = 0

    def pick_move(self, current_board_state):
        word = input("Yo gies your word").upper()
        row = int(input("Which row tho"))
        column = int(input("Which column tho"))
        orientation = "X"
        while orientation not in "HV":
            orientation = input("Which orientation thoooo")
        return Move(word, row, column, orientation)
