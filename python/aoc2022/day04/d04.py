import os
import re
from pathlib import Path


class CampCleanup:
    def __init__(self, filename):
        lines = Path(filename).read_text().strip().split("\n")
        self.ranges = [tuple(map(int, re.split(r"\D", line))) for line in lines]

    def sub_super_set_count(self):
        return sum([c >= a and d <= b or a >= c and b <= d for a, b, c, d in self.ranges])

    def overlapping_count(self):
        return sum([not (c < a and d < a or c > b and d > b) for a, b, c, d in self.ranges])


def test_samples(filename, answer1, answer2):
    test = CampCleanup(filename)
    assert test.sub_super_set_count() == answer1
    assert test.overlapping_count() == answer2


if __name__ == "__main__":

    test_samples("sample1.txt", 2, 4)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day04.txt'
    camp_cleanup = CampCleanup(input_file)
    print(camp_cleanup.sub_super_set_count())
    print(camp_cleanup.overlapping_count())
