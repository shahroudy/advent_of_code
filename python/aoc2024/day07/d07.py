import re
from collections import namedtuple
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.search import Search_DFS

State = namedtuple("state", ["value", "step"])


class MySearch(Search_DFS):
    def get_next_states(self, state):
        value, step = state
        if step >= len(self.nums):
            return
        for op in range(self.operations):
            if op == 0:
                nv = value + self.nums[step]
            elif op == 1:
                nv = value * self.nums[step]
            else:
                nv = int(str(value) + str(self.nums[step]))
            if nv <= self.target:
                yield State(nv, step + 1)

    def is_goal(self, state):
        return state.step == len(self.nums) and state.value == self.target

    def get_result(self, state):
        return True

    def state_core(self, state):
        return tuple(state)


class BridgeRepair:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.inp = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

    def apply_operation(self, left, op, right):
        if op == 0:
            return left + right
        elif op == 1:
            return left * right
        else:
            return int(str(left) + str(right))

    def total_calibration(self, operations=2):
        total = 0
        for line in self.inp:
            test_value, first, rest = line[0], line[1], line[2:]
            search = MySearch(nums=rest, target=test_value, operations=operations)
            if search.search(initial_state=State(first, 0)):
                total += test_value
        return total


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert BridgeRepair("sample1.txt").total_calibration(2) == 3749
    assert BridgeRepair("sample1.txt").total_calibration(3) == 11387

    print("Tests passed, starting with the puzzle")

    puzzle = BridgeRepair(data.input_file)

    print(puzzle.total_calibration(2))
    print(puzzle.total_calibration(3))
