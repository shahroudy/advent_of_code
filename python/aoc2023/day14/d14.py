import os
from collections import defaultdict, deque
from pathlib import Path
from myutils.io_handler import get_input_data


class ParabolicReflectorDish:
    def __init__(self, filename):
        self.init_balls = set()
        self.init_cubes = set()
        for row, line in enumerate(Path(filename).read_text().strip().splitlines()):
            for col, ch in enumerate(line):
                if ch == "O":
                    self.init_balls.add((col, row))
                elif ch == "#":
                    self.init_cubes.add((col, row))
        self.init_cols, self.init_rows = col + 1, row + 1

    def reset(self):
        self.cols, self.rows = self.init_cols, self.init_rows
        self.balls = tuple(
            tuple(sorted([r for (c, r) in self.init_balls if c == col])) for col in range(self.cols)
        )
        self.cubes = tuple(
            tuple(sorted([r for (c, r) in self.init_cubes if c == col])) for col in range(self.cols)
        )

    def tilt_north(self):
        new_balls = tuple()
        for c in range(self.cols):
            balls = deque(self.balls[c])
            cubes = deque(self.cubes[c])
            pre_b = -1
            finished = False
            col_new_balls = []
            while not finished:
                if cubes:
                    b = cubes.popleft()
                else:
                    b = self.cols
                    finished = True
                counter = 0
                while balls and balls[0] < b:
                    balls.popleft()
                    counter += 1
                    col_new_balls.append(pre_b + counter)
                pre_b = b
            new_balls += (tuple(sorted(col_new_balls)),)
        self.balls = new_balls

    def total_load_on_north_support_beam(self):
        return sum(sum(self.rows - r for r in balls) for balls in self.balls)

    def load_after_single_tilt(self):
        self.reset()
        self.tilt_north()
        return self.total_load_on_north_support_beam()

    def rotate_east(self):
        rot_balls = defaultdict(list)
        for col, balls in enumerate(self.balls):
            for r in balls:
                rot_balls[self.rows - 1 - r].append(col)
        self.balls = tuple(tuple(sorted(rot_balls[r])) for r in range(self.rows))

        rot_cubes = defaultdict(list)
        for col, cubes in enumerate(self.cubes):
            for r in cubes:
                rot_cubes[self.rows - 1 - r].append(col)
        self.cubes = tuple(tuple(sorted(rot_cubes[r])) for r in range(self.rows))

        self.cols, self.rows = self.rows, self.cols

    def load_after_a_billion_cycles(self):
        self.reset()
        num_of_iters = 1000000000

        history = dict()
        iter = 0
        fast_forwarded = False
        while iter < num_of_iters:
            for _ in range(4):
                self.tilt_north()
                self.rotate_east()
            iter += 1
            if not fast_forwarded:
                if self.balls not in history:
                    history[self.balls] = iter
                else:
                    period = iter - history[self.balls]
                    iter += period * ((num_of_iters - iter) // period)
                    fast_forwarded = True

        return self.total_load_on_north_support_beam()


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = ParabolicReflectorDish(filename)
    assert answer1 is None or test.load_after_single_tilt() == answer1
    assert answer2 is None or test.load_after_a_billion_cycles() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 136, 64)

    print("Tests passed, starting with the puzzle")

    puzzle = ParabolicReflectorDish(data.input_file)
    print(puzzle.load_after_single_tilt())
    print(puzzle.load_after_a_billion_cycles())
