from nltk.corpus import words, wordnet
from bisect import bisect_left
import re


class WordChecker:

    def __init__(self):
        isAlpha = lambda x: re.compile('[A-Za-z]').match(x)
        corpus = list(filter(isAlpha, words.words() + list(wordnet.all_lemma_names())))
        self.valid_words = sorted(corpus)

    def is_valid_word(self, word):
        i = bisect_left(self.valid_words, word.lower())
        if i != len(self.valid_words) and self.valid_words[i] == word.lower():
            return True
        return False
