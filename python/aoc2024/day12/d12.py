from pathlib import Path

from myutils.geometry import Point, find_connected_components, outer_border, region_perimeter
from myutils.io_handler import get_input_data


class GardenGroups:
    def __init__(self, filename):
        self.input_text = Path(filename).read_text()

        lines = self.input_text.splitlines()
        plot = dict()
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                plot[Point(col, row)] = ch

        self.regions, self.region_map = find_connected_components(plot, Point.neighbors_4)

    def total_price(self):
        return sum(len(r) * region_perimeter(r, Point.neighbors_4) for r in self.regions.values())

    def total_price_discounted(self):
        res = 0
        for region in self.regions.values():
            borders = outer_border(region, Point.neighbors_4)
            side_count = 0
            border_directions = set(direction for point, direction in borders)
            for border_direction in border_directions:
                points = {point for point, direction in borders if direction == border_direction}
                connected_borders, _ = find_connected_components(points, Point.neighbors_4)
                side_count += len(connected_borders)
            res += len(region) * side_count
        return res


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = GardenGroups(filename)
    assert answer1 is None or test.total_price() == answer1
    assert answer2 is None or test.total_price_discounted() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert GardenGroups("sample1.txt").total_price() == 140
    assert GardenGroups("sample2.txt").total_price() == 772
    assert GardenGroups("sample3.txt").total_price() == 1930

    assert GardenGroups("sample1.txt").total_price_discounted() == 80
    assert GardenGroups("sample2.txt").total_price_discounted() == 436
    assert GardenGroups("sample3.txt").total_price_discounted() == 1206
    assert GardenGroups("sample4.txt").total_price_discounted() == 368

    print("Tests passed, starting with the puzzle")

    puzzle = GardenGroups(data.input_file)

    print(puzzle.total_price())
    print(puzzle.total_price_discounted())

    assert puzzle.total_price() == 1421958
    assert puzzle.total_price_discounted() == 885394
