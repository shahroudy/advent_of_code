from itertools import combinations
from pathlib import Path

from myutils.io_handler import get_input_data


class CodeChronicle:
    def __init__(self, filename):
        self.patterns = []
        for pattern_txt in Path(filename).read_text().strip().split("\n\n"):
            pattern = set()
            for row, line in enumerate(pattern_txt.split("\n")):
                for col, ch in enumerate(line):
                    if ch == "#":
                        pattern.add((col, row))
            self.patterns.append(pattern)

    def count_fit_pairs(self):
        return sum(not a.intersection(b) for a, b in combinations(self.patterns, 2))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert CodeChronicle("sample1.txt").count_fit_pairs() == 3

    print("Tests passed, starting with the puzzle")

    puzzle = CodeChronicle(data.input_file)

    print(puzzle.count_fit_pairs())
