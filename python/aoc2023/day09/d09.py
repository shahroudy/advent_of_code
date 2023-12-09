import os
import re
from pathlib import Path


class MirageMaintenance:
    def __init__(self, filename):
        self.histories = [
            list(map(int, re.findall(r"-?\d+", line)))
            for line in Path(filename).read_text().splitlines()
        ]

        self.sum_firsts = self.sum_lasts = 0
        for history in self.histories:
            dif = history
            first = last = 0
            sign = -1
            while any(dif):
                last += dif[-1]
                first = dif[0] - first
                sign *= -1
                dif = [dif[i + 1] - dif[i] for i in range(len(dif) - 1)]
            self.sum_lasts += last
            self.sum_firsts += first * sign


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = MirageMaintenance(filename)
    assert answer1 is None or test.sum_lasts == answer1
    assert answer2 is None or test.sum_firsts == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 114, 2)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day09.txt'
    puzzle = MirageMaintenance(input_file)
    print(puzzle.sum_lasts)
    print(puzzle.sum_firsts)
