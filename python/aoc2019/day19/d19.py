import os
from collections import defaultdict, deque
from itertools import product
from myutils.file_reader import read_int_list
from aoc2019.day09.d09 import IntcodeComputer


class TractorBeam:
    def __init__(self, filename):
        self.program = read_int_list(filename)
        self.computer = IntcodeComputer(self.program.copy())

    def read(self, x, y):
        return bool(self.computer.compute(deque([x, y])).pop())

    def affected_in_50x50(self):
        return sum([self.read(*p) for p in product(range(50), repeat=2)])

    def detect_100x100_square(self):
        start_cols = defaultdict(int)
        row = 0
        while True:
            row += 1
            start = start_cols[row - 1]
            for col in range(start, start + 50):
                if self.read(col, row):
                    break
            else:
                continue
            start_cols[row] = col
            if (
                start_cols[col - 99] > 0
                and self.read(col + 99, row)
                and col >= start_cols[col - 99]
                and self.read(col + 99, row - 99)
            ):
                return col * 10000 + row - 99


if __name__ == "__main__":

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2019_day19.txt'
    puzzle = TractorBeam(input_file)
    print(puzzle.affected_in_50x50())
    print(puzzle.detect_100x100_square())
