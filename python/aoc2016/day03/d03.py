import re
from pathlib import Path

from myutils.io_handler import get_input_data


class SquaresWithThreeSides:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.inp = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

    def possible(self, values):
        return max(values) < sum(values) / 2

    def sum_possible_horizontal(self):
        return sum(self.possible(values) for values in self.inp)

    def sum_possible_vertical(self):
        return sum(
            self.possible([self.inp[j][i], self.inp[j + 1][i], self.inp[j + 2][i]])
            for j in range(0, len(self.inp), 3)
            for i in range(3)
        )


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = SquaresWithThreeSides(filename)
    assert answer1 is None or test.sum_possible_horizontal() == answer1
    assert answer2 is None or test.sum_possible_vertical() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 2, 3)

    print("Tests passed, starting with the puzzle")

    puzzle = SquaresWithThreeSides(data.input_file)

    print(puzzle.sum_possible_horizontal())
    print(puzzle.sum_possible_vertical())
