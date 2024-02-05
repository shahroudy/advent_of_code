import re
from collections import defaultdict
from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data, submit_answer


class ReservoirResearch:
    def __init__(self, filename):
        self.process_input(filename)
        self.simulate()

    def process_input(self, filename):
        self.map = defaultdict(lambda: ".")
        line_re = re.compile(r"(\w)=(\d+),\s*\w=(\d+)..(\d+)")
        for line in Path(filename).read_text().splitlines():
            fix_var, fix_value, range_start, range_end = re.match(line_re, line).groups()
            fix_value, range_start, range_end = map(int, (fix_value, range_start, range_end))
            r1, r2 = range(fix_value, fix_value + 1), range(int(range_start), int(range_end) + 1)
            for x, y in product(*((r1, r2) if fix_var == "x" else (r2, r1))):
                self.map[x, y] = "#"
        self.spring = (500, 0)
        y_values = {y for _, y in self.map.keys()}
        self.min_y, self.max_y = min(y_values), max(y_values)

    def simulate(self):
        waterfalls = {self.spring}
        while waterfalls:
            x, y = waterfalls.pop()
            y += 1
            while self.map[x, y] == "." and y <= self.max_y:
                self.map[x, y] = "|"
                y += 1
            if self.map[x, y] == "|":
                continue
            y -= 1
            if y < self.max_y:
                new_waterfalls = set()
                while len(new_waterfalls) == 0:
                    new_points = []
                    for dx in (-1, 1):
                        nx, ny = x, y
                        while self.map[nx, ny] != "#":
                            new_points.append((nx, ny))
                            if self.map[nx, ny + 1] in "~#":
                                nx += dx
                            else:
                                new_waterfalls.add((nx, ny))
                                break
                    fill_with = "~" if len(new_waterfalls) == 0 else "|"
                    for p in new_points:
                        self.map[p] = fill_with
                    y -= 1
                waterfalls.update(new_waterfalls)

    def water_reached_count(self):
        return sum(v in "|~" for (x, y), v in self.map.items() if self.min_y <= y <= self.max_y)

    def remaining_water_count(self):
        return sum(v == "~" for (x, y), v in self.map.items() if self.min_y <= y <= self.max_y)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = ReservoirResearch(filename)
    assert answer1 is None or test.water_reached_count() == answer1
    assert answer2 is None or test.remaining_water_count() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 57, 29)
    test_samples("sample2.txt", 96, 65)

    print("Tests passed, starting with the puzzle")

    puzzle = ReservoirResearch(data.input_file)
    print(puzzle.water_reached_count())
    print(puzzle.remaining_water_count())
