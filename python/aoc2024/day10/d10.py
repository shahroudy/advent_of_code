from collections import defaultdict
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data


class HoofIt:
    def __init__(self, filename):
        sets = defaultdict(set)
        for row, line in enumerate(Path(filename).read_text().splitlines()):
            for col, digit in enumerate(line):
                if digit != ".":
                    sets[int(digit)].add(Point(col, row))
        self.locations = dict(sets)
        self.reachable_targets = dict()
        self.path_counts = dict()
        self.find_all_targets_and_paths()

    def calculate_targets_and_paths(self, point: Point, step):
        if step == 9:
            self.reachable_targets[point], self.path_counts[point] = {point}, 1
        else:
            self.path_counts[point] = 0
            self.reachable_targets[point] = set()
            for n in point.neighbors_4():
                if n in self.locations[step + 1]:
                    self.reachable_targets[point].update(self.reachable_targets[n])
                    self.path_counts[point] += self.path_counts[n]

    def find_all_targets_and_paths(self):
        for step in range(9, -1, -1):
            for point in self.locations[step]:
                self.calculate_targets_and_paths(point, step)

    def count_of_all_reachable_targets(self):
        return sum(len(self.reachable_targets[p]) for p in self.locations[0])

    def sum_of_path_counts(self):
        return sum(self.path_counts[p] for p in self.locations[0])


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert HoofIt("sample1.txt").count_of_all_reachable_targets() == 1
    assert HoofIt("sample2.txt").count_of_all_reachable_targets() == 2
    assert HoofIt("sample3.txt").count_of_all_reachable_targets() == 4
    assert HoofIt("sample4.txt").count_of_all_reachable_targets() == 3
    assert HoofIt("sample5.txt").count_of_all_reachable_targets() == 36

    assert HoofIt("sample6.txt").sum_of_path_counts() == 3
    assert HoofIt("sample7.txt").sum_of_path_counts() == 13
    assert HoofIt("sample8.txt").sum_of_path_counts() == 227
    assert HoofIt("sample9.txt").sum_of_path_counts() == 81

    print("Tests passed, starting with the puzzle")

    puzzle = HoofIt(data.input_file)

    print(puzzle.count_of_all_reachable_targets())
    print(puzzle.sum_of_path_counts())
