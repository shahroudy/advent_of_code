from itertools import cycle
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import read_ints


class ChronalCalibration:
    def __init__(self, filename):
        self.frequency_changes = read_ints(text=Path(filename).read_text())

    def resulting_frequency(self):
        return sum(self.frequency_changes)

    def first_repeated_frequency(self):
        frequency = 0
        seen = {frequency}
        for change in cycle(self.frequency_changes):
            frequency += change
            if frequency in seen:
                return frequency
            seen.add(frequency)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ChronalCalibration("sample1.txt").resulting_frequency() == 3
    assert ChronalCalibration("sample1.txt").first_repeated_frequency() == 2

    print("Tests passed, starting with the puzzle")

    puzzle = ChronalCalibration(data.input_file)

    print(puzzle.resulting_frequency())
    print(puzzle.first_repeated_frequency())
