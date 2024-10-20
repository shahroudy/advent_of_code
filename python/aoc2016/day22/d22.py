import re
from collections import namedtuple
from itertools import product
from pathlib import Path
from typing import override

from myutils.io_handler import get_input_data
from myutils.search import Search_BFS

State = namedtuple("state", ["zero_loc", "goal_loc", "steps"])


class GridComputing(Search_BFS):
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        data = [list(map(int, re.findall(r"\d+", line))) for line in lines]
        self.df_data = [d for d in data if len(d) > 0]

    def viable_pairs_count(self):
        prod = product(self.df_data, repeat=2)
        return sum(a[:2] != b[:2] and a[3] != 0 and a[3] <= b[4] for a, b in prod)

    @override
    def get_next_states(self, state):
        next_states = []
        zero_loc, goal_loc, steps = state
        for delta in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            new_zero_loc = tuple([delta[i] + zero_loc[i] for i in range(2)])
            if new_zero_loc not in self.nodes:
                continue
            new_goal_loc = goal_loc if new_zero_loc != goal_loc else zero_loc
            next_states.append(State(new_zero_loc, new_goal_loc, steps + 1))
        return next_states

    @override
    def is_goal(self, state):
        return state.goal_loc == (0, 0)

    @override
    def cost(self, state):
        return state.steps

    @override
    def get_result(self, state):
        return state.steps

    @override
    def state_core(self, state):
        return tuple(state.goal_loc) + tuple(state.zero_loc)

    def steps_to_move_goal(self):
        goal_loc = (max(d[0] for d in self.df_data if d[1] == 0), 0)
        zero_loc = [(d[0], d[1]) for d in self.df_data if d[3] == 0].pop()
        self.nodes = {(d[0], d[1]) for d in self.df_data if d[3] <= self.df_data[zero_loc[0]][2]}
        return self.search(initial_state=State(zero_loc, goal_loc, 0))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert GridComputing("sample1.txt").steps_to_move_goal() == 7

    print("Tests passed, starting with the puzzle")

    puzzle = GridComputing(data.input_file)

    print(puzzle.viable_pairs_count())
    print(puzzle.steps_to_move_goal())
