import os
import re
from pathlib import Path
import numpy


class TheStarsAlign:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")

    def fast_forward(self):
        line_re = re.compile(r"position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>.*")
        values = [list(map(int, line_re.match(line).groups())) for line in self.lines]
        nums = numpy.array(values)
        t = 0
        while True:
            t += 1
            nums[:, :2] += nums[:, 2:]
            mins = numpy.min(nums, 0)
            maxs = numpy.max(nums, 0)
            if maxs[1] - mins[1] <= 10:
                stars = {(n[0], n[1]) for n in nums}
                for yc in range(mins[1], maxs[1] + 1):
                    for xc in range(mins[0], maxs[0] + 1):
                        print("#" if (xc, yc) in stars else ".", end="")
                    print()
                print(f"Time: {t}")
                return


if __name__ == "__main__":
    input_file = f'{os.environ.get("aoc_inputs")}/aoc2018_day10.txt'
    TheStarsAlign(input_file).fast_forward()
