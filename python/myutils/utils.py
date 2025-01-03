import operator
import re
from collections import defaultdict, namedtuple
from functools import reduce

from myutils.geometry import *
from myutils.geometry import Point, Point3D
from myutils.search import (
    Search,
    Search_AStar,
    Search_BFS,
    Search_DFS,
    Search_DFS_MaxCost,
    Search_Dijkstra,
    Search_MinHeap,
)


class MySearch(Search):
    State = namedtuple("state", ["x", "y"])

    def get_next_states(self, state):
        next_states = []
        # state = State(1, 2)
        # next_states.append(state)
        return next_states

    def is_goal(self, state):
        pass

    def cost(self, state):
        pass

    def heuristic(self, state):
        pass

    def get_result(self, state):
        pass

    def state_core(self, state):
        """
        Core presentation of the state, in an immutable form.
        Used to avoid repetition of the same state in the search.

        Args:
            state: The state to be processed.

        Returns:
            The immutable core state.
        """
        return state


class MapSearch(Search_Dijkstra):
    State = namedtuple("state", ["point", "steps", "cost"])

    def get_next_states(self, state):
        point, steps, cost = state
        for n in point.n4():
            if hasattr(self, "rows") and hasattr(self, "cols"):
                if not n.is_inside(self):
                    continue
            if hasattr(self, "nodes"):
                if n not in self.nodes:
                    continue
            if hasattr(self, "walls"):
                if n in self.walls:
                    continue
            yield self.State(n, steps + 1, cost + 1)

    def cost(self, state):
        return state.cost

    def state_core(self, state):
        return state.point

    # def heuristic(self, state):
    #     return state.point.manhattan(self.goal)

    # def get_result(self, state):
    #     return state.cost

    # def is_goal(self, state):
    #     return state.point == self.goal


def multiply(elements):
    return reduce(operator.mul, elements, 1)


def process(self):
    lines = self.input_text.splitlines()
    self.inp = []

    # self.inp = [tuple(map(int, re.split(r"\D", line))) for line in self.lines]

    # line_re = re.compile(r"(\d+)\s*(\d+):(\d+).*")
    for line in lines:
        # parts = line_re.match(line).groups()
        parts = re.split(r"-, ", line)
        # a = parts[0].strip().split(" ")
        # a = list(map(int, re.findall(r"\d+", parts[0])))
        self.inp.append(parts)


def recursive_split(self, seps, text=None, strip=True):
    if text is None:
        self.inp = recursive_split(self, seps, self.input_text)
        return
    if not seps:
        return text
    return [
        recursive_split(self, seps[1:], x.strip() if strip else x, strip)
        for x in text.split(seps[0])
    ]


def find_all_re(self, pattern, text=None):
    pattern = re.compile(pattern)
    if text is None:
        self.inp = pattern.findall(self.input_text)
    else:
        return pattern.findall(text)


def find_all_per_line_re(self, pattern, text=None):
    pattern = re.compile(pattern)
    if text is None:
        self.inp = [pattern.findall(line) for line in self.input_text.splitlines()]
    else:
        return [pattern.findall(line) for line in text.splitlines()]


def process_map_plain(self):
    lines = self.input_text.splitlines()
    self.inp = dict()
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            self.inp[Point(col, row)] = ch
    self.rows, self.cols = row + 1, col + 1


def process_map_dict_of_sets_of_points(self):
    lines = self.input_text.splitlines()
    sets = defaultdict(set)
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            sets[ch].add(Point(col, row))
    self.inp = dict(sets)
    self.rows, self.cols = row + 1, col + 1


def process_map_dict_of_sets_of_3D_points(self):
    sets = defaultdict(set)
    for z, plane in enumerate(self.input_text.split("\n\n")):
        for y, line in enumerate(plane.splitlines()):
            for x, ch in enumerate(line):
                sets[ch].add(Point3D(x, y, z))
    self.inp = dict(sets)
    self.planes, self.rows, self.cols = z + 1, y + 1, x + 1


def read_ints(self):
    self.inp = [int(n) for n in re.findall(r"[+-]?\d+", self.input_text)]


def read_line_groups(self):
    self.inp = [re.split("\n", g) for g in re.split("\n\n", self.input_text.strip())]


def read_int_line_groups(self):
    self.inp = [
        [int(n) for n in re.split("\n", g)] for g in re.split("\n\n", self.input_text.strip())
    ]


def process_int_list(self):
    lines = self.input_text.splitlines()
    self.inp = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]


def process_int_int_dict(self):
    lines = self.input_text.splitlines()
    self.inp = {}
    for line in lines:
        parts = list(map(int, re.findall(r"-?\d+", line)))
        self.inp[parts[0]] = parts[1]


def process_int_list_dict(self):
    lines = self.input_text.splitlines()
    self.inp = {}
    for line in lines:
        parts = list(map(int, re.findall(r"-?\d+", line)))
        self.inp[parts[0]] = parts[1:]


def print_with_color(self, text, text_color="#FFFFFF", back_color="#000000", end="\n"):
    from colored import attr, bg, fg

    color = fg(text_color)
    back = bg(back_color)
    reset = attr("reset")
    print(f"{color + back}" + text + f"{reset}", end=end)


def get_sample_number(filename):
    number = re.match(r"sample(\d+).txt", filename)
    if number:
        return int(number.group(1))
    return 0  # actual input file, not a sample test


# Example usage
assert multiply([1, 2, 3, 4, 5]) == 120
