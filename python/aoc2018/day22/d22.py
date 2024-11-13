import re
from collections import namedtuple
from functools import cache
from itertools import product
from pathlib import Path
from typing import override

from myutils.io_handler import get_input_data
from myutils.search import Search_AStar

State = namedtuple("state", ["x", "y", "equipment", "time"])


class ModeMaze(Search_AStar):
    def __init__(self, filename):
        inputs = [int(n) for n in re.findall(r"[+-]?\d+", Path(filename).read_text())]
        self.depth, self.target = inputs[0], (inputs[1], inputs[2])

    @cache
    def geological_index(self, x, y):
        if (x, y) == self.target:
            return 0
        if y == 0:
            return x * 16807
        if x == 0:
            return y * 48271
        return self.erosion_level(x - 1, y) * self.erosion_level(x, y - 1)

    @cache
    def erosion_level(self, x, y):
        return (self.geological_index(x, y) + self.depth) % 20183

    @cache
    def region_type(self, x, y):
        return self.erosion_level(x, y) % 3

    def total_risk_level(self):
        return sum(
            self.region_type(x, y)
            for x, y in product(range(self.target[0] + 1), range(self.target[1] + 1))
        )

    @override
    def get_next_states(self, state):
        next_states = []
        changed_equipment = 3 - self.region_type(state.x, state.y) - state.equipment
        next_states.append(State(state.x, state.y, changed_equipment, state.time + 7))
        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = state.x + d[0], state.y + d[1]
            if x < 0 or y < 0 or self.region_type(x, y) == state.equipment:
                continue
            next_states.append(State(x, y, state.equipment, state.time + 1))
        return next_states

    @override
    def is_goal(self, state):
        return ((state.x, state.y) == self.target) and (state.equipment == 1)

    @override
    def heuristic(self, state):
        return (
            abs(state.x - self.target[0])
            + abs(state.y - self.target[1])
            + 7 * abs(1 - state.equipment)
        )

    @override
    def get_result(self, state):
        return state.time

    @override
    def cost(self, state):
        return state.time

    @override
    def state_core(self, state):
        return (state.x, state.y, state.equipment)

    def fastest_way_to_reach_the_target(self):
        return self.search(initial_state=State(0, 0, 1, 0))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ModeMaze("sample1.txt").total_risk_level() == 114
    assert ModeMaze("sample1.txt").fastest_way_to_reach_the_target() == 45

    print("Tests passed, starting with the puzzle")

    puzzle = ModeMaze(data.input_file)

    print(puzzle.total_risk_level())
    print(puzzle.fastest_way_to_reach_the_target())
