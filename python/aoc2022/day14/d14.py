import os
from itertools import product
from pathlib import Path
from myutils.io_handler import get_input_data


class RegolithReservoir:
    def __init__(self, filename):
        self.rocks = set()
        self.maxy = 0

        for line in Path(filename).read_text().strip().split("\n"):
            pre = None
            for point in line.split():
                if point == "->":
                    continue
                cur = list(map(int, point.split(",")))
                self.maxy = max(self.maxy, cur[1])
                if pre:
                    for i, j in product(
                        *[range(min(cur[d], pre[d]), max(cur[d], pre[d]) + 1) for d in [0, 1]]
                    ):
                        self.rocks.add((i, j))
                pre = cur
        self.maxy += 1

    def rested_sands(self, have_floor=False):
        sand_count = 0
        rocks = self.rocks.copy()
        while True:
            current_position = (500, 0)
            while current_position[1] < self.maxy:
                for x in [0, -1, 1]:
                    next_position = (current_position[0] + x, current_position[1] + 1)
                    if next_position not in rocks:
                        current_position = next_position
                        break
                else:
                    if current_position in rocks:
                        return sand_count
                    rocks.add(current_position)
                    break
            if current_position[1] == self.maxy:
                if have_floor:
                    rocks.add(current_position)
                else:
                    return sand_count
            sand_count += 1


def test_samples(filename, answer1, answer2):
    test = RegolithReservoir(filename)
    assert test.rested_sands(have_floor=False) == answer1
    assert test.rested_sands(have_floor=True) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 24, 93)

    regolith_reservoir = RegolithReservoir(data.input_file)
    print(regolith_reservoir.rested_sands(have_floor=False))
    print(regolith_reservoir.rested_sands(have_floor=True))
