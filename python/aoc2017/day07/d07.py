import os
import re
from functools import reduce
from collections import deque, Counter
from pathlib import Path
from myutils.io_handler import get_input_data


class RecursiveCircus:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.process()

    def process(self):
        self.hold = {}
        self.weight = {}

        line_re = re.compile(r"(\w+)\s*\((\d+)\)(.*)")
        for line in self.lines:
            parts = line_re.match(line).groups()
            self.weight[parts[0]] = int(parts[1])
            self.hold[parts[0]] = set(re.findall(r"\w+", parts[2]))

    def bottom_program(self):
        return (self.hold.keys() - reduce(lambda x, y: x.union(y), self.hold.values())).pop()

    def proper_weight_of_unbalanced_program(self):
        nodes = deque(self.hold.keys())
        total_weight = dict()
        while nodes:
            node = nodes.popleft()
            try:
                child_weights = [total_weight[c] for c in self.hold[node]]
            except KeyError:
                nodes.append(node)
                continue

            total_weight[node] = self.weight[node] + sum(child_weights)
            if len(child_weights) > 1 and len(set(child_weights)) > 1:
                weight_counter = Counter([total_weight[k] for k in self.hold[node]])
                unbalanced_value = {k for k, v in weight_counter.items() if v == 1}.pop()
                balanced_value = set(weight_counter.keys() - {unbalanced_value}).pop()
                for held in self.hold[node]:
                    if total_weight[held] == unbalanced_value:
                        return self.weight[held] + balanced_value - unbalanced_value


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = RecursiveCircus(filename)
    assert test.bottom_program() == answer1 or answer1 is None
    assert test.proper_weight_of_unbalanced_program() == answer2 or answer2 is None


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", "tknk", 60)
    print("Tests passed, starting with the puzzle")

    puzzle = RecursiveCircus(data.input_file)
    print(puzzle.bottom_program())
    print(puzzle.proper_weight_of_unbalanced_program())
