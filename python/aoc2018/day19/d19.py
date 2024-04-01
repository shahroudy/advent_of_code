import cProfile
import os
import re
from collections import *
from copy import deepcopy
from functools import cache, cmp_to_key, reduce
from itertools import *
from pathlib import Path

from myutils.file_reader import *
from myutils.io_handler import get_input_data, submit_answer
from sympy import Symbol
from sympy.solvers import solve


class Puzzle:
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

    def calc1(self, r0_init=0):
        registers = [0] * 6
        registers[0] = r0_init
        while True:
            self.run_op(self.program[registers[self.ip_reg]], registers)
            if registers[self.ip_reg] >= len(self.program) - 1:
                return registers[0]
            registers[self.ip_reg] += 1

    def calc2(self):
        return self.calc1(1)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = Puzzle(filename)
    assert answer1 is None or test.calc1() == answer1
    assert answer2 is None or test.calc2() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    # assert Puzzle("sample1.txt").calc1() == 6

    print("Tests passed, starting with the puzzle")

    submit_answers = False
    puzzle = Puzzle(data.input_file)
    # cProfile.run("print(answer1 := puzzle.calc1())")
    # print(answer1 := puzzle.calc1())
    # if submit_answers and answer1 is not None:
    #     submit_answer(answer1, "a", data)
    # cProfile.run("print(answer2 := puzzle.calc2())")
    print(answer2 := puzzle.calc2())
    if submit_answers and answer2 is not None:
        submit_answer(answer2, "b", data)
