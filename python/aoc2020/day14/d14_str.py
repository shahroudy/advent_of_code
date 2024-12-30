import re
from collections import defaultdict
from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data


class DockingData:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().splitlines()

    def sum_after_value_decode(self):
        memory = defaultdict(int)
        for line in self.lines:
            if line.startswith("mask"):
                mask = line.split(" ")[-1]
            else:
                address, value = map(int, re.findall(r"\d+", line))
                v_str = f"{value:036b}"
                v_str = [m if m != "X" else v for v, m in zip(v_str, mask)]
                memory[address] = int("".join(v_str), 2)
        return sum(memory.values())

    def sum_after_address_decode(self):
        memory = defaultdict(int)
        for line in self.lines:
            if line.startswith("mask"):
                mask = line.split(" ")[-1]
            else:
                address, value = list(map(int, re.findall(r"\d+", line)))
                addr_str = f"{address:036b}"
                addr_str = [m if m != "0" else a for a, m in zip(addr_str, mask)]
                x_count = addr_str.count("X")
                for c in product("01", repeat=x_count):
                    digits = list(c)
                    addr_copy = addr_str.copy()
                    for i, digit in enumerate(addr_copy):
                        if digit == "X":
                            addr_copy[i] = digits.pop()
                    memory[int("".join(addr_copy), 2)] = value
        return sum(memory.values())


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert DockingData("sample1.txt").sum_after_value_decode() == 165
    assert DockingData("sample2.txt").sum_after_address_decode() == 208

    print("Tests passed, starting with the puzzle")

    puzzle = DockingData(data.input_file)

    print(puzzle.sum_after_value_decode())
    print(puzzle.sum_after_address_decode())
