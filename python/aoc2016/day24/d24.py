from collections import namedtuple
from pathlib import Path
from typing import override

from myutils.io_handler import get_input_data
from myutils.search import Search_BFS

State = namedtuple("state", ["x", "y", "steps", "goals"])


class AirDuctSpelunking(Search_BFS):
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.map = dict()
        self.goals = dict()
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                self.map[(col, row)] = ch
                if ch.isnumeric():
                    n = int(ch)
                    if n > 0:
                        self.goals[col, row] = int(ch)
                    else:
                        self.zero = (col, row)

    @override
    def get_next_states(self, state):
        next_states = []
        goals = state.goals
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = state.x + dx, state.y + dy
            if (x, y) in self.map and self.map[(x, y)] != "#":
                if (x, y) in self.goals and self.goals[(x, y)] not in goals:
                    if self.goals[(x, y)] == 0 and len(goals) < len(self.goals) - 1:
                        new_goals = goals
                    else:
                        new_goals = goals + [self.goals[(x, y)]]
                        new_goals.sort()
                else:
                    new_goals = goals
                next_states.append(State(x, y, state.steps + 1, new_goals))
        return next_states

    @override
    def is_goal(self, state):
        return len(state.goals) == len(self.goals)

    @override
    def get_result(self, state):
        return state.steps

    @override
    def state_core(self, state):
        return (state.x, state.y, tuple(state.goals))

    def min_steps_to_meet_all_numbers(self):
        return self.search(State(*self.zero, 0, []))

    def min_steps_to_meet_all_numbers_and_return(self):
        self.goals[self.zero] = 0
        return self.min_steps_to_meet_all_numbers()


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert AirDuctSpelunking("sample1.txt").min_steps_to_meet_all_numbers() == 14

    print("Tests passed, starting with the puzzle")

    puzzle = AirDuctSpelunking(data.input_file)

    print(puzzle.min_steps_to_meet_all_numbers())
    print(puzzle.min_steps_to_meet_all_numbers_and_return())
