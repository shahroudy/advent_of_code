import re
from math import sqrt
from pathlib import Path

import numpy as np
from myutils.io_handler import get_input_data


class FractalArt:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.exp = {}
        for line in lines:
            left, right = map(self.make_tile, re.split(r" => ", line.replace("/", "")))
            for tile in (left, np.fliplr(left)):
                for k in range(4):
                    self.exp[self.make_vector(np.rot90(tile, k))] = right

    def make_tile(self, vector):
        v = [ch == "#" for ch in vector] if isinstance(vector, str) else vector
        size = round(sqrt(len(v)))
        return np.reshape(v, (size, size))

    def make_vector(self, tile):
        return tuple(tile.flatten())

    def expand(self, tile):
        return self.exp[self.make_vector(tile)]

    def pixel_count_after_expansion(self, iterations=5):
        cur = self.make_tile(".#...####")
        for _ in range(iterations):
            for s in (2, 3):
                if len(cur) % s == 0:
                    cuts = len(cur) // s
                    cur = np.vstack(
                        [
                            np.hstack([self.expand(tile) for tile in np.hsplit(row, cuts)])
                            for row in np.vsplit(cur, cuts)
                        ]
                    )
                    break
        return np.sum(cur)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert FractalArt("sample1.txt").pixel_count_after_expansion(iterations=2) == 12

    print("Tests passed, starting with the puzzle")

    puzzle = FractalArt(data.input_file)

    print(puzzle.pixel_count_after_expansion(iterations=5))
    print(puzzle.pixel_count_after_expansion(iterations=18))
