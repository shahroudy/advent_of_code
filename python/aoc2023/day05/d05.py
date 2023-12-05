import os
import re
from pathlib import Path


class IfYouGiveASeedAFertilizer:
    def __init__(self, filename):
        line_groups = [
            re.split("\n", g) for g in re.split("\n\n", Path(filename).read_text().strip())
        ]
        self.seeds = list(map(int, re.findall(r"\d+", line_groups[0][0])))

        self.mapping_groups = [
            [list(map(int, re.findall(r"\d+", line))) for line in line_group[1:]]
            for line_group in line_groups[1:]
        ]

    def min_location_for_input_seeds(self):
        locations = []
        for seed in self.seeds:
            i = seed
            for mapping_group in self.mapping_groups:
                for mapping in mapping_group:
                    dest, src, length = mapping
                    if src <= i < src + length:
                        i = dest + i - src
                        break
            locations.append(i)
        return min(locations)

    def min_location_for_input_seed_ranges(self):
        location_counter = 0
        seed_ranges = [
            range(self.seeds[i], self.seeds[i] + self.seeds[i + 1])
            for i in range(0, len(self.seeds) - 1, 2)
        ]
        while True:
            i = location_counter
            for mapping_group in self.mapping_groups[::-1]:  # reversed mapping groups
                for mapping in mapping_group:
                    dest, src, length = mapping
                    if dest <= i < dest + length:  # if i is in the range of destinations
                        i = src + i - dest  # find the source
                        break
            for seed_range in seed_ranges:
                if i in seed_range:
                    return location_counter
            location_counter += 1


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = IfYouGiveASeedAFertilizer(filename)
    assert answer1 is None or test.min_location_for_input_seeds() == answer1
    assert answer2 is None or test.min_location_for_input_seed_ranges() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 35, 46)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day05.txt'
    puzzle = IfYouGiveASeedAFertilizer(input_file)
    print(puzzle.min_location_for_input_seeds())
    print(puzzle.min_location_for_input_seed_ranges())
