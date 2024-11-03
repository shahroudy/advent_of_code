import re
from collections import namedtuple
from pathlib import Path
from typing import override

from myutils.io_handler import get_input_data
from myutils.search import Search_DFS_MaxCost

State = namedtuple("state", ["last", "used", "score"])


class ElectromagneticMoat(Search_DFS_MaxCost):
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.inp = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

    @override
    def get_next_states(self, state):
        next_states = []
        last, used, score = state
        for i, pair in enumerate(self.inp):
            if last in pair and not used[i]:
                other = pair[0] if pair[1] == last else pair[1]
                new_used = used.copy()
                new_used[i] = True
                next_states.append(State(other, new_used, score + last + other))
        return next_states

    @override
    def cost(self, state):
        return state.score if self.ignore_length else (sum(state.used), state.score)

    def find_strongest_bridge(self, ignore_length=True):
        self.ignore_length = ignore_length
        score = self.search(initial_state=State(0, [False] * len(self.inp), 0))
        return score if ignore_length else score[1]


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ElectromagneticMoat("sample1.txt").find_strongest_bridge() == 31
    assert ElectromagneticMoat("sample1.txt").find_strongest_bridge(ignore_length=False) == 19

    print("Tests passed, starting with the puzzle")

    puzzle = ElectromagneticMoat(data.input_file)

    print(puzzle.find_strongest_bridge())
    print(puzzle.find_strongest_bridge(ignore_length=False))
