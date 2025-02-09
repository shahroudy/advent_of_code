import cProfile
import os
import re
from collections import *
from collections import Counter, defaultdict, deque, namedtuple
from copy import deepcopy
from functools import *
from functools import cache, cmp_to_key, reduce
from itertools import *
from itertools import combinations, combinations_with_replacement, permutations, product
from pathlib import Path
from typing import override

import numpy as np
import scipy as sp
from myutils.geometry import *
from myutils.geometry import (
    Point,
    Point3D,
    connected_region,
    find_connected_components,
    inner_border,
    outer_border,
    region_perimeter,
)
from myutils.grammar import count_matching_inputs
from myutils.io_handler import get_input_data, submit_answer
from myutils.matching import find_match_dict
from myutils.matrix import (
    concat_2d_matrices,
    find_all_points_with_value,
    flip,
    hstack,
    mirror,
    rotate,
    rotate_90,
    rotate_180,
    rotate_270,
    sub_matrix,
    tile_side,
    transpose,
    tuple_matrix,
    vstack,
)

# from myutils.search import Search, Search_AStar, Search_BFS, Search_DFS, Search_MinHeap
from myutils.utils import (
    MapSearch,
    MySearch,
    find_all_per_line_re,
    find_all_re,
    get_sample_number,
    multiply,
    print_with_color,
    process,
    process_int_int_dict,
    process_int_list,
    process_int_list_dict,
    process_map_dict_of_sets_of_3D_points,
    process_map_dict_of_sets_of_points,
    process_map_plain,
    read_int_line_groups,
    read_ints,
    read_line_groups,
    recursive_split,
)
from sympy import Symbol
from sympy.solvers import solve


class Puzzle:
    def __init__(self, filename):
        self.input_text = Path(filename).read_text()

        # read_ints(self)
        # read_line_groups(self)
        # read_int_line_groups(self)
        # process_int_list(self)
        # process_int_int_dict(self)
        # process_int_list_dict(self)
        # process_map_plain(self)
        # process_map_dict_of_sets_of_points(self)
        # process_map_dict_of_sets_of_3D_points(self)

        # process(self)

        # recursive_split(self, "\n:", strip=True)
        # inputs = recursive_split(self, "\n:", text=line, strip=True)

        # find_all_re(self, r"(\d+)")
        # inputs = find_all_re(self, r"(\d+)", text=line)

        # find_all_per_line_re(self, r"(\d+)")
        # inputs = find_all_per_line_re(self, r"(\d+)", text=line)

        # for easy setting of different parameters for samples vs real data
        self.sample_number = get_sample_number(filename)
        self.parameter = {
            0: 100,  # real data
            1: 10,  # sample 1
            2: 10,  # sample 2
            3: 10,  # sample 3
            4: 10,  # sample 4
            5: 10,  # sample 5
            6: 10,  # sample 6
            7: 10,  # sample 7
            8: 10,  # sample 8
            9: 10,  # sample 9
        }[self.sample_number]

    def calc1(self):
        return None

    def calc2(self):
        return None

    def calc0(self):
        # s = MySearch()
        # s.search(initial_state=MySearch.State(0, 0))

        # s = MapSearch(walls=set(), nodes=set(), rows=100, cols=100)
        # min_dist, backtrack = s.search(initial_state=MapSearch.State(Point(0, 0), 0, 0))
        # goal_dist = min_dist.get(Point(goal), None)

        # x = Symbol("x")
        # y = Symbol("y")
        # s = solve(x**2 - 1, x)
        pass


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
    # assert Puzzle("sample6.txt").calc1() == 0
    # assert Puzzle("sample7.txt").calc1() == 0
    # assert Puzzle("sample8.txt").calc1() == 0
    # assert Puzzle("sample9.txt").calc1() == 0

    # assert Puzzle("sample1.txt").calc2() == 0
    # assert Puzzle("sample2.txt").calc2() == 0
    # assert Puzzle("sample3.txt").calc2() == 0
    # assert Puzzle("sample4.txt").calc2() == 0
    # assert Puzzle("sample5.txt").calc2() == 0
    # assert Puzzle("sample6.txt").calc2() == 0
    # assert Puzzle("sample7.txt").calc2() == 0
    # assert Puzzle("sample8.txt").calc2() == 0
    # assert Puzzle("sample9.txt").calc2() == 0
    # endregion

    test_samples("sample1.txt", None, None)
    test_samples("sample2.txt", None, None)
    test_samples("sample3.txt", None, None)
    test_samples("sample4.txt", None, None)
    test_samples("sample5.txt", None, None)
    test_samples("sample6.txt", None, None)
    test_samples("sample7.txt", None, None)
    test_samples("sample8.txt", None, None)
    test_samples("sample9.txt", None, None)

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
