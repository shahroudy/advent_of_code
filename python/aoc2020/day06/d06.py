from functools import reduce
from pathlib import Path

from myutils.io_handler import get_input_data


class CustomCustoms:
    def __init__(self, filename):
        self.inp = [g.strip().splitlines() for g in Path(filename).read_text().split("\n\n")]

    def count_anyone_answered(self):
        return sum(len(set("".join(g))) for g in self.inp)

    def count_everyone_answered(self):
        return sum(len(reduce(set.intersection, [set(line) for line in lg])) for lg in self.inp)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert CustomCustoms("sample1.txt").count_anyone_answered() == 11
    assert CustomCustoms("sample1.txt").count_everyone_answered() == 6

    print("Tests passed, starting with the puzzle")

    puzzle = CustomCustoms(data.input_file)

    print(puzzle.count_anyone_answered())
    print(puzzle.count_everyone_answered())
