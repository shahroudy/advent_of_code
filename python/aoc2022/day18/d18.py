import os
from pathlib import Path
from functools import cache
from myutils.io_handler import get_input_data


class BoilingBoulders:
    def __init__(self, filename):
        lines = Path(filename).read_text().strip().split("\n")
        self.cubes = {tuple(map(int, line.split(","))) for line in lines}
        self.sides = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))

    def adj(self, cube):
        return {tuple([side[i] + cube[i] for i in range(3)]) for side in self.sides}

    def open_sides(self):
        return sum([6 - sum([adj in self.cubes for adj in self.adj(cube)]) for cube in self.cubes])

    @cache
    def exposed_to_lava(self):
        lower_bound = [min(c[dim] for c in self.cubes) - 1 for dim in range(3)]
        higher_bound = [max(c[dim] for c in self.cubes) + 1 for dim in range(3)]

        start = tuple([lower_bound[dim] for dim in range(3)])
        stack = [start]
        exposed = {start}

        while stack:
            cube = stack.pop()
            for adj in self.adj(cube) - exposed - self.cubes:
                if all(lower_bound[dim] <= adj[dim] <= higher_bound[dim] for dim in range(3)):
                    stack.append(adj)
                    exposed.add(adj)
        return exposed

    def reachable_sides(self):
        return sum([adj in self.exposed_to_lava() for cube in self.cubes for adj in self.adj(cube)])


def test_samples(filename, answer1, answer2):
    test = BoilingBoulders(filename)
    assert test.open_sides() == answer1
    assert test.reachable_sides() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 64, 58)

    boiling_boulders = BoilingBoulders(data.input_file)
    print(boiling_boulders.open_sides())
    print(boiling_boulders.reachable_sides())
