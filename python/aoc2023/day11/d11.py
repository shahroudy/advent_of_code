import os
from itertools import combinations
from pathlib import Path
from myutils.io_handler import get_input_data


class CosmicExpansion:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().splitlines()
        self.galaxies = []
        self.indices = [set(), set()]
        for row, line in enumerate(self.lines):
            for col, ch in enumerate(line):
                if ch == "#":
                    self.galaxies.append((col, row))
                    self.indices[0].add(col)
                    self.indices[1].add(row)

    def sum_distance_between_expanded_galaxies(self, expansion=2):
        mapping = [{}, {}]  # mapping of indices for each dimension (cols and rows)
        for dimension in range(2):
            miss_counter = 0
            for i in range(max(self.indices[dimension]) + 1):
                if i in self.indices[dimension]:
                    mapping[dimension][i] = i + miss_counter
                else:
                    miss_counter += expansion - 1

        return sum(
            [
                sum([abs(mapping[i][first[i]] - mapping[i][second[i]]) for i in range(2)])
                for first, second in combinations(self.galaxies, 2)
            ]
        )


if __name__ == "__main__":
    data = get_input_data(__file__)
    test = CosmicExpansion("sample1.txt")
    assert test.sum_distance_between_expanded_galaxies(2) == 374
    assert test.sum_distance_between_expanded_galaxies(10) == 1030
    assert test.sum_distance_between_expanded_galaxies(100) == 8410

    print("Tests passed, starting with the puzzle")

    puzzle = CosmicExpansion(data.input_file)
    print(puzzle.sum_distance_between_expanded_galaxies())
    print(puzzle.sum_distance_between_expanded_galaxies(1000000))
