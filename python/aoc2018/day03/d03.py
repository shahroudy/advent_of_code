import os
import re
from collections import defaultdict
from itertools import product
from myutils.file_reader import read_lines


class NoMatterHowYouSliceIt:
    def __init__(self, filename):
        self.lines = read_lines(filename)
        self.process()

    def process(self):
        self.claims = []
        for line in self.lines:
            nums = re.sub(r"\D", " ", line)
            parts = list(map(int, nums.split()))
            self.claims.append(parts)
        self.claimed_count = defaultdict(int)
        for claim in self.claims:
            _, x, y, width, height = claim
            for i in range(width):
                for j in range(height):
                    self.claimed_count[(x + i, y + j)] += 1

    def within_multiple_claims(self):
        return sum([value >= 2 for value in self.claimed_count.values()])

    def id_of_no_overlapping_claim(self):
        for claim in self.claims:
            number, x, y, width, height = claim
            for i, j in product(range(width), range(height)):
                if self.claimed_count[(x + i, y + j)] != 1:
                    break
            else:
                return number


if __name__ == "__main__":

    test1 = NoMatterHowYouSliceIt("test1.txt")
    assert test1.within_multiple_claims() == 4
    assert test1.id_of_no_overlapping_claim() == 3

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2018_day03.txt'
    puzzle = NoMatterHowYouSliceIt(input_file)
    print(puzzle.within_multiple_claims())
    print(puzzle.id_of_no_overlapping_claim())
