import cProfile
import os
import re
from collections import *
from copy import deepcopy
from functools import cache, cmp_to_key, reduce
from itertools import *
from pathlib import Path
from typing import override

import numpy as np
import scipy as sp
from myutils.geometry import Point, Point3D
from myutils.io_handler import get_input_data, submit_answer

# from myutils.search import Search, Search_AStar, Search_BFS, Search_DFS, Search_MinHeap
from myutils.utils import *
from sympy import Symbol
from sympy.solvers import solve


class Puzzle:
    def __init__(self, filename):
        self.input_text = Path(filename).read_text()
        self.mask4 = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.mask8 = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if i or j]
        self.mask9 = [[i, j] for i in range(-1, 2) for j in range(-1, 2)]
        self.maskx = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
        self.directions = {"e": (1, 0), "w": (-1, 0), "n": (0, -1), "s": (0, 1)}
        self.turn_left = {"e": "n", "n": "w", "w": "s", "s": "e"}
        self.turn_right = {"e": "s", "s": "w", "w": "n", "n": "e"}
        self.turn_reverse = {"e": "w", "w": "e", "n": "s", "s": "n"}
        self.dir_chars = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
        self.dir_chars_turn_left = {">": "^", "^": "<", "<": "v", "v": ">"}
        self.dir_chars_turn_right = {">": "v", "v": "<", "<": "^", "^": ">"}
        self.dir_chars_turn_reverse = {">": "<", "<": ">", "^": "v", "v": "^"}

        # read_ints(self)
        # read_line_groups(self)
        # read_int_line_groups(self)
        # process_int_list(self)
        # process_int_int_dict(self)
        # process_int_list_dict(self)
        # process_map_plain(self)
        # process_map_dict_of_sets_of_points(self)
        # process_map_dict_of_sets_of_3D_points(self)

        # process()
        # recursive_split(self, "\n:", strip=True)
        # find_all_re()
        # find_all_per_line_re()

    def calc0(self):
        # s = MySearch()
        # s.search(initial_state=State(0, 0))
        # x = Symbol("x")
        # y = Symbol("y")
        # s = solve(x**2 - 1, x)
        pass

    def calc1(self):
        return None

    def calc2(self):
        return None


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = Puzzle(filename)
    assert answer1 is None or test.calc1() == answer1
    assert answer2 is None or test.calc2() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    # region Tests
    # assert Puzzle("sample1.txt").calc1() == 0
    # assert Puzzle("sample2.txt").calc1() == 0
    # assert Puzzle("sample3.txt").calc1() == 0
    # assert Puzzle("sample4.txt").calc1() == 0
    # assert Puzzle("sample5.txt").calc1() == 0

    # assert Puzzle("sample1.txt").calc2() == 0
    # assert Puzzle("sample2.txt").calc2() == 0
    # assert Puzzle("sample3.txt").calc2() == 0
    # assert Puzzle("sample4.txt").calc2() == 0
    # assert Puzzle("sample5.txt").calc2() == 0
    # endregion

    test_samples("sample1.txt", None, None)
    test_samples("sample2.txt", None, None)
    test_samples("sample3.txt", None, None)
    test_samples("sample4.txt", None, None)
    test_samples("sample5.txt", None, None)

    print("Tests passed, starting with the puzzle")

    puzzle = Puzzle(data.input_file)

    submit_answers = True
    # cProfile.run("print(answer1 := puzzle.calc1())")
    print(answer1 := puzzle.calc1())
    if submit_answers and answer1 is not None:
        submit_answer(answer1, "a", data)
    # cProfile.run("print(answer2 := puzzle.calc2())")
    print(answer2 := puzzle.calc2())
    if submit_answers and answer2 is not None:
        submit_answer(answer2, "b", data)
    exit()

    print(puzzle.calc1())
    print(puzzle.calc2())
