import os
from collections import Counter
from functools import cache
from itertools import product
from pathlib import Path


class UnstableDiffusion:
    def __init__(self, filename):
        lines = Path(filename).read_text().strip().split("\n")
        self.elves = set()
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                if ch == "#":
                    self.elves.add((col, row))
        self.eight_directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
        self.four_directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    @cache
    def adj_directions(self, dir):
        if dir[0]:
            return [(dir[0], dir[1] + i) for i in range(-1, 2)]
        else:
            return [(dir[0] + i, dir[1]) for i in range(-1, 2)]

    def dim_range(self, dim):
        return range(min([e[dim] for e in self.elves]), 1 + max([e[dim] for e in self.elves]))

    def print_map(self):
        print()
        for y in self.dim_range(1):
            for x in self.dim_range(0):
                print("#" if (x, y) in self.elves else ".", end="")
            print()

    def move_elves_one_step(self):
        moving_elves = []
        for elve in self.elves:
            for direction in self.eight_directions:
                neighbour = (direction[0] + elve[0], direction[1] + elve[1])
                if neighbour in self.elves:
                    moving_elves.append(elve)
                    break
        destinations = {}
        for elve in moving_elves:
            for direction in self.four_directions:
                for adj in self.adj_directions(direction):
                    if (adj[0] + elve[0], adj[1] + elve[1]) in self.elves:
                        break
                else:
                    destinations[elve] = (elve[0] + direction[0], elve[1] + direction[1])
                    break
        destination_counter = Counter(destinations.values())
        moving = False
        for elve, direction in destinations.items():
            c = destination_counter[destinations[elve]]
            if c == 1:
                self.elves.remove(elve)
                self.elves.add(destinations[elve])
                moving = True
        self.four_directions = self.four_directions[1:] + self.four_directions[:1]
        return moving

    def spread_the_elves(self, visualize=False):
        iteration = 1
        while self.move_elves_one_step():
            if visualize:
                self.print_map()
            if iteration == 10:
                product_range = product(self.dim_range(0), self.dim_range(1))
                empty_ground_tiles = sum([(x, y) not in self.elves for x, y in product_range])
            iteration += 1
        return (empty_ground_tiles, iteration)


def test_samples(filename, answer):
    test = UnstableDiffusion(filename)
    assert test.spread_the_elves() == answer


if __name__ == "__main__":

    test_samples("sample1.txt", (110, 20))

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day23.txt'
    unstable_diffusion = UnstableDiffusion(input_file)
    print(unstable_diffusion.spread_the_elves())
