import os
from functools import cache
from pathlib import Path


class PlanetOfDiscord:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().splitlines()
        self.process_map()
        self.directions = {"e": (1, 0), "w": (-1, 0), "n": (0, -1), "s": (0, 1)}

    def process_map(self):
        self.map = dict()
        for row, line in enumerate(self.lines):
            for col, ch in enumerate(line):
                self.map[(col, row)] = ch
        self.rows, self.cols = row + 1, col + 1

    @cache
    def get_value(self, pos):
        col, row = pos
        n = row * self.cols + col
        return 2**n

    def first_repeating_biodiversity_rating(self):
        bugged_cells = set()
        edges = {}
        for pos, ch in self.map.items():
            value = self.get_value(pos)
            if ch == "#":
                bugged_cells.add(value)
            edges[value] = []
            for dir in self.directions.values():
                neighbor = (pos[0] + dir[0], pos[1] + dir[1])
                if neighbor in self.map:
                    neighbor_value = self.get_value(neighbor)
                    edges[value].append(neighbor_value)

        history = {sum(bugged_cells)}
        while True:
            next_bugged_cells = set()
            for cell, neighbors in edges.items():
                bug_count = sum([n in bugged_cells for n in neighbors])
                if cell in bugged_cells:
                    if bug_count == 1:
                        next_bugged_cells.add(cell)
                else:
                    if bug_count in [1, 2]:
                        next_bugged_cells.add(cell)
            bugged_cells = next_bugged_cells
            biodiversity_rate = sum(bugged_cells)
            if biodiversity_rate in history:
                return biodiversity_rate
            else:
                history.add(biodiversity_rate)

    def bug_count_in_recursing_grids(self, iterations=10):
        bugged_cells = set()
        edges = {}
        mid_col, mid_row = self.cols // 2, self.rows // 2
        mid_point = (mid_col, mid_row)
        for pos, ch in self.map.items():
            if pos == mid_point:
                continue
            if ch == "#":
                bugged_cells.add((*pos, 0))
            edges[pos] = []
            for dir in self.directions.values():
                neighbor = (pos[0] + dir[0], pos[1] + dir[1])
                if neighbor in self.map and neighbor != mid_point:
                    edges[pos].append((*neighbor, 0))
        for c in range(self.cols):
            edges[(c, 0)].append((mid_col, mid_row - 1, 1))
            edges[(mid_col, mid_row - 1)].append((c, 0, -1))
            edges[(c, self.rows - 1)].append((mid_col, mid_row + 1, 1))
            edges[(mid_col, mid_row + 1)].append((c, self.rows - 1, -1))
        for r in range(self.rows):
            edges[(0, r)].append((mid_col - 1, mid_row, 1))
            edges[(mid_col - 1, mid_row)].append((0, r, -1))
            edges[(self.cols - 1, r)].append((mid_col + 1, mid_row, 1))
            edges[(mid_col + 1, mid_row)].append((self.cols - 1, r, -1))

        for _ in range(iterations):
            to_check = {(x, y, z + c) for a, b, c in bugged_cells for x, y, z in edges[(a, b)]}
            next_bugged_cells = set()
            for cell in to_check | bugged_cells:
                x, y, z = cell
                bug_count = sum([(n[0], n[1], n[2] + z) in bugged_cells for n in edges[(x, y)]])
                if cell in bugged_cells:
                    if bug_count == 1:
                        next_bugged_cells.add(cell)
                else:
                    if bug_count in [1, 2]:
                        next_bugged_cells.add(cell)
            bugged_cells = next_bugged_cells
        return len(bugged_cells)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = PlanetOfDiscord(filename)
    assert answer1 is None or test.first_repeating_biodiversity_rating() == answer1
    assert answer2 is None or test.bug_count_in_recursing_grids() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 2129920, 99)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2019_day24.txt'
    puzzle = PlanetOfDiscord(input_file)
    print(puzzle.first_repeating_biodiversity_rating())
    print(puzzle.bug_count_in_recursing_grids(iterations=200))
