import os
from pathlib import Path

from aoc2019.day09.d09 import IntcodeComputer
from myutils.io_handler import get_input_data


class CategorySix:
    def __init__(self, filename):
        self.program = list(map(int, Path(filename).read_text().split(",")))

    def run_network(self, NAT_mode=False):
        computers = []
        nat_state = None
        nat_memory = set()
        for i in range(50):
            computer = IntcodeComputer(self.program)
            computer.input.extend([i, -1])
            computer.reset(computer.input)
            computers.append(computer)
        while True:
            input_available = True
            while input_available:
                input_available = False
                for i in range(50):
                    if computers[i].input:
                        input_available = True
                        output = computers[i].compute_while_input()
                        while output:
                            i, x, y = (output.popleft(), output.popleft(), output.popleft())
                            if i == 255:
                                if NAT_mode:
                                    nat_state = [x, y]
                                else:
                                    return y
                            else:
                                computers[i].input.extend([x, y])
            y = nat_state[1]
            if y in nat_memory:
                return y
            nat_memory.add(y)
            computers[0].input.extend(nat_state)


if __name__ == "__main__":
    data = get_input_data(__file__)
    puzzle = CategorySix(data.input_file)
    print(puzzle.run_network())
    print(puzzle.run_network(NAT_mode=True))
