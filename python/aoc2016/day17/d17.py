import hashlib
from collections import deque, namedtuple
from pathlib import Path

from myutils.io_handler import get_input_data

State = namedtuple("state", ["x", "y", "path"])


class TwoStepsForward:
    def __init__(self, filename):
        self.directions = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
        self.inp = Path(filename).read_text().strip()

    def get_next_states(self, state):
        next_states = []
        hash = hashlib.md5((self.inp + state.path).encode()).hexdigest()
        for i, (k, v) in enumerate(self.directions.items()):
            x, y = state.x + v[0], state.y + v[1]
            if hash[i] in "bcdef" and 0 <= x < 4 and 0 <= y < 4:
                next_states.append(State(x, y, state.path + k))
        return next_states

    def is_goal(self, state):
        return state.x == 3 and state.y == 3

    def shortest_path(self):
        self.queue = deque([State(0, 0, "")])
        while self.queue:
            state = self.queue.popleft()
            for next_state in self.get_next_states(state):
                if self.is_goal(next_state):
                    return next_state.path
                self.queue.append(next_state)

    def length_of_longest_path(self):
        longest = 0
        self.queue = deque([State(0, 0, "")])
        while self.queue:
            state = self.queue.popleft()
            for next_state in self.get_next_states(state):
                if self.is_goal(next_state):
                    longest = max(longest, len(next_state.path))
                else:
                    self.queue.append(next_state)
        return longest


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = TwoStepsForward(filename)
    assert answer1 is None or test.shortest_path() == answer1
    assert answer2 is None or test.length_of_longest_path() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", "DDRRRD", 370)
    test_samples("sample2.txt", "DDUDRLRRUDRD", 492)
    test_samples("sample3.txt", "DRURDRUDDLLDLUURRDULRLDUUDDDRR", 830)

    print("Tests passed, starting with the puzzle")

    puzzle = TwoStepsForward(data.input_file)

    print(puzzle.shortest_path())
    print(puzzle.length_of_longest_path())
