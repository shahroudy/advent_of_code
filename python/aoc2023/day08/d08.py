import os
import re
from math import lcm
from pathlib import Path


class HauntedWasteland:
    def __init__(self, filename):
        lines = Path(filename).read_text().strip().split("\n")
        self.inp = {}
        self.steps = lines[0].strip()
        for line in lines[2:]:
            nodes = re.findall(r"\w+", line)
            self.inp[nodes[0]] = (nodes[1], nodes[2])

    def count_steps(self, cur, end):
        counter = 0
        while cur not in end:
            for step in self.steps:
                counter += 1
                cur = self.inp[cur][0 if step == "L" else 1]
        return counter

    def navigate_human(self):
        return self.count_steps("AAA", ["ZZZ"])

    def navigate_ghost(self):
        start_nodes = [node for node in self.inp if node[-1] == "A"]
        end_nodes = [node for node in self.inp if node[-1] == "Z"]
        return lcm(*[self.count_steps(s, end_nodes) for s in start_nodes])


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = HauntedWasteland(filename)
    assert answer1 is None or test.navigate_human() == answer1
    assert answer2 is None or test.navigate_ghost() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 2, None)
    test_samples("sample2.txt", 6, None)
    test_samples("sample3.txt", None, 6)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day08.txt'
    puzzle = HauntedWasteland(input_file)
    print(puzzle.navigate_human())
    print(puzzle.navigate_ghost())
