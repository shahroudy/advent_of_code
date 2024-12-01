import os
from pathlib import Path
from myutils.io_handler import get_input_data


class RucksackReorganization:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")

    def priority_of_common_item(self, *rucksacks):
        c = set.intersection(*(set(rucksack) for rucksack in rucksacks)).pop()
        return ord(c.upper()) - ord("A") + (27 if c.isupper() else 1)

    def halves(self, rucksack):
        mid_index = len(rucksack) // 2
        return rucksack[:mid_index], rucksack[mid_index:]

    def sum_of_common_items(self):
        return sum([self.priority_of_common_item(*self.halves(r)) for r in self.lines])

    def groups_of_3(self, elves):
        return [elves[g * 3 : g * 3 + 3] for g in range(len(elves) // 3)]

    def sum_of_badges(self):
        return sum([self.priority_of_common_item(*t) for t in self.groups_of_3(self.lines)])


def test_samples(filename, answer1, answer2):
    test = RucksackReorganization(filename)
    assert test.sum_of_common_items() == answer1
    assert test.sum_of_badges() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 157, 70)

    rucksack_reorganization = RucksackReorganization(data.input_file)
    print(rucksack_reorganization.sum_of_common_items())
    print(rucksack_reorganization.sum_of_badges())
