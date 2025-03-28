import concurrent.futures
import cProfile
import os
import re
from collections import *
from collections import Counter, defaultdict, deque, namedtuple
from copy import deepcopy
from datetime import UTC, datetime, timedelta
from functools import *
from functools import cache, cmp_to_key, reduce
from itertools import *
from itertools import combinations, combinations_with_replacement, permutations, product
from pathlib import Path
from typing import override
from unicodedata import normalize
from zoneinfo import ZoneInfo

import bcrypt
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

# from myutils.io_handler import get_input_data, submit_answer
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

    def calc(self):
        return 0

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


if __name__ == "__main__":
    assert Puzzle("test-input.txt").calc() == 0
    print("Tests passed, starting with the puzzle")
    # input_folder = os.environ.get("i18n_inputs")
    # print(Puzzle(f"{input_folder}/i18n2025_day00.txt").calc())
    print(Puzzle("i18n2025_day00.txt").calc())
