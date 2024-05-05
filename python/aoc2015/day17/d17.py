from itertools import combinations
from pathlib import Path

from myutils.io_handler import get_input_data


class NoSuchThingAsTooMuch:
    def __init__(self, filename):
        self.inp = [int(line) for line in Path(filename).read_text().splitlines()]

    def total_number_of_ways(self, s=25):
        return sum(
            sum(c) == s for n in range(1, len(self.inp) + 1) for c in combinations(self.inp, n)
        )

    def number_of_ways_with_min_containers(self, s=25):
        for n in range(1, len(self.inp) + 1):
            counter = sum(sum(c) == s for c in combinations(self.inp, n))
            if counter > 0:
                return counter


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = NoSuchThingAsTooMuch("sample1.txt")
    assert test.total_number_of_ways() == 4
    assert test.number_of_ways_with_min_containers() == 3

    print("Tests passed, starting with the puzzle")

    puzzle = NoSuchThingAsTooMuch(data.input_file)

    print(puzzle.total_number_of_ways(150))
    print(puzzle.number_of_ways_with_min_containers(150))
