from pathlib import Path

from myutils.io_handler import get_input_data


class BinaryBoarding:
    def __init__(self, filename):
        self.numbers = {
            int("".join(["0" if ch in "FL" else "1" for ch in line]), 2)
            for line in Path(filename).read_text().splitlines()
        }

    def maximum_seat_id(self):
        return max(self.numbers)

    def id_of_my_seat(self):
        return (set(range(min(self.numbers), max(self.numbers))) - self.numbers).pop()


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert BinaryBoarding("sample1.txt").maximum_seat_id() == 357
    assert BinaryBoarding("sample2.txt").maximum_seat_id() == 820

    print("Tests passed, starting with the puzzle")

    puzzle = BinaryBoarding(data.input_file)

    print(puzzle.maximum_seat_id())
    print(puzzle.id_of_my_seat())
