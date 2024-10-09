from collections import deque, namedtuple
from functools import cache
from pathlib import Path
from typing import override

from myutils.io_handler import get_input_data
from myutils.search import Search_BFS

State = namedtuple("state", ["x", "y", "steps"])


class AMazeOfTwistyLittleCubicles(Search_BFS):
    def __init__(self, filename):
        self.mask4 = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.process(filename)

    def process(self, filename):
        lines = Path(filename).read_text()
        self.inp = int(lines.strip())

    @cache
    def is_open(self, x, y):
        if x < 0 or y < 0:
            return False
        value = (x + y) ** 2 + 3 * x + y + self.inp
        one_count = bin(value).count("1")
        return one_count % 2 == 0

    @override
    def get_next_states(self, state):
        x, y, s = state
        return [
            State(x + dx, y + dy, s + 1) for dx, dy in self.mask4 if self.is_open(x + dx, y + dy)
        ]

    @override
    def is_goal(self, state):
        return state[:2] == self.destination

    @override
    def cost(self, state):
        return state.steps

    @override
    def get_result(self, state):
        return state.steps

    @override
    def state_core(self, state):
        return (state.x, state.y)

    def shortest_path_to(self, *destination):
        self.destination = destination
        return self.search(State(1, 1, 0))

    def locations_reachable_by_50_steps(self):
        initial_state = State(1, 1, 0)
        queue = deque([initial_state])
        history = {
            self.state_core(initial_state),
        }
        while queue:
            state = queue.popleft()
            for next_state in self.get_next_states(state):
                if (core_state := self.state_core(next_state)) in history:
                    continue
                if next_state.steps < 50:
                    queue.append(next_state)
                history.add(core_state)
        return len(history)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert AMazeOfTwistyLittleCubicles("sample1.txt").shortest_path_to(7, 4) == 11

    print("Tests passed, starting with the puzzle")

    puzzle = AMazeOfTwistyLittleCubicles(data.input_file)

    print(puzzle.shortest_path_to(31, 39))
    print(puzzle.locations_reachable_by_50_steps())
