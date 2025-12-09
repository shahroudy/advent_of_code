from itertools import combinations
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data
from myutils.utils import read_points_per_line


class MovieTheater:
    def __init__(self, filename):
        self.points = read_points_per_line(Path(filename).read_text())

    def largest_rectangle(self):
        return max(p.area(q, inclusive=True) for p, q in combinations(self.points, 2))

    def is_rectangle_inside(self, p, q, outer_points):
        for x in range(min(p.x, q.x), max(p.x, q.x) + 1):
            for y in range(min(p.y, q.y), max(p.y, q.y) + 1):
                if Point(x, y) in outer_points:
                    return False
        return True

    def largest_rectangle_within_contour(self):
        xs = sorted({p.x for p in self.points})
        ys = sorted({p.y for p in self.points})

        mini_index = {}
        for p in self.points:
            mini_index[p] = Point(xs.index(p.x), ys.index(p.y))
        mini_points = [mini_index[p] for p in self.points]

        borders = set()
        for p, q in zip(mini_points, mini_points[1:] + [mini_points[0]]):
            if p.x == q.x:
                for y in range(p.y, q.y, 1 if q.y >= p.y else -1):
                    borders.add(Point(p.x, y))
            else:
                for x in range(p.x, q.x, 1 if q.x >= p.x else -1):
                    borders.add(Point(x, p.y))

        # Flood fill from outside to find outer area
        x_range = range(-1, len(xs) + 1)
        y_range = range(-1, len(ys) + 1)
        outer = set([Point(-1, -1)])
        q = [Point(-1, -1)]
        while q:
            p = q.pop()
            for n in p.n4():
                if n.x not in x_range or n.y not in y_range:
                    continue
                if n in borders:
                    continue
                if n in outer:
                    continue
                outer.add(n)
                q.append(n)

        max_area = 0
        for p, q in combinations(self.points, 2):
            pi, qi = mini_index[p], mini_index[q]
            d = p.area(q, inclusive=True)
            if d > max_area and self.is_rectangle_inside(pi, qi, outer_points=outer):
                max_area = d

        return max_area


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert MovieTheater("sample1.txt").largest_rectangle() == 50
    assert MovieTheater("sample1.txt").largest_rectangle_within_contour() == 24

    print("Tests passed, starting with the puzzle")

    puzzle = MovieTheater(data.input_file)

    print(puzzle.largest_rectangle())
    print(puzzle.largest_rectangle_within_contour())
