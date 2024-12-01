import os
import re
from pathlib import Path
from myutils.io_handler import get_input_data


class SlamShuffle:
    def __init__(self, filename=None, description=None, deck_size=10, increment=1, cut=0):
        self.deck_size, self.cut, self.increment = deck_size, cut, increment
        if filename:
            self.load_from_file(filename)
        elif description:
            self.load_from_description(description)

    def load_from_file(self, filename):
        for line in Path(filename).read_text().splitlines():
            self.combine(SlamShuffle(description=line, deck_size=self.deck_size))

    def load_from_description(self, description):
        if m := re.match(r"cut (-?\d+)", description):
            self.increment, self.cut = 1, -int(m.groups(0)[0])
        elif m := re.match(r"deal with increment (-?\d+)", description):
            self.increment, self.cut = int(m.groups(0)[0]), 0
        elif re.match(r"deal into new stack", description):
            self.increment = self.cut = -1 % self.deck_size

    def combine(self, other):
        self.cut = (self.cut * other.increment + other.cut) % self.deck_size
        self.increment = (self.increment * other.increment) % self.deck_size

    def iterate(self, iterations):
        current = self.copy()
        power = 1
        shuffles = {1: current}
        while power < iterations:
            current = current.copy()
            current.combine(current)
            power *= 2
            shuffles[power] = current

        result = SlamShuffle(deck_size=self.deck_size)
        while iterations > 0:
            current = shuffles[power]
            while iterations >= power:
                iterations -= power
                result.combine(current)
            power //= 2
        return result

    def copy(self):
        return SlamShuffle(deck_size=self.deck_size, increment=self.increment, cut=self.cut)

    def inverse(self, n):
        return ((n - self.cut) * pow(self.increment, -1, self.deck_size)) % self.deck_size

    def single_shuffle(self, n):
        return (n * self.increment + self.cut) % self.deck_size

    def shuffle_all_cards(self):
        cards = {self.single_shuffle(n): n for n in range(self.deck_size)}
        return [cards[n] for n in range(self.deck_size)]

    def giant_shuffle_inverse(self, n, iterations):
        return self.iterate(iterations).inverse(n)


def test_samples(filename, deck_size, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = SlamShuffle(filename=filename, deck_size=deck_size)
    assert answer1 is None or test.single_shuffle(answer1[0]) == answer1[1]
    assert answer2 is None or test.giant_shuffle_inverse() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    assert SlamShuffle(filename="sample1.txt").shuffle_all_cards() == [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
    assert SlamShuffle(filename="sample2.txt").shuffle_all_cards() == [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
    assert SlamShuffle(filename="sample3.txt").shuffle_all_cards() == [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]
    assert SlamShuffle(filename="sample4.txt").shuffle_all_cards() == [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]

    print("Tests passed, starting with the puzzle")

    puzzle = SlamShuffle(filename=input_file, deck_size=10007)
    print(puzzle.single_shuffle(2019))
    puzzle = SlamShuffle(filename=input_file, deck_size=119315717514047)
    print(puzzle.giant_shuffle_inverse(2020, iterations=101741582076661))
