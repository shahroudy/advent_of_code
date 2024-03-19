import re
from itertools import permutations
from pathlib import Path

from myutils.io_handler import get_input_data


class AllInASingleNight:
    def __init__(self, filename):
        cities = set()
        distances = dict()

        line_re = re.compile(r"(\w+)\s+to\s+(\w+)\s+=\s+(\d+)")
        for line in Path(filename).read_text().splitlines():
            c1, c2, d = line_re.match(line).groups()
            cities |= {c1, c2}
            distances[c1, c2] = distances[c2, c1] = int(d)

        self.min_distance, self.max_distance = float("inf"), 0
        for route in permutations(cities):
            distance = sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))
            self.min_distance = min(self.min_distance, distance)
            self.max_distance = max(self.max_distance, distance)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = AllInASingleNight(filename)
    assert answer1 is None or test.min_distance == answer1
    assert answer2 is None or test.max_distance == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 605, 982)

    print("Tests passed, starting with the puzzle")

    puzzle = AllInASingleNight(data.input_file)
    print(puzzle.min_distance)
    print(puzzle.max_distance)
