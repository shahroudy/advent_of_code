import re
from functools import cache
from pathlib import Path

from myutils.io_handler import get_input_data


class LinenLayout:
    def __init__(self, filename):
        find_pat = re.compile(r"(\w+)")
        self.pat, self.des = map(find_pat.findall, Path(filename).read_text().split("\n\n"))

    @cache
    def ways(self, d):
        return sum(self.ways(d[len(p) :]) for p in self.pat if d.startswith(p)) if d else 1

    def number_of_possible_patters(self):
        return sum(w > 0 for w in map(self.ways, self.des))

    def sum_of_all_possible_ways(self):
        return sum(map(self.ways, self.des))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert LinenLayout("sample1.txt").number_of_possible_patters() == 6
    assert LinenLayout("sample1.txt").sum_of_all_possible_ways() == 16

    print("Tests passed, starting with the puzzle")

    puzzle = LinenLayout(data.input_file)

    print(puzzle.number_of_possible_patters())
    print(puzzle.sum_of_all_possible_ways())
