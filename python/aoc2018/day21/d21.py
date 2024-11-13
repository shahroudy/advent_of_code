from pathlib import Path

from myutils.io_handler import get_input_data


class ChronalConversion:
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
        self.counter += 1

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
            if b == 0:
                return registers[a]
            elif a == 0:
                return registers[b]
        return 0

    def register_0_value_for_fewest_instructions_executed_before_halt(self):
        registers = [0] * 6
        self.counter = 0
        while True:
            if result := self.run_op(self.program[registers[self.ip_reg]], registers):
                return result
            registers[self.ip_reg] += 1

    def register_0_value_for_maximum_instructions_executed_before_repeating(self):
        registers = [0] * 6
        self.counter = 0
        ex = set()
        last = 0
        while True:
            if result := self.run_op(self.program[registers[self.ip_reg]], registers):
                if result in ex:
                    return last
                last = result
                ex.add(result)
            registers[self.ip_reg] += 1


if __name__ == "__main__":
    data = get_input_data(__file__)

    puzzle = ChronalConversion(data.input_file)
    print(puzzle.register_0_value_for_fewest_instructions_executed_before_halt())
    print(puzzle.register_0_value_for_maximum_instructions_executed_before_repeating())
