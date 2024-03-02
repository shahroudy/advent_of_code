import cProfile
import os
import re
from collections import *
from copy import deepcopy
from functools import cache, cmp_to_key, reduce
from itertools import *
from pathlib import Path

from myutils.file_reader import *
from myutils.io_handler import get_input_data, submit_answer
from sympy import Symbol
from sympy.solvers import solve


class Puzzle:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().splitlines()
        # self.inp = read_int_lines(filename)
        # self.inp = read_line_groups(filename)
        # self.inp = read_int_line_groups(filename)

        self.directions = {"e": (1, 0), "w": (-1, 0), "n": (0, -1), "s": (0, 1)}
        self.dir_chars = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
        self.mask4 = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.mask5 = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
        self.mask9 = [[i, j] for i in range(-1, 2) for j in range(-1, 2)]
        self.mask8 = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if i or j]

        self.process()
        # self.process_int_list()
        # self.process_int_int_dict()
        # self.process_int_list_dict()
        # self.process_map()

    def print_with_color(self, text, text_color="#FFFFFF", back_color="#000000", end="\n"):
        from colored import attr, bg, fg

        color = fg(text_color)
        back = bg(back_color)
        reset = attr("reset")
        print(f"{color+ back}" + text + f"{reset}", end=end)

    def process_map(self):
        self.map = dict()
        for row, line in enumerate(self.lines):
            for col, ch in enumerate(line):
                self.map[(col, row)] = ch
        self.rows, self.cols = row + 1, col + 1

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
        return None

    def calc2(self):
        return None

    def solve_some_equation(self):
        x = Symbol("x")
        y = Symbol("y")
        s = solve(x**2 - 1, x)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = Puzzle(filename)
    assert answer1 is None or test.calc1() == answer1
    assert answer2 is None or test.calc2() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", None, None)
    test_samples("sample2.txt", None, None)
    test_samples("sample3.txt", None, None)
    test_samples("sample4.txt", None, None)
    test_samples("sample5.txt", None, None)

    print("Tests passed, starting with the puzzle")

    submit_answers = True
    puzzle = Puzzle(data.input_file)
    # cProfile.run("print(answer1 := puzzle.calc1())")
    print(answer1 := puzzle.calc1())
    if submit_answers and answer1 is not None:
        submit_answer(answer1, "a", data)
    # cProfile.run("print(answer2 := puzzle.calc2())")
    print(answer2 := puzzle.calc2())
    if submit_answers and answer2 is not None:
        submit_answer(answer2, "b", data)
