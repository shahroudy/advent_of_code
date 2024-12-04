from collections import defaultdict
from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data


class CeresSearch:
    def __init__(self, filename):
        self.map = defaultdict(str)
        for row, line in enumerate(Path(filename).read_text().splitlines()):
            for col, ch in enumerate(line):
                self.map[(col, row)] = ch
        self.rows, self.cols = row + 1, col + 1

    def count_XMAS(self):
        res = 0
        word = "XMAS"
        mask8 = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if i or j]
        for row, col, (dx, dy) in product(range(self.rows), range(self.cols), mask8):
            for i, ch in enumerate(word):
                if self.map[col + dx * i, row + dy * i] != ch:
                    break
            else:
                res += 1
        return res

    def count_X_MAS(self):
        res = 0
        word = "MAS"
        diagonal = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
        for row, col in product(range(self.rows), range(self.cols)):
            count = 0
            for dx, dy in diagonal:
                for j, ch in enumerate(word):
                    i = j - 1
                    if self.map[col + dx * i, row + dy * i] != ch:
                        break
                else:
                    count += 1
            if count == 2:
                res += 1
        return res


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert CeresSearch("sample1.txt").count_XMAS() == 18
    assert CeresSearch("sample1.txt").count_X_MAS() == 9

    print("Tests passed, starting with the puzzle")

    puzzle = CeresSearch(data.input_file)

    print(puzzle.count_XMAS())
    print(puzzle.count_X_MAS())
