import re
from pathlib import Path

from myutils.io_handler import get_input_data


class DuelingGenerators:
    def __init__(self, filename):
        self.inp = [int(n) for n in re.findall(r"\d+", Path(filename).read_text())]

    def judges_final_count(self):
        c = 0
        a, b = self.inp
        for _ in range(40000000):
            a = a * 16807 % 2147483647
            b = b * 48271 % 2147483647
            if a & 0xFFFF == b & 0xFFFF:
                c += 1
        return c

    def judges_final_count_more_picky(self):
        c = 0
        a, b = self.inp
        for _ in range(5000000):
            a = a * 16807 % 2147483647
            while a % 4:
                a = a * 16807 % 2147483647
            b = b * 48271 % 2147483647
            while b % 8:
                b = b * 48271 % 2147483647
            if a & 0xFFFF == b & 0xFFFF:
                c += 1
        return c


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = DuelingGenerators("sample1.txt")
    assert test.judges_final_count() == 588
    assert test.judges_final_count_more_picky() == 309

    print("Tests passed, starting with the puzzle")

    puzzle = DuelingGenerators(data.input_file)

    print(puzzle.judges_final_count())
    print(puzzle.judges_final_count_more_picky())
