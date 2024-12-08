from collections import defaultdict
from itertools import combinations
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data


class ResonantCollinearity:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        sets = defaultdict(set)
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                if ch != ".":
                    sets[ch].add(Point(col, row))
        self.map = dict(sets)
        self.rows, self.cols = row + 1, col + 1

    def count_antinode(self, unlimited=False):
        antinode = set()
        for points in self.map.values():
            for a, b in combinations(points, 2):
                delta = b - a
                p = a - delta
                while p.is_inside(self.cols, self.rows):
                    antinode.add(p)
                    p -= delta
                    if not unlimited:
                        break
                p = b + delta
                while p.is_inside(self.cols, self.rows):
                    antinode.add(p)
                    p += delta
                    if not unlimited:
                        break
            if unlimited:
                antinode |= set(points)
        return len(antinode)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ResonantCollinearity("sample1.txt").count_antinode() == 14
    assert ResonantCollinearity("sample1.txt").count_antinode(unlimited=True) == 34
    assert ResonantCollinearity("sample2.txt").count_antinode(unlimited=True) == 9

    print("Tests passed, starting with the puzzle")

    puzzle = ResonantCollinearity(data.input_file)

    print(puzzle.count_antinode())
    print(puzzle.count_antinode(unlimited=True))
