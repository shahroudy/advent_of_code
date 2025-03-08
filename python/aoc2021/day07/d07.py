from pathlib import Path

from myutils.io_handler import get_input_data


class TreacheryOfWhales:
    def __init__(self, filename):
        self.positions = list(map(int, Path(filename).read_text().split(",")))

    def least_needed_fuel_to_align(self, constant_rate=True):
        needed_fuel = [0]
        for steps in range(1, max(self.positions) + 1):
            needed_fuel.append(needed_fuel[-1] + (1 if constant_rate else steps))
        return min(
            sum(needed_fuel[abs(p - f)] for p in self.positions)
            for f in range(min(self.positions), max(self.positions) + 1)
        )


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert TreacheryOfWhales("sample1.txt").least_needed_fuel_to_align(constant_rate=True) == 37
    assert TreacheryOfWhales("sample1.txt").least_needed_fuel_to_align(constant_rate=False) == 168

    print("Tests passed, starting with the puzzle")

    puzzle = TreacheryOfWhales(data.input_file)

    print(puzzle.least_needed_fuel_to_align(constant_rate=True))
    print(puzzle.least_needed_fuel_to_align(constant_rate=False))
