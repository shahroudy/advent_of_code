import os
import re
from pathlib import Path

from myutils.exrange import ranges_overlap, ranges_sub_super_set


class CampCleanup:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        nums = [list(map(int, re.findall(r"\d+", line))) for line in lines]
        self.ranges = [[range(a, b + 1), range(c, d + 1)] for a, b, c, d in nums]

    def sub_super_set_count(self):
        return sum(ranges_sub_super_set(*r) for r in self.ranges)

    def overlapping_count(self):
        return sum(ranges_overlap(*r) for r in self.ranges)


if __name__ == "__main__":

    test = CampCleanup("sample1.txt")
    assert test.sub_super_set_count() == 2
    assert test.overlapping_count() == 4

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day04.txt'
    camp_cleanup = CampCleanup(input_file)
    print(camp_cleanup.sub_super_set_count())
    print(camp_cleanup.overlapping_count())
