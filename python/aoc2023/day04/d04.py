import os
import re
from pathlib import Path
from myutils.io_handler import get_input_data


class Scratchcards:
    def __init__(self, filename):
        self.matches = {}
        line_re = re.compile(r"\w+\s+(\d+)\s*:\s*(.+)\s*\|\s*(.+)\s*")
        for line in Path(filename).read_text().strip().split("\n"):
            parts = line_re.match(line).groups()
            id = int(parts[0])
            left = set(map(int, re.findall(r"\d+", parts[1])))
            right = set(map(int, re.findall(r"\d+", parts[2])))
            self.matches[id] = len(left & right)

    def sum_of_points(self):
        return sum(2 ** (m - 1) for m in self.matches.values() if m)

    def sum_of_card_copies(self):
        copies = {card: 1 for card in self.matches.keys()}
        for id in range(1, 1 + len(self.matches)):
            for card in range(id + 1, id + 1 + self.matches[id]):
                if card in copies:
                    copies[card] += copies[id]
        return sum(copies.values())


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = Scratchcards(filename)
    assert answer1 is None or test.sum_of_points() == answer1
    assert answer2 is None or test.sum_of_card_copies() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 13, 30)

    print("Tests passed, starting with the puzzle")

    puzzle = Scratchcards(data.input_file)
    print(puzzle.sum_of_points())
    print(puzzle.sum_of_card_copies())
