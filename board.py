from math import floor


class Board:
    WIDTH = 15

    def __init__(self):
        self.board = [[None for _ in range(Board.WIDTH)] for _ in range(Board.WIDTH)]

    def __str__(self):

        column_labels = '   |' + '|'.join(map(Board.label_to_string, range(Board.WIDTH)))
        return column_labels + '\n' + '\n'.join(
            [Board.row_to_string(row, i) for i, row in enumerate(self.board)]
        ) + '\n' + column_labels

    @staticmethod
    def row_to_string(row, i):
        return Board.label_to_string(i) + ' |' + '|'.join(
            map(Board.letter_to_string, row)
        ) + '|' + Board.label_to_string(i)

    @staticmethod
    def letter_to_string(letter):
        length = len(str(Board.WIDTH - 1))
        return ' ' * length if letter is None else letter + ' ' * (length - 1)

    @staticmethod
    def label_to_string(i):
        length = len(str(Board.WIDTH - 1))
        i_str = str(i)
        return i_str + ' ' * (length - len(i_str))

    def __eq__(self, other):
        return self.board == other.board

    def add_letter(self, row, column, letter):
        if len(letter) != 1:
            raise RuntimeError("Invalid letter; must be length one. Found: " + str(len(letter)))

        self.board[row][column] = letter

    def is_valid(self, move):
        if move.starting_row < 0 or move.starting_row > Board.WIDTH - 1:
            raise RuntimeError("Row out of bounds")
        if move.starting_column < 0 or move.starting_column > Board.WIDTH - 1:
            raise RuntimeError("Column out of bounds")
        if len(move.word) > Board.WIDTH - (move.starting_column if move.orientation == "H" else move.starting_row):
            raise RuntimeError("You stuck a word to close to the edge boyo")

        for i, letter in enumerate(move.word):
            row = move.starting_row + (i if move.orientation == "V" else 0)
            column = move.starting_column + (i if move.orientation == "H" else 0)
            if self.board[row][column] not in [None, letter]:
                raise RuntimeError("There's letters in the way of that don't be a silly")

    def add_word(self, move):
        self.is_valid(move)

        for i, letter in enumerate(move.word):
            self.add_letter(
                move.starting_row + (i if move.orientation == "V" else 0),
                move.starting_column + (i if move.orientation == "H" else 0),
                letter.upper()
            )

    @staticmethod
    def is_over_centre_square(move):
        centre_square = floor((Board.WIDTH - 1) / 2)
        for i, letter in enumerate(move.word):
            row = move.starting_row + (i if move.orientation == "V" else 0)
            column = move.starting_column + (i if move.orientation == "H" else 0)
            if row == centre_square and column == centre_square:
                return True
        return False
