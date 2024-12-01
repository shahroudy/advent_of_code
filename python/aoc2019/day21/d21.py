import os
from collections import deque
from pathlib import Path

from aoc2019.day09.d09 import IntcodeComputer
from myutils.io_handler import get_input_data


class SpringdroidAdventure:
    def __init__(self, filename):
        self.program = list(map(int, Path(filename).read_text().split(",")))

    def run_springscript(self, inputs, debug=False):
        computer = IntcodeComputer(self.program)
        outputs = computer.compute(deque(map(ord, "\n".join(inputs) + "\n")))
        for i in outputs:
            if i > 255:
                return i
            elif debug:
                print(chr(i), end="")

    def hull_damage(self, extended_sensor_mode=False):
        inputs = (
            [  # (not A) or (D and not B) or (D and not C)
                "NOT A J",
                "OR D T",
                "AND B T",
                "AND C T",
                "NOT T T",
                "AND D T",
                "OR T J",
                "WALK",
            ]
            if not extended_sensor_mode
            else [  # (not A) or (D and not B and (E or H)) or (D and not C and (E or H))
                "OR A T",
                "AND B T",
                "AND C T",
                "NOT T T",
                "AND D T",
                "OR E J",
                "AND T J",
                "OR H J",
                "AND T J",
                "NOT A T",
                "OR T J",
                "RUN",
            ]
        )
        return self.run_springscript(inputs, False)


if __name__ == "__main__":
    data = get_input_data(__file__)
    puzzle = SpringdroidAdventure(data.input_file)
    print(puzzle.hull_damage())
    print(puzzle.hull_damage(extended_sensor_mode=True))
