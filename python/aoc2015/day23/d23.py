from pathlib import Path

from myutils.io_handler import get_input_data


class OpeningTheTuringLock:
    def __init__(self, filename):
        self.code = [c.replace(",", "").split() for c in Path(filename).read_text().splitlines()]

    def run(self, a_value=0):
        self.a, self.b = a_value, 0
        head = 0
        while head < len(self.code):
            cmd, *args = self.code[head]
            if cmd == "hlf":
                setattr(self, args[0], getattr(self, args[0]) // 2)
            elif cmd == "tpl":
                setattr(self, args[0], getattr(self, args[0]) * 3)
            elif cmd == "inc":
                setattr(self, args[0], getattr(self, args[0]) + 1)
            elif cmd == "jmp":
                head += int(args[0])
                continue
            elif cmd == "jie":
                if getattr(self, args[0]) % 2 == 0:
                    head += int(args[1])
                    continue
            elif cmd == "jio":
                if getattr(self, args[0]) == 1:
                    head += int(args[1])
                    continue
            head += 1
        return self.b


if __name__ == "__main__":
    data = get_input_data(__file__)

    puzzle = OpeningTheTuringLock(data.input_file)

    print(puzzle.run(a_value=0))
    print(puzzle.run(a_value=1))
