import os
import re
from collections import defaultdict
from pathlib import Path


class HeardYouLikeRegisters:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.process()

    def process(self):
        line_re = re.compile(r"(\S+)\s*(\S+)\s*(\S+)\s*\S+\s*(.+)")
        self.registers = defaultdict(int)
        self.max_ever = 0
        for line in self.lines:
            reg, cmd, val, cond = line_re.match(line).groups()
            val = int(val)
            if cmd == "dec":
                val *= -1
            if eval(cond, None, self.registers):
                self.registers[reg] += val
            self.max_ever = max(self.max_ever, self.registers[reg])

    def max_register_value(self):
        return max([v for v in self.registers.values() if type(v) is int])

    def max_register_value_over_time(self):
        return self.max_ever


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = HeardYouLikeRegisters(filename)
    assert test.max_register_value() == answer1 or answer1 is None
    assert test.max_register_value_over_time() == answer2 or answer2 is None


if __name__ == "__main__":
    test_samples("sample1.txt", 1, 10)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2017_day08.txt'
    puzzle = HeardYouLikeRegisters(input_file)
    print(puzzle.max_register_value())
    print(puzzle.max_register_value_over_time())
