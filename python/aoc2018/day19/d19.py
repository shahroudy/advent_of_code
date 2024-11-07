from pathlib import Path

from myutils.io_handler import get_input_data


class GoWithTheFlow:
    def __init__(self, filename):
        self.program = []
        for line in Path(filename).read_text().strip().split("\n"):
            parts = line.split()
            if len(parts) == 2:
                self.ip_reg = int(parts[1])
            else:
                self.program.append([parts[0], *map(int, parts[1:])])

    def run_op(self, command, registers):
        opcode, a, b, c = command
        if opcode == "addr":
            registers[c] = registers[a] + registers[b]
        elif opcode == "addi":
            registers[c] = registers[a] + b
        elif opcode == "mulr":
            registers[c] = registers[a] * registers[b]
        elif opcode == "muli":
            registers[c] = registers[a] * b
        elif opcode == "banr":
            registers[c] = registers[a] & registers[b]
        elif opcode == "bani":
            registers[c] = registers[a] & b
        elif opcode == "borr":
            registers[c] = registers[a] | registers[b]
        elif opcode == "bori":
            registers[c] = registers[a] | b
        elif opcode == "setr":
            registers[c] = registers[a]
        elif opcode == "seti":
            registers[c] = a
        elif opcode == "gtir":
            registers[c] = 1 if a > registers[b] else 0
        elif opcode == "gtri":
            registers[c] = 1 if registers[a] > b else 0
        elif opcode == "gtrr":
            registers[c] = 1 if registers[a] > registers[b] else 0
        elif opcode == "eqir":
            registers[c] = 1 if a == registers[b] else 0
        elif opcode == "eqri":
            registers[c] = 1 if registers[a] == b else 0
        elif opcode == "eqrr":
            registers[c] = 1 if registers[a] == registers[b] else 0

    def run_background_process(self):
        registers = [0] * 6
        while True:
            self.run_op(self.program[registers[self.ip_reg]], registers)
            if not (0 <= registers[self.ip_reg] < len(self.program) - 1):
                return registers[0]
            registers[self.ip_reg] += 1

    def set_reg_0_and_run_background_process(self):
        registers = [0] * 6
        registers[0] = 1
        while registers[self.ip_reg] != 1:
            self.run_op(self.program[registers[self.ip_reg]], registers)
            if not (0 <= registers[self.ip_reg] < len(self.program) - 1):
                return registers[0]
            registers[self.ip_reg] += 1
        r5 = registers[5]
        return sum([i for i in range(1, r5 + 1) if r5 % i == 0])


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert GoWithTheFlow("sample1.txt").run_background_process() == 6

    print("Tests passed, starting with the puzzle")

    puzzle = GoWithTheFlow(data.input_file)
    print(puzzle.run_background_process())
    print(puzzle.set_reg_0_and_run_background_process())
