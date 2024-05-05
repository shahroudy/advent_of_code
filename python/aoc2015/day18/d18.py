from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class LikeAGifForYourYard:
    def __init__(self, filename):
        self.mask8 = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if i or j]
        self.init_map = defaultdict(str)
        for row, line in enumerate(Path(filename).read_text().splitlines()):
            for col, ch in enumerate(line):
                self.init_map[(col, row)] = ch
        self.corners = [(0, 0), (0, row), (col, 0), (col, row)]

    def neighbors_counts(self, p):
        return sum(self.current[(p[0] + i, p[1] + j)] == "#" for i, j in self.mask8)

    def light_corners(self):
        for p in self.corners:
            self.current[p] = "#"

    def step_grid(self, set_corners=False):
        next_map = defaultdict(str)
        for p in self.init_map.keys():
            v = self.current[p]
            light_count = self.neighbors_counts(p)
            if v == "#":
                next_map[p] = "#" if light_count in (2, 3) else "."
            if v == ".":
                next_map[p] = "#" if light_count == 3 else "."
        self.current = next_map
        if set_corners:
            self.light_corners()

    def animate_grid(self, steps=4, set_corners=False):
        self.current = self.init_map.copy()
        if set_corners:
            self.light_corners()
        for _ in range(steps):
            self.step_grid(set_corners)
        return sum(v == "#" for v in self.current.values())


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = LikeAGifForYourYard("sample1.txt")
    assert test.animate_grid(steps=4) == 4
    assert test.animate_grid(steps=5, set_corners=True) == 17

    print("Tests passed, starting with the puzzle")

    puzzle = LikeAGifForYourYard(data.input_file)

    print(puzzle.animate_grid(steps=100))
    print(puzzle.animate_grid(steps=100, set_corners=True))
