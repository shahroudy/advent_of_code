import re
from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data


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
            for ops in product(range(operations), repeat=len(rest)):
                result = first
                for op, value in zip(ops, rest):
                    result = self.apply_operation(result, op, value)
                    if result > test_value:
                        break  # not possible with these operations, break the op,value loop
                else:
                    if result == test_value:
                        total += test_value
                        break  # we found the combination and added it, break the ops loop
        return total


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert BridgeRepair("sample1.txt").total_calibration(2) == 3749
    assert BridgeRepair("sample1.txt").total_calibration(3) == 11387

    print("Tests passed, starting with the puzzle")

    puzzle = BridgeRepair(data.input_file)

    print(puzzle.total_calibration(2))
    print(puzzle.total_calibration(3))
