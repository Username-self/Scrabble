from constants import LETTER_DISTRIBUTION
from random import shuffle

class Scrabble():
    def __init__(self):
        self.bag = Scrabble.shake_the_bag()

    def shake_the_bag():
        starting_bag = []
        for letter, count in LETTER_DISTRIBUTION.items():
            starting_bag += [letter] * count

        shuffle(starting_bag)

        return starting_bag


if __name__ == '__main__':
    scrabble = Scrabble()
    print(scrabble.bag)
