import os
import re
from pathlib import Path
from myutils.io_handler import get_input_data


class CorruptionChecksum:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.process()

    def process(self):
        self.inp = []
        for line in self.lines:
            parts = re.split(r"\s", line)
            self.inp.append(list(map(int, parts)))

    def max_min_checksum(self):
        return sum([max(row) - min(row) for row in self.inp])

    def find_int_quotient(self, numbers):
        while numbers:
            a = numbers.pop()
            for b in numbers:
                q = max(a, b) / min(a, b)
                if q.is_integer():
                    return int(q)

    def divisible_checksum(self):
        return sum(self.find_int_quotient(row) for row in self.inp)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = CorruptionChecksum(filename)
    assert answer1 is None or test.max_min_checksum() == answer1
    assert answer2 is None or test.divisible_checksum() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 18, None)
    test_samples("sample2.txt", None, 9)

    print("Tests passed, starting with the puzzle")

    puzzle = CorruptionChecksum(data.input_file)
    print(puzzle.max_min_checksum())
    print(puzzle.divisible_checksum())
