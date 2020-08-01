from constants import LETTER_DISTRIBUTION
from random import shuffle
from player import Player
from board import Board
from word_checker import WordChecker


class Scrabble:
    def __init__(self, number_of_players):
        if number_of_players < 2 or number_of_players > 4:
            raise RuntimeError("Invalid number of players; must be 2, 3 or 4, found " + number_of_players)
        self.bag = Scrabble.shake_the_bag()
        self.players = [Player() for _ in range(number_of_players)]
        for player in self.players:
            player.hand += self.draw_tiles(7)
        self.current_player_index = 0
        self.board = Board()
        self.turn_counter = 0
        self.word_checker = WordChecker()

    def run_game(self):
        while True:
            current_player = self.players[self.current_player_index]
            print(self.board)
            print("Current player is player " + str(self.current_player_index))
            print("Your tiles are " + str(current_player.hand))
            move = self.get_valid_move(current_player)
            letters_needed_for_move = self.get_letters_needed_for_move(move)
            for letter in letters_needed_for_move:
                current_player.hand.remove(letter)
            current_player.hand += self.draw_tiles(len(letters_needed_for_move))

            self.board.add_word(move)
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            self.turn_counter += 1

    def get_valid_move(self, current_player):
        while True:
            try:
                move = current_player.pick_move(self.board)
                self.is_valid(move)
                break
            except RuntimeError as e:
                print(e.args)
        return move

    def is_valid(self, move):
        self.board.is_valid(move)
        current_player = self.players[self.current_player_index]
        letters_needed_for_move = self.get_letters_needed_for_move(move)
        if not Scrabble.is_subset(letters_needed_for_move, current_player.hand):
            raise RuntimeError("you don't have dem letters boi")
        if self.turn_counter == 0:
            if not Board.is_over_centre_square(move):
                raise RuntimeError("gotta be in dat middle")
        else:
            if len(letters_needed_for_move) == len(move.word):
                raise RuntimeError("use what's there, fuckwit")

        if not self.word_checker.is_valid_word(move.word):
            raise RuntimeError("Who taught you to spell you insuffetrabel goon")

    def get_letters_needed_for_move(self, move):
        letters_to_add = []
        for i, letter in enumerate(move.word):
            row = move.starting_row + (i if move.orientation == "V" else 0)
            column = move.starting_column + (i if move.orientation == "H" else 0)
            if self.board.board[row][column] is None:
                letters_to_add += letter
        return letters_to_add

    def draw_tiles(self, n=1):
        return [self.bag.pop() for _ in range(n)]

    @staticmethod
    def is_subset(littlelist, biglist):
        big_list_copy = biglist.copy()
        for x in littlelist:
            if x not in big_list_copy:
                return False
            big_list_copy.remove(x)
        return True

    @staticmethod
    def shake_the_bag():
        starting_bag = []
        for letter, count in LETTER_DISTRIBUTION.items():
            starting_bag += [letter] * count

        shuffle(starting_bag)

        return starting_bag


if __name__ == '__main__':
    scrabble = Scrabble(2)
    scrabble.run_game()
