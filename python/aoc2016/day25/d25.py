from itertools import count
from pathlib import Path

from myutils.io_handler import get_input_data


class ClockSignal:
    def __init__(self, filename):
        self.code = [line.split() for line in Path(filename).read_text().splitlines()]

    def does_generate_the_pattern(self, init_value):
        code = self.code
        regs = {"a": init_value, "b": 0, "c": 0, "d": 0}
        head = 0
        bit = 0
        bit_count = 100
        while head < len(code):
            cmd = code[head]
            head += 1
            if cmd[0] == "cpy":
                if cmd[2] in regs:
                    regs[cmd[2]] = regs[cmd[1]] if cmd[1] in regs else int(cmd[1])
            elif cmd[0] == "inc":
                if cmd[1] in regs:
                    regs[cmd[1]] += 1
            elif cmd[0] == "dec":
                if cmd[1] in regs:
                    regs[cmd[1]] -= 1
            elif cmd[0] == "jnz":
                if int(cmd[1]) if cmd[1].isnumeric() else regs[cmd[1]]:
                    head += (regs[cmd[2]] if cmd[2] in regs else int(cmd[2])) - 1
            elif cmd[0] == "out":
                if regs[cmd[1]] != bit:
                    return False
                else:
                    bit = 1 - bit
                    bit_count -= 1
                    if bit_count == 0:
                        return True

    def find_minimum_init_value(self):
        for i in count():
            if self.does_generate_the_pattern(i):
                return i


if __name__ == "__main__":
    data = get_input_data(__file__)

    puzzle = ClockSignal(data.input_file)

    print(puzzle.find_minimum_init_value())
