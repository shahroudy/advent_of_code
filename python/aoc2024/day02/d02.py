import re
from itertools import combinations
from pathlib import Path

from myutils.io_handler import get_input_data


class RedNosedReports:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.inp = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

    def is_safe(self, input, tolerance=0):
        for ls in combinations(input, len(input) - tolerance):
            inc = ls[0] > ls[-1]
            for i, j in zip(ls[:-1], ls[1:]):
                if (inc and i <= j) or (not inc and i >= j) or abs(i - j) > 3:
                    break
            else:
                return True
        return False

    def safe_count(self, tolerance=0):
        return sum(self.is_safe(ls, tolerance) for ls in self.inp)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert RedNosedReports("sample1.txt").safe_count(0) == 2
    assert RedNosedReports("sample1.txt").safe_count(1) == 4

    print("Tests passed, starting with the puzzle")

    puzzle = RedNosedReports(data.input_file)

    print(puzzle.safe_count(0))
    print(puzzle.safe_count(1))
