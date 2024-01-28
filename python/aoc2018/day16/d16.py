import os
import re
from collections import defaultdict
from pathlib import Path

from myutils.matching import find_a_mapping_dic


class ChronalClassification:
    def __init__(self, filename):
        tests, program = Path(filename).read_text().split("\n\n\n\n")
        nums_re = re.compile(r"\d+")
        self.tests = [list(map(int, re.findall(nums_re, test))) for test in tests.split("\n\n")]
        self.program = [list(map(int, re.findall(nums_re, line))) for line in program.splitlines()]
        self.matches = defaultdict(set)

    def run_op(self, command, registers):
        opcode, a, b, c = command
        if opcode == 0:
            registers[c] = registers[a] + registers[b]
        elif opcode == 1:
            registers[c] = registers[a] + b
        elif opcode == 2:
            registers[c] = registers[a] * registers[b]
        elif opcode == 3:
            registers[c] = registers[a] * b
        elif opcode == 4:
            registers[c] = registers[a] & registers[b]
        elif opcode == 5:
            registers[c] = registers[a] & b
        elif opcode == 6:
            registers[c] = registers[a] | registers[b]
        elif opcode == 7:
            registers[c] = registers[a] | b
        elif opcode == 8:
            registers[c] = registers[a]
        elif opcode == 9:
            registers[c] = a
        elif opcode == 10:
            registers[c] = 1 if a > registers[b] else 0
        elif opcode == 11:
            registers[c] = 1 if registers[a] > b else 0
        elif opcode == 12:
            registers[c] = 1 if registers[a] > registers[b] else 0
        elif opcode == 13:
            registers[c] = 1 if a == registers[b] else 0
        elif opcode == 14:
            registers[c] = 1 if registers[a] == b else 0
        elif opcode == 15:
            registers[c] = 1 if registers[a] == registers[b] else 0

    def find_matches(self):
        result = 0
        for test in self.tests:
            before, op, after = test[:4], test[4:8], test[8:]
            match_count = 0
            for i in range(16):
                registers = before.copy()
                self.run_op([i] + op[1:], registers)
                if registers == after:
                    self.matches[op[0]].add(i)
                    match_count += 1
            if match_count >= 3:
                result += 1
        return result

    def run_opcode_program(self):
        if len(self.matches) == 0:
            self.find_matches()
        opcode_matching = find_a_mapping_dic(self.matches)
        registers = [0] * 4
        for command in self.program:
            command[0] = opcode_matching[command[0]]
            self.run_op(command, registers)
        return registers[0]


if __name__ == "__main__":
    input_file = f'{os.environ.get("aoc_inputs")}/aoc2018_day16.txt'
    puzzle = ChronalClassification(input_file)
    print(puzzle.find_matches())
    print(puzzle.run_opcode_program())
