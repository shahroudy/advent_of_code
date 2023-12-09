import cProfile
import os
import re
from collections import *
from functools import cache, cmp_to_key, reduce
from itertools import *
from pathlib import Path

from myutils.file_reader import *


class Puzzle:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().splitlines()
        # self.inp = read_int_lines(filename)
        # self.inp = read_line_groups(filename)
        # self.inp = read_int_line_groups(filename)

        self.process()
        # self.process_int_list()
        # self.process_int_int_dict()
        # self.process_int_list_dict()
        # self.process_num_map()

        self.mask4 = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
        self.mask9 = [[i, j] for i in range(-1, 2) for j in range(-1, 2)]
        self.mask8 = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if i or j]

    def process_num_map(self):
        self.map = dict()
        row = 0
        for line in self.lines:
            col = 0
            for ch in line:
                self.map[(col, row)] = int(ch)
                col += 1
            if row == 0:
                self.cols = col
            col = 0
            row += 1
        self.rows = row

    def process_int_list(self):
        self.inp = [list(map(int, re.findall(r"-?\d+", line))) for line in self.lines]

    def process_int_int_dict(self):
        self.inp = {}
        for line in self.lines:
            parts = list(map(int, re.findall(r"-?\d+", line)))
            self.inp[parts[0]] = parts[1]

    def process_int_list_dict(self):
        self.inp = {}
        for line in self.lines:
            parts = list(map(int, re.findall(r"-?\d+", line)))
            self.inp[parts[0]] = parts[1:]

    def process(self):
        self.inp = []

        # self.inp = [tuple(map(int, re.split(r"\D", line))) for line in self.lines]

        # line_re = re.compile(r"(\d+)\s*(\d+):(\d+).*")
        for line in self.lines:
            # parts = line_re.match(line).groups()
            parts = re.split(r"-, ", line)
            # a = parts[0].strip().split(" ")
            # a = list(map(int, re.findall(r"\d+", parts[0])))
            self.inp.append(parts)

    def calc1(self):
        return 0

    def calc2(self):
        return 0


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = Puzzle(filename)
    assert answer1 is None or test.calc1() == answer1
    assert answer2 is None or test.calc2() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", None, None)
    test_samples("sample2.txt", None, None)
    test_samples("sample3.txt", None, None)
    test_samples("sample4.txt", None, None)
    test_samples("sample5.txt", None, None)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day00.txt'
    puzzle = Puzzle(input_file)
    print(puzzle.calc1())
    print(puzzle.calc2())

    # cProfile.run("puzzle.calc1()")
    # cProfile.run("puzzle.calc2()")
