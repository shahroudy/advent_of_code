import os
from functools import cache
from collections import defaultdict
from itertools import product
from pathlib import Path
import heapq as hq


class BlizzardBasin:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.process_input_map()
        self.ground = set(product(range(1, self.height + 1), range(1, self.width + 1)))

    def process_input_map(self):
        directions = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
        self.blizzards_init = set()
        for row, line in enumerate(self.lines):
            for col, ch in enumerate(line):
                if "##" in line and ch == ".":
                    if row == 0:
                        self.start = (col, row)
                    else:
                        self.goal = (col, row)
                        self.width = row - 1
                        self.height = len(line) - 2
                        return
                else:
                    if ch in "<>v^":
                        self.blizzards_init.add((col, row) + directions[ch])

    @cache
    def blizzards_state(self, iteration):
        if iteration == 0:
            return self.blizzards_init
        else:
            return set(
                [
                    (1 + (x + dx - 1) % self.height, 1 + (y + dy - 1) % self.width, dx, dy)
                    for x, y, dx, dy in self.blizzards_state(iteration - 1)
                ]
            )

    @cache
    def blizzard_locations(self, iteration):
        return set([(b[0], b[1]) for b in self.blizzards_state(iteration)])

    @cache
    def open_ground(self, iteration):
        return {self.start, self.goal}.union(self.ground - self.blizzard_locations(iteration))

    def find_min_path_a_star(self, start_time, start, goal):
        start_state = start + (start_time, 0)
        heap = [0]
        hq.heapify(heap)
        nodes = defaultdict(list)
        nodes[0].append(start_state)
        iteration = start_time
        while True:
            node = nodes[hq.heappop(heap)].pop()
            iteration = node[2] + 1

            for direction in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                child = tuple([node[i] + direction[i] for i in (0, 1)])
                if child == goal:
                    return iteration
                if child in self.open_ground(iteration):
                    cost_value = iteration + sum([abs(child[i] - goal[i]) for i in (0, 1)])
                    new_state = child + (iteration, cost_value)
                    if new_state not in nodes[cost_value]:
                        nodes[cost_value].append(new_state)
                        hq.heappush(heap, cost_value)

    def reach_the_goal_with_snacks(self):
        t1 = self.find_min_path_a_star(0, self.start, self.goal)
        t2 = self.find_min_path_a_star(t1, self.goal, self.start)
        t3 = self.find_min_path_a_star(t2, self.start, self.goal)
        return (t1, t3)


def test_samples(filename, answer):
    test = BlizzardBasin(filename)
    assert test.reach_the_goal_with_snacks() == answer


if __name__ == "__main__":

    test_samples("sample1.txt", (18, 54))

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day24.txt'
    blizzard_basin = BlizzardBasin(input_file)
    print(blizzard_basin.reach_the_goal_with_snacks())
