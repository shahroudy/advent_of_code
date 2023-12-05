import re
from pathlib import Path


class CampCleanup:
    def __init__(self, filename):
        lines = Path(filename).read_text().strip().split("\n")
        self.ranges = [tuple(map(int, re.split(r"\D", line))) for line in lines]

    def get_sets(self, ranges):
        return [set(range(ranges[i], ranges[i + 1] + 1)) for i in [0, 2]]

    def are_sub_super_sets(self, ranges):
        s1, s2 = self.get_sets(ranges)
        return s1 <= s2 or s2 <= s1

    def are_overlapping(self, ranges):
        s1, s2 = self.get_sets(ranges)
        return bool(s1 & s2)

    def sub_super_set_count(self):
        return sum([self.are_sub_super_sets(r) for r in self.ranges])

    def overlapping_count(self):
        return sum([self.are_overlapping(r) for r in self.ranges])


def test_samples(filename, answer1, answer2):
    test = CampCleanup(filename)
    assert test.sub_super_set_count() == answer1
    assert test.overlapping_count() == answer2


if __name__ == "__main__":

    test_samples("sample1.txt", 2, 4)

    camp_cleanup = CampCleanup("input.txt")
    print(camp_cleanup.sub_super_set_count())
    print(camp_cleanup.overlapping_count())
