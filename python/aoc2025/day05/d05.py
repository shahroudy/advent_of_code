from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import read_ints, read_ranges


class Cafeteria:
    def __init__(self, filename):
        ranges_text, ids_text = Path(filename).read_text().split("\n\n")
        self.ids = read_ints(ids_text)
        self.ranges = read_ranges(ranges_text)

    def available_fresh_ingredients_count(self):
        return sum(id in self.ranges for id in self.ids)

    def all_fresh_ingredients_count(self):
        return self.ranges.length()


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Cafeteria("sample1.txt").available_fresh_ingredients_count() == 3
    assert Cafeteria("sample1.txt").all_fresh_ingredients_count() == 14

    print("Tests passed, starting with the puzzle")

    puzzle = Cafeteria(data.input_file)

    print(puzzle.available_fresh_ingredients_count())
    print(puzzle.all_fresh_ingredients_count())
