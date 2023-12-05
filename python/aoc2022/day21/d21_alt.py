import os
from pathlib import Path


class MonkeyMath:
    def __init__(self, filename):
        self.eqs = dict()
        for line in Path(filename).read_text().strip().split("\n"):
            parts = line.replace(":", "").split()
            self.eqs[parts[0]] = parts[1:]
        self.operations = {
            "*": lambda left, right: left * right,
            "+": lambda left, right: left + right,
            "-": lambda left, right: left - right,
            "/": lambda left, right: left / right,
        }
        self.right_operations = {
            "*": lambda var, left: var / left,
            "+": lambda var, left: var - left,
            "-": lambda var, left: left - var,
            "/": lambda var, left: left / var,
        }
        self.left_operations = {
            "*": lambda var, right: var / right,
            "+": lambda var, right: var - right,
            "-": lambda var, right: var + right,
            "/": lambda var, right: var * right,
        }

    def run_equation(self, var, equation):
        if len(equation) == 1:
            self.values[var] = int(equation[0])
            return
        left, op, right = equation
        if var not in self.values:
            if left in self.values and right in self.values:
                self.values[var] = self.operations[op](self.values[left], self.values[right])
        else:
            if left in self.values:
                self.values[right] = self.right_operations[op](self.values[var], self.values[left])
            elif right in self.values:
                self.values[left] = self.left_operations[op](self.values[var], self.values[right])

    def apply_equations(self):
        for var, eq in self.eqs.items():
            self.run_equation(var, eq)

    def yell_root(self):
        self.values = {}
        while "root" not in self.values:
            self.apply_equations()
        return round(self.values["root"])

    def match_root(self):
        self.values = {}
        left, _, right = self.eqs.pop("root")
        del self.eqs["humn"]

        while left not in self.values and right not in self.values:
            self.apply_equations()

        if left in self.values:
            left, right = right, left

        self.values[left] = self.values[right]

        while "humn" not in self.values:
            self.apply_equations()

        return round(self.values["humn"])


def test_samples(filename, answer1, answer2):
    test = MonkeyMath(filename)
    assert test.yell_root() == answer1
    assert test.match_root() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 152, 301)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day21.txt'
    puzzle = MonkeyMath(input_file)
    print(puzzle.yell_root())
    print(puzzle.match_root())
