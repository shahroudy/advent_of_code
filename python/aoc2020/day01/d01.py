from itertools import combinations
from pathlib import Path

from myutils.io_handler import get_input_data


class ReportRepair:
    def __init__(self, filename):
        self.inp = {int(n) for n in Path(filename).read_text().splitlines()}

    def multiplication_of_two(self):
        for n in self.inp:
            if 2020 - n in self.inp:
                return n * (2020 - n)

    def multiplication_of_three(self):
        for n, m in combinations(self.inp, 2):
            if 2020 - n - m in self.inp:
                return n * m * (2020 - n - m)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ReportRepair("sample1.txt").multiplication_of_two() == 514579
    assert ReportRepair("sample1.txt").multiplication_of_three() == 241861950

    print("Tests passed, starting with the puzzle")

    puzzle = ReportRepair(data.input_file)

    print(puzzle.multiplication_of_two())
    print(puzzle.multiplication_of_three())
