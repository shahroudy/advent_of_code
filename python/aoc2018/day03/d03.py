from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import process_int_list


class NoMatterHowYouSliceIt:
    def __init__(self, filename):
        self.claims = process_int_list(text=Path(filename).read_text())
        self.calculate_overlapping_tiles()

    def calculate_overlapping_tiles(self):
        seen_tiles = set()
        self.overlapping_tiles = set()
        for _, x, y, w, h in self.claims:
            for tile in product(range(x, x + w), range(y, y + h)):
                if tile in seen_tiles:
                    self.overlapping_tiles.add(tile)
                seen_tiles.add(tile)

    def overlapping_area(self):
        return len(self.overlapping_tiles)

    def non_overlapping_claim_id(self):
        for id, x, y, w, h in self.claims:
            for tile in product(range(x, x + w), range(y, y + h)):
                if tile in self.overlapping_tiles:
                    break
            else:
                return id


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = NoMatterHowYouSliceIt("sample1.txt")
    assert test.overlapping_area() == 4
    assert test.non_overlapping_claim_id() == 3

    print("Tests passed, starting with the puzzle")

    puzzle = NoMatterHowYouSliceIt(data.input_file)

    print(puzzle.overlapping_area())
    print(puzzle.non_overlapping_claim_id())
