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
        num = self.nums[step]
        for op in range(self.operations):
            if op == 0:
                nv = value - num
            elif op == 1:
                if value % num == 0:
                    nv = value // num
                else:
                    continue
            else:
                value_str = str(value)
                num_str = str(num)
                if value_str.endswith(num_str) and len(num_str) < len(value_str):
                    nv = int(value_str[: -len(num_str)])
                else:
                    continue
            if nv >= self.target:
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

    def total_calibration(self, operations=2):
        total = 0
        for line in self.inp:
            test_value, first, rest = line[0], line[1], line[2:]
            search = MySearch(nums=rest[::-1], target=first, operations=operations)
            if search.search(initial_state=State(test_value, 0)):
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
