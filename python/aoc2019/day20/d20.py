import heapq
import os
from collections import defaultdict
from copy import deepcopy
from pathlib import Path

from myutils.graph_funcs import shortest_path, simplify_graph


class DonutMaze:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().splitlines()
        self.process_map()
        self.process_graph()

    def process_map(self):
        self.map = dict()
        for row, line in enumerate(self.lines):
            for col, ch in enumerate(line):
                self.map[(col, row)] = ch

    def process_graph(self):
        self.graph = defaultdict(list)
        self.portals = defaultdict(list)
        for p in self.map:
            if self.map[p] != ".":
                continue
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                p2 = tuple(map(sum, zip(p, d)))
                if self.map[p2] == ".":
                    self.graph[p].append(p2)
                elif self.map[p2].isalpha():
                    p3 = tuple(map(sum, zip(p2, d)))
                    label = self.map[p2] + self.map[p3]
                    if -1 in d:
                        label = label[::-1]
                    if label == "AA":
                        self.start = p
                    elif label == "ZZ":
                        self.end = p
                    else:
                        self.portals[label].append(p)
        self.graph, self.portals = dict(self.graph), dict(self.portals)

    def steps_in_single_space(self):
        graph = deepcopy(self.graph)
        for a, b in self.portals.values():
            graph[a].append(b)
            graph[b].append(a)
        return shortest_path(self.start, self.end, *simplify_graph(graph))[0]

    def steps_in_recursive_spaces(self):
        cols, rows = {v[0] for v in self.graph}, {v[1] for v in self.graph}
        out_cols, out_rows = {min(cols), max(cols)}, {min(rows), max(rows)}
        outer_portals = dict()
        inner_portals = dict()
        for portal, (u, v) in self.portals.items():
            outer_portals[portal], inner_portals[portal] = (
                (u, v) if u[0] in out_cols or u[1] in out_rows else (v, u)
            )
        outer_labels = {v: k for k, v in outer_portals.items()}
        inner_labels = {v: k for k, v in inner_portals.items()}
        graph, weights = simplify_graph(self.graph)

        pq = [(0, (self.start, 0))]
        dist = defaultdict(lambda: float("inf"))
        dist[(self.start, 0)] = 0
        # Looping until the priority queue becomes empty
        while pq:
            # The first element in the tuple is the minimum distance vertex
            # Extract it from the priority queue
            _, (u, u_level) = heapq.heappop(pq)
            u_dist = dist[(u, u_level)]
            # Iterate over all adjacent vertices of a vertex
            neighbors = []
            for v in graph[u]:
                neighbors.append((v, u_level, u_dist + weights[(u, v)]))
            if u in inner_labels.keys():
                neighbors.append((outer_portals[inner_labels[u]], u_level + 1, u_dist + 1))
            elif u in outer_labels.keys() and u_level > 0:
                neighbors.append((inner_portals[outer_labels[u]], u_level - 1, u_dist + 1))
            for v, v_level, d in neighbors:
                if dist[(v, v_level)] > d:
                    # Update the distance of v
                    dist[(v, v_level)] = d
                    if d < dist[(self.end, 0)]:
                        heapq.heappush(pq, (d, (v, v_level)))
        return dist[(self.end, 0)]


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = DonutMaze(filename)
    assert answer1 is None or test.steps_in_single_space() == answer1
    assert answer2 is None or test.steps_in_recursive_spaces() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 23, 26)
    test_samples("sample2.txt", 58, None)
    test_samples("sample3.txt", None, 396)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2019_day20.txt'
    puzzle = DonutMaze(input_file)
    print(puzzle.steps_in_single_space())
    print(puzzle.steps_in_recursive_spaces())
