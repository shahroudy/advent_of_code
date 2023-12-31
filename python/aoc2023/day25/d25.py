import os
import re
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import networkx as nx
from myutils.graph_funcs import path_counter


class Snowverload:
    def __init__(self, filename):
        self.edges = set()
        for line in Path(filename).read_text().strip().splitlines():
            nodes = re.findall(r"(\w+)", line)
            for r in nodes[1:]:
                self.edges.add((nodes[0], r))

    def cut_three_wires(self):
        graph = nx.Graph()
        for edge in self.edges:
            graph.add_edge(*edge, capacity=1)
        for s, t in combinations(graph.nodes, 2):
            cut_value, partition = nx.minimum_cut(graph, s, t)
            if cut_value == 3 and len(partition) == 2:
                return len(partition[0]) * len(partition[1])

    def cut_three_wires_2(self):
        graph = defaultdict(set)
        for a, b in self.edges:
            graph[a].add(b)
            graph[b].add(a)
        nodes = sorted(graph.keys(), key=lambda n: len(graph[n]), reverse=True)
        s1 = set([nodes[0]])
        s2 = set()

        for n in nodes[1:]:
            if sum(nn in s1 for nn in graph[n]) > 2:
                s1.add(n)
            elif sum(nn in s2 for nn in graph[n]) > 2:
                s2.add(n)
            elif path_counter(nodes[0], n, graph, max_counter=4) == 3:
                s2.add(n)
            else:
                s1.add(n)
        return len(s1) * len(s2)


if __name__ == "__main__":
    test = Snowverload("sample1.txt")
    assert test.cut_three_wires() == 54

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day25.txt'
    puzzle = Snowverload(input_file)
    print(puzzle.cut_three_wires())
