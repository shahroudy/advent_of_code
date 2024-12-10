import operator
import re
from collections import defaultdict, namedtuple
from functools import reduce

from myutils.geometry import *
from myutils.search import Search, Search_AStar, Search_BFS, Search_DFS, Search_MinHeap

State = namedtuple("state", ["x", "y"])


class MySearch(Search):
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


def recursive_split(self, seps, inp=None, strip=True):
    if inp is None:
        self.inp = recursive_split(self, seps, self.input_text)
        return
    if not seps:
        return inp
    return [
        recursive_split(self, seps[1:], x.strip() if strip else x, strip)
        for x in inp.split(seps[0])
    ]


def find_all_re(self):
    pattern = re.compile(r"(\d+)")
    self.inp = pattern.findall(self.input_text)


def find_all_per_line_re(self):
    pattern = re.compile(r"(\d+)")
    self.inp = [pattern.findall(line) for line in self.input_text.splitlines()]


def process_map_plain(self):
    lines = self.input_text.splitlines()
    self.map = dict()
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            self.map[(col, row)] = ch
    self.rows, self.cols = row + 1, col + 1


def process_map_dict_of_sets_of_points(self):
    lines = self.input_text.splitlines()
    sets = defaultdict(set)
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            if ch != ".":
                sets[ch].add(Point(col, row))
    self.map = dict(sets)
    self.rows, self.cols = row + 1, col + 1


def process_map_dict_of_sets_of_3D_points(self):
    sets = defaultdict(set)
    for z, plane in enumerate(self.input_text.split("\n\n")):
        for y, line in enumerate(plane.splitlines()):
            for x, ch in enumerate(line):
                if ch != ".":
                    sets[ch].add(Point3D(x, y, z))
    self.map = dict(sets)
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


# Example usage
assert multiply([1, 2, 3, 4, 5]) == 120
