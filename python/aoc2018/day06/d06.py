import os
from itertools import product
from pathlib import Path
from myutils.io_handler import get_input_data


class ChronalCoordinates:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.mask4 = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.process_lines()

    def process_lines(self):
        xs, ys = list(), list()
        for line in self.lines:
            x, y = map(int, line.split(", "))
            xs.append(x)
            ys.append(y)

        self.map = {(xs[i], ys[i]): i + 1 for i in range(len(xs))}
        self.minx, self.maxx = min(xs), max(xs)
        self.miny, self.maxy = min(ys), max(ys)

    def largest_finite_area(self):
        current_map = self.map.copy()
        points_queue = current_map.copy()
        areas = {n: 1 for n in self.map.values()}

        expanded = True
        while expanded:
            expanded = False
            iteration_points = dict()
            for point, label in points_queue.items():
                for direction in self.mask4:
                    neighbour = (point[0] + direction[0], point[1] + direction[1])
                    if neighbour not in current_map:
                        if neighbour not in iteration_points:
                            iteration_points[neighbour] = label
                        elif iteration_points[neighbour] != label:  # equal distance to two points
                            iteration_points[neighbour] = 0
            if not iteration_points:
                break
            points_queue = dict()
            for point, label in iteration_points.items():
                current_map[point] = label
                points_queue[point] = label
                if (
                    label > 0
                    and self.minx <= point[0] <= self.maxx
                    and self.miny <= point[1] <= self.maxy
                ):
                    if areas[label] > 0:
                        areas[label] += 1
                        expanded = True
                else:
                    areas[label] = -1

        return max(areas.values())

    def area_of_the_region(self, distance_limit=32):
        point_count = 0
        for i, j in product(range(self.minx, self.maxx), range(self.miny, self.maxy)):
            sum_distance = 0
            for point in self.map:
                sum_distance += abs(i - point[0]) + abs(j - point[1])
                if sum_distance >= distance_limit:
                    break
            if sum_distance < distance_limit:
                point_count += 1
        return point_count


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = ChronalCoordinates("test1.txt")
    assert test1.largest_finite_area() == 17
    assert test1.area_of_the_region() == 16

    chronal_coordinates = ChronalCoordinates(data.input_file)
    print(chronal_coordinates.largest_finite_area())
    print(chronal_coordinates.area_of_the_region(10000))
