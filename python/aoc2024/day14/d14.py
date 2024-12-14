import re
from itertools import count
from pathlib import Path

from myutils.geometry import Point, connected_region
from myutils.io_handler import get_input_data


class RestroomRedoubt:
    def __init__(self, filename, **kwargs):
        lines = Path(filename).read_text().splitlines()
        numbers = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]
        self.init_robot_positions = [Point(x, y) for x, y, _, _ in numbers]
        self.velocities = [Point(dx, dy) for _, _, dx, dy in numbers]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def move_robots(self, robots):
        for i in range(len(robots)):
            robots[i] += self.velocities[i]
            robots[i].wrap_around(self)

    def safety_factor(self):
        robots = self.init_robot_positions.copy()
        for _ in range(100):
            self.move_robots(robots)
        q0 = q1 = q2 = q3 = 0
        for i in range(len(robots)):
            x, y = robots[i].tuple
            if x < self.cols // 2:
                if y < self.rows // 2:
                    q0 += 1
                if y > self.rows // 2:
                    q2 += 1
            if x > self.cols // 2:
                if y < self.rows // 2:
                    q1 += 1
                if y > self.rows // 2:
                    q3 += 1
        return q0 * q1 * q2 * q3

    def time_to_display_easter_egg(self, display=False):
        robots = self.init_robot_positions.copy()
        center_point = Point(self.cols // 2, self.rows // 2)
        for time in count(1):
            self.move_robots(robots)
            region = connected_region(robots, Point.n8, center_point)
            if len(region) > 50:
                if display:
                    for y in range(self.rows):
                        for x in range(self.cols):
                            print("#" if Point(x, y) in robots else ".", end="")
                        print()
                return time


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert RestroomRedoubt("sample1.txt", cols=11, rows=7).safety_factor() == 12

    print("Tests passed, starting with the puzzle")

    puzzle = RestroomRedoubt(data.input_file, cols=101, rows=103)

    print(puzzle.safety_factor())
    print(puzzle.time_to_display_easter_egg(True))
