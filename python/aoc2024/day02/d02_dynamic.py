import re
from collections import namedtuple
from itertools import combinations
from pathlib import Path

from myutils.io_handler import get_input_data

State = namedtuple("state", ["index", "increasing", "failures"])


class SafeSearch:
    def is_safe(self, input, tolerance=0):
        self.input = input
        self.tolerance = tolerance
        self.stack = self.get_initial_states()
        self.history = set(self.stack)
        while self.stack:
            state = self.stack.pop()
            if self.is_goal(state):
                return self.get_result(state)
            for next_state in self.get_next_states(state):
                if next_state not in self.history:
                    self.history.add(next_state)
                    self.stack.append(next_state)
        return False

    def get_initial_states(self):
        states = []
        for start in range(1 + self.tolerance):
            for increasing in [True, False]:
                states.append(State(start, increasing, start))
        return states

    def is_goal(self, state):
        return state.index >= len(self.input) - 1

    def get_result(self, state):
        return True

    def is_acceptable_edge(self, next, previous, increasing):
        if abs(next - previous) > 3:
            return False
        if increasing and next > previous:
            return True
        if not increasing and next < previous:
            return True
        return False

    def get_next_states(self, state):
        index, increasing, failures = state
        for gap in range(1 + self.tolerance - failures):
            next = index + 1 + gap
            if next == len(self.input):
                return [State(next, increasing, failures + gap)]
            if self.is_acceptable_edge(self.input[index], self.input[next], increasing):
                return [State(next, increasing, failures + gap)]
        return []


class RedNosedReports:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.inp = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

    def safe_count(self, tolerance=0):
        # if tolerance == 1:
        #     Path("temp.txt").write_text(
        #         "\n".join([str(int(SafeSearch().is_safe(ls, tolerance))) for ls in self.inp])
        #     )
        return sum(SafeSearch().is_safe(ls, tolerance) for ls in self.inp)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert RedNosedReports("sample1.txt").safe_count(0) == 2
    assert RedNosedReports("sample1.txt").safe_count(1) == 4

    print("Tests passed, starting with the puzzle")

    puzzle = RedNosedReports(data.input_file)

    print(puzzle.safe_count(0))
    print(puzzle.safe_count(1))
