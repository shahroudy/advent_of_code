import re
from collections import defaultdict
from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data


class DockingData:
    def __init__(self, filename):
        self.lines = [re.findall(r"[\dX]+", cmd) for cmd in Path(filename).read_text().splitlines()]

    def sum_after_value_decode(self):
        memory = defaultdict(int)
        for line in self.lines:
            if len(line) == 1:
                mask = line[0]
                zero_mask = int(mask.replace("X", "1"), 2)
                one_mask = int(mask.replace("X", "0"), 2)
            else:
                address, value = map(int, line)
                memory[address] = value & zero_mask | one_mask
        return sum(memory.values())

    def sum_after_address_decode(self):
        memory = defaultdict(int)
        for line in self.lines:
            if len(line) == 1:
                mask = line[0]
                zero_mask = int(mask.replace("0", "1").replace("X", "0"), 2)
                one_mask = int(mask.replace("X", "0"), 2)
                x_values = [1 << (35 - i) for i, c in enumerate(mask) if c == "X"]
            else:
                address, value = map(int, line)
                base_address = address & zero_mask | one_mask
                for bits in product([0, 1], repeat=len(x_values)):
                    memory[base_address + sum(b * x for b, x in zip(bits, x_values))] = value
        return sum(memory.values())


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert DockingData("sample1.txt").sum_after_value_decode() == 165
    assert DockingData("sample2.txt").sum_after_address_decode() == 208

    print("Tests passed, starting with the puzzle")

    puzzle = DockingData(data.input_file)

    print(puzzle.sum_after_value_decode())
    print(puzzle.sum_after_address_decode())
