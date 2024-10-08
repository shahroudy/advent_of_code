from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class LeonardosMonorail:
    def __init__(self, filename):
        self.assembunny = [line.split() for line in Path(filename).read_text().splitlines()]

    def run_assembunny_code(self, ignition=False):
        regs = defaultdict(int)
        regs["c"] = 1 if ignition else 0
        head = 0
        while head < len(self.assembunny):
            cmd = self.assembunny[head]
            head += 1
            if cmd[0] == "cpy":
                regs[cmd[2]] = int(cmd[1]) if cmd[1].isnumeric() else regs[cmd[1]]
            elif cmd[0] == "inc":
                regs[cmd[1]] += 1
            elif cmd[0] == "dec":
                regs[cmd[1]] -= 1
            elif cmd[0] == "jnz":
                if int(cmd[1]) if cmd[1].isnumeric() else regs[cmd[1]]:
                    head += int(cmd[2]) - 1
        return regs["a"]


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert LeonardosMonorail("sample1.txt").run_assembunny_code() == 42

    print("Tests passed, starting with the puzzle")

    puzzle = LeonardosMonorail(data.input_file)

    print(puzzle.run_assembunny_code())
    print(puzzle.run_assembunny_code(ignition=1))
