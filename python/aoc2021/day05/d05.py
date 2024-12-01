import os
from collections import defaultdict
from myutils.file_reader import read_lines
from myutils.io_handler import get_input_data


class HydrothermalVenture:
    def __init__(self, filename):
        self.lines = read_lines(filename)

    def process(self, keep_diag=True):
        self.map = defaultdict(int)
        for line in self.lines:
            parts = line.split()
            y0, x0 = list(map(int, parts[0].split(",")))
            y1, x1 = list(map(int, parts[2].split(",")))

            if not keep_diag and y0 != y1 and x0 != x1:
                continue

            dy = abs(y1 - y0)
            dx = abs(x1 - x0)
            for i in range(max(dy, dx) + 1):
                y = (y0 + i * (y1 - y0) / dy) if dy else y0
                x = (x0 + i * (x1 - x0) / dx) if dx else x0
                self.map[(x, y)] += 1

    def count_overlaps(self, keep_diag=True):
        self.process(keep_diag)
        return sum(map(lambda x: x > 1, self.map.values()))


if __name__ == "__main__":
    data = get_input_data(__file__)
    test1 = HydrothermalVenture("test1.txt")
    assert test1.count_overlaps(keep_diag=False) == 5
    assert test1.count_overlaps(keep_diag=True) == 12

    hydrothermal_venture = HydrothermalVenture(data.input_file)
    print(hydrothermal_venture.count_overlaps(keep_diag=False))
    print(hydrothermal_venture.count_overlaps(keep_diag=True))
