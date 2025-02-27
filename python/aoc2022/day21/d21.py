import os
from pathlib import Path
from sympy import symbols, Eq, solve
from myutils.io_handler import get_input_data


class MonkeyMath:
    def __init__(self, filename):
        self.eqs = [s.replace(":", "=") for s in Path(filename).read_text().strip().split("\n")]

    def yell_root(self):
        while "root" not in locals():
            for eq in self.eqs:
                try:
                    exec(eq)
                except NameError:
                    pass
        return round(locals()["root"])

    def match_root(self):
        humn = symbols("humn")
        while "root" not in locals():
            for eq in self.eqs:
                try:
                    exec(eq)
                except NameError:
                    pass
        for eq in self.eqs:
            if eq[:4] == "root":
                eq = eq.split()
                return round(solve(Eq(locals()[eq[1]], locals()[eq[3]]))[0])


def test_samples(filename, answer1, answer2):
    test = MonkeyMath(filename)
    assert test.yell_root() == answer1
    assert test.match_root() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 152, 301)

    puzzle = MonkeyMath(data.input_file)
    print(puzzle.yell_root())
    print(puzzle.match_root())
