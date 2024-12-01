import math
import os
import re
from pathlib import Path
from myutils.io_handler import get_input_data


class WaitForIt:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.times, self.distances = [list(map(int, re.findall(r"\d+", line))) for line in lines]

    def ways_to_win_loop(self, time, distance):
        return sum([(time - t) * t > distance for t in range(time)])

    def ways_to_win(self, time, distance):
        # we want to solve the equation: time*t - t^2 - distance > 0
        # the solutions to the quadratic equation: a * x^2 + b * x + c = 0 are:
        a, b, c = -1, time, -distance
        d = b**2 - 4 * a * c
        sol1 = (-b - math.sqrt(d)) / (2 * a)
        sol2 = (-b + math.sqrt(d)) / (2 * a)
        min_sol, max_sol = min(sol1, sol2), max(sol1, sol2)
        # we are not interested in the integer solutions because they don't beat the record
        min_sol = min_sol + 1 if min_sol.is_integer() else math.ceil(min_sol)
        max_sol = max_sol - 1 if max_sol.is_integer() else math.floor(max_sol)
        return max_sol - min_sol + 1

    def ways_to_beat_records(self):
        ways = 1
        for time, distance in zip(self.times, self.distances):
            ways *= self.ways_to_win(time, distance)
        return ways

    def ways_to_beat_the_combined_record(self):
        time = int("".join(map(str, self.times)))
        distance = int("".join(map(str, self.distances)))
        return self.ways_to_win(time, distance)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = WaitForIt(filename)
    assert answer1 is None or test.ways_to_beat_records() == answer1
    assert answer2 is None or test.ways_to_beat_the_combined_record() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 288, 71503)

    print("Tests passed, starting with the puzzle")

    puzzle = WaitForIt(data.input_file)
    print(puzzle.ways_to_beat_records())
    print(puzzle.ways_to_beat_the_combined_record())
