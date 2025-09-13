from pathlib import Path

from myutils.geometry import Point, Point3D
from myutils.io_handler import get_input_data


class Dive:
    def __init__(self, filename):
        text = Path(filename).read_text().splitlines()
        self.inp = [(cmd, int(val)) for cmd, val in (line.split() for line in text)]

    def final_depth(self):
        """Represent the current position in 2D space (x:horizontal, y:depth)"""
        moves = {"up": Point(0, -1), "down": Point(0, 1), "forward": Point(1, 0)}
        current = Point(0, 0)
        for cmd, val in self.inp:
            current += moves[cmd] * val
        return abs(current.x) * abs(current.y)

    def final_depth_with_aim(self):
        """Represent the current position in 3D space (x:horizontal, y:depth, z:aim)"""
        moves = {"up": Point3D(0, 0, -1), "down": Point3D(0, 0, 1), "forward": Point3D(1, 0, 0)}
        current = Point3D(0, 0, 0)
        for cmd, val in self.inp:
            current += moves[cmd] * val
            if cmd == "forward":
                current.y += val * current.z
        return abs(current.x) * abs(current.y)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Dive("sample1.txt").final_depth() == 150
    assert Dive("sample1.txt").final_depth_with_aim() == 900

    print("Tests passed, starting with the puzzle")

    puzzle = Dive(data.input_file)

    print(puzzle.final_depth())
    print(puzzle.final_depth_with_aim())
