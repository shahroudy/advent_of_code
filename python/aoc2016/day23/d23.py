from copy import deepcopy
from math import factorial
from pathlib import Path

from myutils.io_handler import get_input_data


class SafeCracking:
    def __init__(self, filename):
        self.assembunny = [line.split() for line in Path(filename).read_text().splitlines()]

    def run_assembunny_code(self, eggs_number=7):
        return factorial(eggs_number) + int(self.assembunny[19][1]) * int(self.assembunny[20][1])

    def run_assembunny_code_adhoc(self, eggs_number=7):
        code = deepcopy(self.assembunny)
        regs = {"a": eggs_number, "b": 0, "c": 0, "d": 0}
        head = 0
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
            elif cmd[0] == "tgl":
                offset = int(cmd[1]) if cmd[1].isnumeric() else regs[cmd[1]]
                pointer = head + offset - 1
                if 0 <= pointer < len(code):
                    ocmd = code[head + offset - 1]
                    if ocmd[0] == "inc":
                        ocmd[0] = "dec"
                    elif ocmd[0] == "dec" or ocmd[0] == "tgl":
                        ocmd[0] = "inc"
                    elif ocmd[0] == "jnz":
                        ocmd[0] = "cpy"
                    elif ocmd[0] == "cpy":
                        ocmd[0] = "jnz"
        return regs["a"]


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert SafeCracking("sample1.txt").run_assembunny_code_adhoc(eggs_number=7) == 3

    print("Tests passed, starting with the puzzle")

    puzzle = SafeCracking(data.input_file)

    print(puzzle.run_assembunny_code(eggs_number=7))

    print(puzzle.run_assembunny_code(eggs_number=12))
