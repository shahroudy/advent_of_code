import re
from pathlib import Path

from myutils.io_handler import get_input_data


class SomeAssemblyRequired:
    def __init__(self, filename):
        self.commands = Path(filename).read_text().splitlines()
        self.wires = {}
        self.run_all_commands()

    def run_command(self, command):
        def my_eval(s):
            if s.isdigit():
                return int(s)
            return self.wires[s]

        left, right = re.split(r" -> ", command)
        if right in self.wires:
            return False
        parts = re.split(r" ", left.strip())
        try:
            if len(parts) == 1:
                self.wires[right] = my_eval(parts[0])
            elif len(parts) == 2:
                if parts[0] == "NOT":
                    self.wires[right] = (~my_eval(parts[1])) & 0xFFFF
                else:
                    raise ValueError("Unknown operator")
            elif len(parts) == 3:
                if parts[1] == "AND":
                    self.wires[right] = my_eval(parts[0]) & my_eval(parts[2])
                elif parts[1] == "OR":
                    self.wires[right] = my_eval(parts[0]) | my_eval(parts[2])
                elif parts[1] == "LSHIFT":
                    self.wires[right] = my_eval(parts[0]) << my_eval(parts[2])
                elif parts[1] == "RSHIFT":
                    self.wires[right] = my_eval(parts[0]) >> my_eval(parts[2])
        except KeyError:
            return False
        return True

    def run_all_commands(self):
        finished = False
        while not finished:
            finished = True
            for line in self.commands:
                if self.run_command(line):
                    finished = False

    def first_execution(self):
        return self.wires["a"]

    def second_execution(self):
        self.wires = {"b": self.wires["a"]}
        self.run_all_commands()
        return self.wires["a"]


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = SomeAssemblyRequired(filename)
    assert answer1 is None or test.first_execution() == answer1
    assert answer2 is None or test.second_execution() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 65079, None)

    print("Tests passed, starting with the puzzle")

    puzzle = SomeAssemblyRequired(data.input_file)

    print(puzzle.first_execution())
    print(puzzle.second_execution())
