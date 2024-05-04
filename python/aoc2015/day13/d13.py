import re
from collections import defaultdict
from itertools import permutations
from pathlib import Path

from myutils.io_handler import get_input_data


class KnightsOfTheDinnerTable:
    def __init__(self, filename):
        self.n = set()
        self.e = defaultdict(int)
        line_re = re.compile(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).")
        for line in Path(filename).read_text().splitlines():
            first, gain_or_lose, value, second = line_re.match(line).groups()
            self.e[first, second] = int(value) if gain_or_lose == "gain" else -int(value)
            self.n.add(first)

    def happiness(self, p):
        count = len(p)
        return sum(self.e[p[i], p[(i + 1) % count]] + self.e[p[i], p[i - 1]] for i in range(count))

    def optimal_happiness(self):
        first = list(self.n)[0]
        return max(self.happiness([first] + list(p)) for p in permutations(self.n - {first}))

    def optimal_happiness_with_me(self):
        self.n.add("me")
        return self.optimal_happiness()


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert KnightsOfTheDinnerTable("sample1.txt").optimal_happiness() == 330

    print("Tests passed, starting with the puzzle")

    puzzle = KnightsOfTheDinnerTable(data.input_file)

    print(puzzle.optimal_happiness())
    print(puzzle.optimal_happiness_with_me())
