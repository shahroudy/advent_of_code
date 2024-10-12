import re
from math import lcm
from pathlib import Path

from myutils.io_handler import get_input_data


class TimingIsEverything:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.discs = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

    def fist_capsule_passing_time(self, extra_disc=False):
        discs = self.discs + ([[len(self.discs) + 1, 11, 0, 0]] if extra_disc else [])
        time, step = 0, 1
        for i, n, _, p in sorted(discs, key=lambda x: x[1], reverse=True):
            while (p + i + time) % n:
                time += step
            step = lcm(step, n)
        return time


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert TimingIsEverything("sample1.txt").fist_capsule_passing_time() == 5

    print("Tests passed, starting with the puzzle")

    puzzle = TimingIsEverything(data.input_file)

    print(puzzle.fist_capsule_passing_time())
    print(puzzle.fist_capsule_passing_time(extra_disc=True))
