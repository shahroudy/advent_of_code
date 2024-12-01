import os
from functools import cache
from pathlib import Path
from myutils.io_handler import get_input_data


class PointOfIncidence:
    def __init__(self, filename):
        self.mirrors = [g.splitlines() for g in Path(filename).read_text().strip().split("\n\n")]

    @cache
    def difference_count(self, row1, row2):
        return sum([row1[i] != row2[i] for i in range(len(row1))])

    def find_horizontal_reflection(self, mirror, smudge_count=0):
        for row in range(0, len(mirror) - 1):
            diff_sum = 0
            for r in range(min(row + 1, len(mirror) - row - 1)):
                diff_sum += self.difference_count(mirror[row + r + 1], mirror[row - r])
                if diff_sum > smudge_count:
                    break
            if diff_sum == smudge_count:
                return row + 1
        return 0

    def sum_of_reflections(self, smudge_count=0):
        return sum(
            [
                100 * self.find_horizontal_reflection(mirror, smudge_count)
                + self.find_horizontal_reflection(list(zip(*mirror)), smudge_count)
                for mirror in self.mirrors
            ]
        )


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = PointOfIncidence(filename)
    assert answer1 is None or test.sum_of_reflections() == answer1
    assert answer2 is None or test.sum_of_reflections(smudge_count=1) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 405, 400)

    print("Tests passed, starting with the puzzle")

    puzzle = PointOfIncidence(data.input_file)
    print(puzzle.sum_of_reflections())
    print(puzzle.sum_of_reflections(smudge_count=1))
