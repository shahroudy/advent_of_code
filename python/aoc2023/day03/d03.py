import os
from pathlib import Path


class GearRatios:
    def __init__(self, filename):
        self.numbers = []
        self.symbols = []
        self.stars = []
        for row, line in enumerate(Path(filename).read_text().strip().split("\n")):
            number_string = ""
            cols = []
            for col, ch in enumerate(line):
                if ch.isdigit():
                    number_string += ch
                    cols.append(col)
                else:
                    if number_string:
                        self.numbers.append([int(number_string), row, cols])
                        number_string = ""
                        cols = []
                    if ch != ".":
                        self.symbols.append((row, col))
                        if ch == "*":
                            self.stars.append((row, col))
            if number_string:
                self.numbers.append([int(number_string), row, cols])

    def adjacent(self, row, col):
        return [(row + i, col + j) for i in range(-1, 2) for j in range(-1, 2) if i or j]

    def sum_of_part_numbers_in_engine_schematic(self):
        result = 0
        for n, row, cols in self.numbers:
            for c in cols:
                if any([(m in self.symbols) for m in self.adjacent(row, c)]):
                    result += n
                    break

        return result

    def sum_of_gear_ratios(self):
        result = 0
        for star in self.stars:
            adjacent_numbers = []
            for n, row, cols in self.numbers:
                for col in cols:
                    if star in self.adjacent(row, col):
                        adjacent_numbers.append(n)
                        break
                if len(adjacent_numbers) > 2:
                    break
            if len(adjacent_numbers) == 2:
                result += adjacent_numbers[0] * adjacent_numbers[1]
        return result


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = GearRatios(filename)
    assert answer1 is None or test.sum_of_part_numbers_in_engine_schematic() == answer1
    assert answer2 is None or test.sum_of_gear_ratios() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 4361, 467835)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day03.txt'
    puzzle = GearRatios(input_file)
    print(puzzle.sum_of_part_numbers_in_engine_schematic())
    print(puzzle.sum_of_gear_ratios())
