class Board:
    WIDTH = 15

    def __init__(self):
        self.board = [[None for _ in range(Board.WIDTH)] for _ in range(Board.WIDTH)]

    def __str__(self):
        return '\n'.join(
            map(Board.row_to_string, self.board)
        )

    @staticmethod
    def row_to_string(row):
        return '|' + '|'.join(
            map(lambda letter: ' ' if letter is None else letter, row)
        ) + '|'

    def __eq__(self, other):
        return self.board == other.board

    def add_letter(self, row, column, letter):
        if len(letter) != 1:
            raise RuntimeError("Invalid letter; must be length one. Found: " + str(len(letter)))

        self.board[row][column] = letter

    def is_valid(self, word, starting_row, starting_column, orientation):
        if starting_row < 0 or starting_row > Board.WIDTH - 1:
            raise RuntimeError("Row out of bounds")
        if starting_column < 0 or starting_column > Board.WIDTH - 1:
            raise RuntimeError("Column out of bounds")
        if len(word) > Board.WIDTH - (starting_column if orientation == "H" else starting_row):
            raise RuntimeError("You stuck a word to close to the edge boyo")

        for i, letter in enumerate(word):
            row = starting_row + (i if orientation == "V" else 0)
            column = starting_column + (i if orientation == "H" else 0)
            if self.board[row][column] not in [None, letter]:
                raise RuntimeError("There's letters in the way of that don't be a silly")

    def add_word(self, word, starting_row, starting_column, orientation):
        self.is_valid(word, starting_row, starting_column, orientation)

        for i, letter in enumerate(word):
            self.add_letter(
                starting_row + (i if orientation == "V" else 0),
                starting_column + (i if orientation == "H" else 0),
                letter.upper()
            )
