import os
from pathlib import Path
from collections import deque


class CathodeRayTube:
    def __init__(self, filename):
        self.program = []
        for line in Path(filename).read_text().strip().split("\n"):
            parts = line.split()
            if len(parts) == 1:
                self.program.append(None)
            else:
                self.program.append(int(parts[1]))

    def sum_signal_strengths(self, printer=False):
        program = deque(self.program)
        x_reg = 1
        sum_ss = 0
        cpu_busy = False
        for cycle in range(1, 241):
            if cycle % 40 == 20:
                sum_ss += cycle * x_reg
            if printer:
                print("#" if abs((cycle - 1) % 40 - x_reg) < 2 else ".", end="")
                if cycle % 40 == 0:
                    print()
            if not cpu_busy:
                op = program.popleft()
                if op is not None:
                    cpu_busy = True
            else:
                cpu_busy = False
                x_reg += op

        return sum_ss


def test_samples(filename, answer):
    test = CathodeRayTube(filename)
    assert test.sum_signal_strengths(printer=False) == answer


if __name__ == "__main__":

    test_samples("sample1.txt", 13140)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day10.txt'
    cathode_ray_tube = CathodeRayTube(input_file)
    print(cathode_ray_tube.sum_signal_strengths(printer=True))
