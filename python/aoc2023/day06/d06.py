import os
import re
from pathlib import Path


class WaitForIt:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.times, self.distances = [list(map(int, re.findall(r"\d+", line))) for line in lines]

    def ways_to_win(self, time, distance):
        return sum([(time - t) * t > distance for t in range(time)])

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
    test_samples("sample1.txt", 288, 71503)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day06.txt'
    puzzle = WaitForIt(input_file)
    print(puzzle.ways_to_beat_records())
    print(puzzle.ways_to_beat_the_combined_record())
