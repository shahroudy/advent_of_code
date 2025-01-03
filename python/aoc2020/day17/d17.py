from functools import reduce
from pathlib import Path

from myutils.geometry import Point, Point3D, Point4D
from myutils.io_handler import get_input_data


class ConwayCubes:
    def __init__(self, filename):
        self.active_2D = set()
        for row, line in enumerate(Path(filename).read_text().splitlines()):
            for col, ch in enumerate(line):
                if ch == "#":
                    self.active_2D.add(Point(col, row))

    def calculate_active_cubes_in_3D(self):
        active = {Point3D(p.x, p.y, 0) for p in self.active_2D}
        for _ in range(6):
            new_active = set()
            for p in reduce(set.union, (p.n27() for p in active), set()):
                active_neighbors = sum(n in active for n in p.n26())
                if active_neighbors == 3 or (p in active and active_neighbors == 2):
                    new_active.add(p)
            active = new_active
        return len(active)

    def calculate_active_cubes_in_4D(self):
        active = {Point4D(p.x, p.y, 0, 0) for p in self.active_2D}
        for _ in range(6):
            new_active = set()
            for p in reduce(set.union, (p.n81() for p in active), set()):
                active_neighbors = sum(n in active for n in p.n80())
                if active_neighbors == 3 or (p in active and active_neighbors == 2):
                    new_active.add(p)
            active = new_active
        return len(active)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ConwayCubes("sample1.txt").calculate_active_cubes_in_3D() == 112
    assert ConwayCubes("sample1.txt").calculate_active_cubes_in_4D() == 848

    print("Tests passed, starting with the puzzle")

    puzzle = ConwayCubes(data.input_file)

    print(puzzle.calculate_active_cubes_in_3D())
    print(puzzle.calculate_active_cubes_in_4D())
