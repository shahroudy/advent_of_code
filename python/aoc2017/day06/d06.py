import os
import re
from pathlib import Path


class MemoryReallocation:
    def __init__(self, filename):
        self.bank = list(map(int, re.split(r"\s", Path(filename).read_text().strip())))
        self.redistribute()

    def redistribute(self):
        self.history = dict()
        self.counter = 0
        while tuple(self.bank) not in self.history:
            self.history[tuple(self.bank)] = self.counter
            most_blocks = max(self.bank)
            index = self.bank.index(most_blocks)
            self.bank[index] = 0
            for i in range(index + 1, index + most_blocks + 1):
                self.bank[i % len(self.bank)] += 1
            self.counter += 1

    def cycle_count(self):
        return self.counter

    def cycles_from_last_occurrence(self):
        return self.counter - self.history[(tuple(self.bank))]


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = MemoryReallocation(filename)
    assert test.cycle_count() == answer1 or answer1 is None
    assert test.cycles_from_last_occurrence() == answer2 or answer2 is None


if __name__ == "__main__":
    test_samples("sample1.txt", 5, 4)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2017_day06.txt'
    puzzle = MemoryReallocation(input_file)
    print(puzzle.cycle_count())
    print(puzzle.cycles_from_last_occurrence())
