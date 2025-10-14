from pathlib import Path

from myutils.geometry import Point, connected_region
from myutils.io_handler import get_input_data
from myutils.utils import process_map_digits


class SmokeBasin:
    def __init__(self, filename):
        self.height_map, _, _ = process_map_digits(Path(filename).read_text())

    def sum_of_low_point_risk_levels(self):
        self.low_points = {
            point
            for point, height in self.height_map.items()
            if all(self.height_map.get(n, 10) > height for n in point.n4())
        }
        return sum(self.height_map[p] + 1 for p in self.low_points)

    def find_basin(self, low_point):
        return connected_region(
            self.height_map, Point.n4, lambda _, n: self.height_map.get(n, 9) != 9, start=low_point
        )

    def three_largest_basins(self):
        basins = [self.find_basin(lp) for lp in self.low_points]
        basins.sort(key=len, reverse=True)
        return len(basins[0]) * len(basins[1]) * len(basins[2])


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = SmokeBasin("sample1.txt")
    assert test1.sum_of_low_point_risk_levels() == 15
    assert test1.three_largest_basins() == 1134

    print("Tests passed, starting with the puzzle")

    puzzle = SmokeBasin(data.input_file)

    print(puzzle.sum_of_low_point_risk_levels())
    print(puzzle.three_largest_basins())
