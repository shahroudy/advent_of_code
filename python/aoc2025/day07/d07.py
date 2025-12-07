from collections import defaultdict
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data
from myutils.utils import read_map_dict_of_sets_of_points


class Laboratories:
    def __init__(self, filename):
        input_map, rows, _ = read_map_dict_of_sets_of_points(Path(filename).read_text())
        start = input_map["S"].pop()
        splitters = input_map["^"]
        beams = {start.x: 1}
        self.splits = 0
        for y in range(rows):
            new_row_beams = defaultdict(int)
            for x, n in beams.items():
                if Point(x, y) in splitters:
                    new_row_beams[x - 1] += n
                    new_row_beams[x + 1] += n
                    self.splits += 1
                else:
                    new_row_beams[x] += n
            beams = new_row_beams
        self.total_paths = sum(beams.values())


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Laboratories("sample1.txt").splits == 21
    assert Laboratories("sample1.txt").total_paths == 40

    print("Tests passed, starting with the puzzle")

    puzzle = Laboratories(data.input_file)

    print(puzzle.splits)
    print(puzzle.total_paths)
