import os
import re
from itertools import combinations
from pathlib import Path

import networkx as nx


class Snowverload:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().splitlines()
        self.conn = set()
        self.nodes = set()
        for line in self.lines:
            left, right = re.split(r":", line)
            self.nodes.add(left)
            for r in [r.strip() for r in right.strip().split(" ")]:
                self.conn.add((left, r))
                self.nodes.add(r)

    def cut_three_wires(self):
        G = nx.DiGraph()
        for a, b in self.conn:
            G.add_edge(a, b, capacity=1)
            G.add_edge(b, a, capacity=1)
        for a, b in combinations(self.nodes, 2):
            cut_value, partition = nx.minimum_cut(G, a, b)
            if cut_value == 3 and len(partition) == 2:
                return len(partition[0]) * len(partition[1])


if __name__ == "__main__":
    test = Snowverload("sample1.txt")
    assert test.cut_three_wires() == 54

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day25.txt'
    puzzle = Snowverload(input_file)
    print(puzzle.cut_three_wires())
    # print(puzzle.calc2())
