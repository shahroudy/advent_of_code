import os
import re
from collections import defaultdict
from pathlib import Path
from copy import deepcopy


class SupplyStacks:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().split("\n")
        self.process()

    def process(self):
        separator = self.lines.index("")
        init_state = self.lines[:separator]
        moves = [line for line in self.lines[separator:] if line]

        digits_line = init_state[-1]
        cols = {int(digits_line[i]): i for i in range(len(digits_line)) if digits_line[i].isdigit()}
        self.number_of_stacks = max(cols.keys())

        self.stacks = defaultdict(list)
        for line in reversed(init_state[:-1]):
            for s, c in cols.items():
                if c < len(line) and line[c] != " ":
                    self.stacks[s].append(line[c])

        move_re = re.compile(r"move (\d+) from (\d+) to (\d+).*")
        self.moves = [list(map(int, move_re.match(move).groups())) for move in moves]

    def move_one_by_one(self):
        stacks = deepcopy(self.stacks)
        for n, src, dest in self.moves:
            for _ in range(n):
                stacks[dest].append(stacks[src].pop())
        return "".join([stacks[i + 1][-1] for i in range(self.number_of_stacks)])

    def move_them_together(self):
        stacks = deepcopy(self.stacks)
        for n, src, dest in self.moves:
            temp = []
            for _ in range(n):
                temp.append(stacks[src].pop())
            while temp:
                stacks[dest].append(temp.pop())
        return "".join([stacks[i + 1][-1] for i in range(self.number_of_stacks)])


def test_samples(filename, answer1, answer2):
    test = SupplyStacks(filename)
    assert test.move_one_by_one() == answer1
    assert test.move_them_together() == answer2


if __name__ == "__main__":

    test_samples("sample1.txt", "CMZ", "MCD")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day05.txt'
    supply_stacks = SupplyStacks(input_file)
    print(supply_stacks.move_one_by_one())
    print(supply_stacks.move_them_together())
