from collections import deque
from pathlib import Path

from myutils.io_handler import get_input_data


class Lobby:
    def __init__(self, filename):
        self.inp = [[int(d) for d in line] for line in Path(filename).read_text().splitlines()]

    def maximum_joltage(self, battery_count):
        total_output_joltage = 0
        for bank in self.inp:
            current, upcoming = bank[:-battery_count], deque(bank[-battery_count:])
            joltage = 0
            while upcoming:
                current.append(upcoming.popleft())
                max_digit = max(current)
                index = current.index(max_digit)
                current = current[index + 1 :]
                joltage = joltage * 10 + max_digit
            total_output_joltage += joltage
        return total_output_joltage


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Lobby("sample1.txt").maximum_joltage(2) == 357
    assert Lobby("sample1.txt").maximum_joltage(12) == 3121910778619

    print("Tests passed, starting with the puzzle")

    puzzle = Lobby(data.input_file)

    print(puzzle.maximum_joltage(2))
    print(puzzle.maximum_joltage(12))
