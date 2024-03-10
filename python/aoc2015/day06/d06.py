import re
from pathlib import Path

import numpy as np
from myutils.io_handler import get_input_data


class ProbablyAFireHazard:
    def __init__(self, filename):
        self.lights = np.zeros((1000, 1000), dtype=int)
        self.brightness = np.zeros((1000, 1000), dtype=int)
        line_re = re.compile(r"(.+) (\d+),(\d+) through (\d+),(\d+)")
        for line in Path(filename).read_text().splitlines():
            groups = line_re.match(line).groups()
            cmd = groups[0]
            x1, y1, x2, y2 = map(int, groups[1:])
            if cmd == "turn on":
                self.lights[x1 : x2 + 1, y1 : y2 + 1] = 1
                self.brightness[x1 : x2 + 1, y1 : y2 + 1] += 1
            elif cmd == "turn off":
                self.lights[x1 : x2 + 1, y1 : y2 + 1] = 0
                self.brightness[x1 : x2 + 1, y1 : y2 + 1] -= 1
                self.brightness[self.brightness < 0] = 0
            else:
                self.lights[x1 : x2 + 1, y1 : y2 + 1] = 1 - self.lights[x1 : x2 + 1, y1 : y2 + 1]
                self.brightness[x1 : x2 + 1, y1 : y2 + 1] += 2

    def lit_lights(self):
        return self.lights.sum()

    def brightness_sum(self):
        return self.brightness.sum()


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = ProbablyAFireHazard(filename)
    assert answer1 is None or test.lit_lights() == answer1
    assert answer2 is None or test.brightness_sum() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 1000000, None)
    test_samples("sample2.txt", 1000, None)
    test_samples("sample3.txt", 0, None)
    test_samples("sample4.txt", None, 1)
    test_samples("sample5.txt", None, 2000000)

    print("Tests passed, starting with the puzzle")

    puzzle = ProbablyAFireHazard(data.input_file)

    print(puzzle.lit_lights())
    print(puzzle.brightness_sum())
