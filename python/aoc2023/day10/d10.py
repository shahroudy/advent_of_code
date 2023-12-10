import os
from pathlib import Path


class PipeMaze:
    def __init__(self, filename):
        self.map = dict()
        for row, line in enumerate(Path(filename).read_text().strip().splitlines()):
            for col, ch in enumerate(line):
                self.map[(col, row)] = ch
                if ch == "S":
                    self.start = (col, row)
            if row == 0:
                self.cols = col
        self.rows, self.cols = row + 1, col + 1

        self.dirs = {"E": [1, 0], "W": [-1, 0], "N": [0, -1], "S": [0, 1]}
        self.connections = {"|": "NS", "-": "EW", "F": "SE", "J": "NW", "7": "SW", "L": "NE"}

    def next(self, current, direction):
        return tuple(current[i] + self.dirs[direction][i] for i in range(2))

    def neighbors(self, current):
        nei = [self.next(current, dir) for dir in self.connections[self.map[current]]]
        return set(nei)

    def loop_length(self):
        self.loop = [self.start]
        for dir in self.dirs.keys():
            next = self.next(self.start, dir)
            if self.start not in self.neighbors(next):
                continue  # if the neighbor is not connected back to the start, skip it
            while next != self.start:
                self.loop.append(next)
                next = (self.neighbors(next) - {self.loop[-2]}).pop()
            return len(self.loop) // 2

    def fill_mid_points_in_loop(self):
        if not hasattr(self, "loop"):
            self.loop_length()
        self.loop_with_mid_points = set(self.loop) | set(
            [
                (
                    (self.loop[i][0] + self.loop[i - 1][0]) / 2,
                    (self.loop[i][1] + self.loop[i - 1][1]) / 2,
                )
                for i in range(len(self.loop))
            ]
        )

    def count_inner_points(self):
        self.fill_mid_points_in_loop()  # to find inner points, we need to look at finer resolution
        to_visit = [(-0.5, -0.5)]
        outer_points = set(to_visit)  # make a copy as a set
        inner_count = len(self.map) - len(self.loop)
        while to_visit:
            current = to_visit.pop()
            for dir in [[-0.5, 0], [0.5, 0], [0, -0.5], [0, 0.5]]:
                next = (current[0] + dir[0], current[1] + dir[1])
                if (
                    -0.5 <= next[0] <= self.cols - 0.5
                    and -0.5 <= next[1] <= self.rows - 0.5
                    and next not in self.loop_with_mid_points
                    and next not in outer_points
                ):
                    outer_points.add(next)
                    to_visit.append(next)
                    if next in self.map:
                        inner_count -= 1
        return inner_count


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = PipeMaze(filename)
    assert answer1 is None or test.loop_length() == answer1
    assert answer2 is None or test.count_inner_points() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 4, 1)
    test_samples("sample2.txt", 8, 1)
    test_samples("sample3.txt", None, 4)
    test_samples("sample4.txt", None, 8)
    test_samples("sample5.txt", None, 10)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day10.txt'
    puzzle = PipeMaze(input_file)
    print(puzzle.loop_length())
    print(puzzle.count_inner_points())
