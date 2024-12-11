import re
from pathlib import Path

from myutils.io_handler import get_input_data


class HandheldHalting:
    def __init__(self, filename):
        line_re = re.compile(r"(\w+) ([+-]\d+)")
        self.program = [(cmd, int(arg)) for cmd, arg in line_re.findall(Path(filename).read_text())]

    def run(self, program):
        acc = 0
        history = set()
        head = 0
        while True:
            history.add(head)
            cmd, arg = program[head]
            if cmd == "acc":
                acc, head = acc + arg, head + 1
            elif cmd == "jmp":
                head += arg
            else:
                head += 1
            if head in history:
                return acc, True
            if head >= len(program):
                return acc, False

    def acc_value_before_looping(self):
        acc, _ = self.run(self.program)
        return acc

    def acc_value_after_proper_termination(self):
        for change_line in [n for n, (cmd, _) in enumerate(self.program) if cmd in ("jmp", "nop")]:
            program = self.program.copy()
            cmd, arg = program[change_line]
            program[change_line] = ("nop" if cmd == "jmp" else "jmp", arg)
            acc, infinite_loop = self.run(program)
            if not infinite_loop:
                return acc


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert HandheldHalting("sample1.txt").acc_value_before_looping() == 5
    assert HandheldHalting("sample1.txt").acc_value_after_proper_termination() == 8

    print("Tests passed, starting with the puzzle")

    puzzle = HandheldHalting(data.input_file)

    print(puzzle.acc_value_before_looping())
    print(puzzle.acc_value_after_proper_termination())
