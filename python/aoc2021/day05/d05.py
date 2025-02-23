import re
from pathlib import Path

from myutils.io_handler import get_input_data
from numpy import sign


class HydrothermalVenture:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.coordinates = [list(map(int, re.findall(r"(\d+)", line))) for line in lines]

    def count_overlaps(self, keep_diag=False):
        visited, overlaps = set(), set()
        for x0, y0, x1, y1 in self.coordinates:
            if not keep_diag and y0 != y1 and x0 != x1:
                continue
            dx, dy, sx, sy = abs(x1 - x0), abs(y1 - y0), sign(x1 - x0), sign(y1 - y0)
            for i in range(max(dx, dy) + 1):
                point = (x0 + i * sx, y0 + i * sy)
                if point in visited:
                    overlaps.add(point)
                else:
                    visited.add(point)
        return len(overlaps)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert HydrothermalVenture("sample1.txt").count_overlaps(keep_diag=False) == 5
    assert HydrothermalVenture("sample1.txt").count_overlaps(keep_diag=True) == 12

    print("Tests passed, starting with the puzzle")

    puzzle = HydrothermalVenture(data.input_file)
    print(puzzle.count_overlaps(keep_diag=False))
    print(puzzle.count_overlaps(keep_diag=True))
