import re
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data


class RainRisk:
    def __init__(self, filename):
        self.inp = [
            (cmd, int(num)) for cmd, num in re.findall(r"(\w)(\d+)", Path(filename).read_text())
        ]

    def move_ship(self):
        ship = Point(0, 0)
        dir = Point(1, 0)
        for cmd, num in self.inp:
            if cmd == "N":
                ship += Point(0, -num)
            elif cmd == "S":
                ship += Point(0, num)
            elif cmd == "E":
                ship += Point(num, 0)
            elif cmd == "W":
                ship += Point(-num, 0)
            elif cmd == "L":
                dir.rotate(num)
            elif cmd == "R":
                dir.rotate(-num)
            elif cmd == "F":
                ship += dir * num
        return ship.manhattan_dist(Point(0, 0))

    def move_ship_with_waypoint(self):
        ship = Point(0, 0)
        waypoint = Point(10, -1)
        for cmd, num in self.inp:
            if cmd == "N":
                waypoint += Point(0, -num)
            elif cmd == "S":
                waypoint += Point(0, num)
            elif cmd == "E":
                waypoint += Point(num, 0)
            elif cmd == "W":
                waypoint += Point(-num, 0)
            elif cmd == "L":
                waypoint.rotate(num)
            elif cmd == "R":
                waypoint.rotate(-num)
            elif cmd == "F":
                ship += waypoint * num
        return ship.manhattan_dist(Point(0, 0))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert RainRisk("sample1.txt").move_ship() == 25
    assert RainRisk("sample1.txt").move_ship_with_waypoint() == 286

    print("Tests passed, starting with the puzzle")

    puzzle = RainRisk(data.input_file)

    print(puzzle.move_ship())
    print(puzzle.move_ship_with_waypoint())
