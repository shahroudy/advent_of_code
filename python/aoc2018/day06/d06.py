from collections import defaultdict
from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import process_int_list


class ChronalCoordinates:
    def __init__(self, filename):
        self.coordinates = process_int_list(Path(filename).read_text())
        self.xmin = min(p[0] for p in self.coordinates)
        self.ymin = min(p[1] for p in self.coordinates)
        self.xmax = max(p[0] for p in self.coordinates)
        self.ymax = max(p[1] for p in self.coordinates)

    def size_of_largest_area(self):
        areas = defaultdict(list)
        infinite_areas = set()
        for x, y in product(range(self.xmin, self.xmax + 1), range(self.ymin, self.ymax + 1)):
            min_dist = float("inf")
            closest_points = []
            for xc, yc in self.coordinates:
                dist = abs(x - xc) + abs(y - yc)
                if dist < min_dist:
                    min_dist = dist
                    closest_points = [(xc, yc)]
                elif dist == min_dist:
                    closest_points.append((xc, yc))
            if len(closest_points) == 1:
                p = closest_points[0]
                areas[p].append((x, y))
                if x in (self.xmin, self.xmax) or y in (self.ymin, self.ymax):
                    infinite_areas.add(p)
        return max((len(points) for area, points in areas.items() if area not in infinite_areas))

    def area_of_the_region(self, distance_limit=10000):
        area = 0
        for q in product(
            range(self.xmin, self.xmax + 1),
            range(self.ymin, self.ymax + 1),
        ):
            dist_sum = 0
            for p in self.coordinates:
                dist_sum += abs(p[0] - q[0]) + abs(p[1] - q[1])
                if dist_sum >= distance_limit:
                    break
            else:
                area += 1
        return area


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ChronalCoordinates("sample1.txt").size_of_largest_area() == 17
    assert ChronalCoordinates("sample1.txt").area_of_the_region(32) == 16

    print("Tests passed, starting with the puzzle")

    puzzle = ChronalCoordinates(data.input_file)

    print(puzzle.size_of_largest_area())
    print(puzzle.area_of_the_region())
