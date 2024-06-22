from itertools import combinations, count
from math import prod
from pathlib import Path

from myutils.io_handler import get_input_data


class ItHangsInTheBalance:
    def __init__(self, filename):
        self.inp = [int(s) for s in Path(filename).read_text().splitlines()]

    def smallest_quantum_entanglement(self, group_count=3):
        expected_sum = sum(self.inp) // group_count
        for package_count in count():
            solutions = []
            for comb in combinations(self.inp, package_count):
                if sum(comb) == expected_sum:
                    solutions.append(prod(comb))
            if solutions:
                return min(solutions)


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = ItHangsInTheBalance("sample1.txt")
    assert test.smallest_quantum_entanglement(3) == 99
    assert test.smallest_quantum_entanglement(4) == 44

    print("Tests passed, starting with the puzzle")

    puzzle = ItHangsInTheBalance(data.input_file)

    print(puzzle.smallest_quantum_entanglement(3))
    print(puzzle.smallest_quantum_entanglement(4))
