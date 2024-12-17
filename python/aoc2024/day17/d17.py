import re
from pathlib import Path

from myutils.io_handler import get_input_data


class ChronospatialComputer:
    def __init__(self, filename):
        numbers = [int(n) for n in re.findall(r"[+-]?\d+", Path(filename).read_text())]
        self.initial_values, self.program = numbers[:3], numbers[3:]

    def reset_computer(self):
        self.A, self.B, self.C = self.initial_values
        self.head = 0
        self.outputs = []

    def run_current_command(self):
        opcode, operand = self.program[self.head : self.head + 2]
        combo_operand = {0: 0, 1: 1, 2: 2, 3: 3, 4: self.A, 5: self.B, 6: self.C}[operand]

        if opcode == 0:  # adv = div
            self.A = self.A // 2**combo_operand
        elif opcode == 1:  # bxl
            self.B = self.B ^ operand
        elif opcode == 2:  # bst
            self.B = combo_operand % 8
        elif opcode == 3:  # jnz
            if self.A != 0:
                self.head = operand - 2
        elif opcode == 4:  # bxc
            self.B = self.B ^ self.C
        elif opcode == 5:  # out
            self.outputs.append(combo_operand % 8)
        elif opcode == 6:  # bdv
            self.B = self.A // 2**combo_operand
        elif opcode == 7:  # cdv
            self.C = self.A // 2**combo_operand
        self.head += 2

    def run_the_program(self):
        self.reset_computer()
        while 0 <= self.head < len(self.program):
            self.run_current_command()
        return ",".join(map(str, self.outputs))

    def find_min_A_to_output_the_same_program(self):
        prog = self.program
        minimum_possible_a = 0
        b_value_history = [0] * len(prog)  # to keep track of the "b" values we have tried so far
        b_value_history[0] = 1  # the last b cannot be zero to avoid early termination
        index = 0
        while 0 <= index < len(prog):
            # for each index we need to try all the 8 possible values of "b" and check which can
            # generate the expected output value;
            # We will proceed with the minimum possible "b" value to minimize the final "a" value.
            # But if we fail to find a proper "b" value, we need to backtrack and try a different
            # "b" value in the previous step.
            b = b_value_history[index]
            while b <= 7:  # b values are 3-bit numbers, so possible values are between 0 and 7
                self.A = minimum_possible_a * 8 + b
                self.head = 0
                self.outputs = []
                while self.head < len(self.program) - 2:
                    self.run_current_command()
                if self.outputs.pop() == prog[-index - 1]:
                    minimum_possible_a = minimum_possible_a * 8 + b
                    b_value_history[index] = b + 1  # if we backtrack, we need to try the next value
                    index += 1
                    if index == len(prog):
                        return minimum_possible_a
                    else:
                        b_value_history[index] = 0  # for the next index, we need to start from 0
                    break
                b += 1
            else:
                # we cannot continue with the current values, we need to backtrack and try
                # a different "b" value in the latest possible step, to minimize the final "a" value
                minimum_possible_a = minimum_possible_a // 8
                index -= 1


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ChronospatialComputer("sample1.txt").run_the_program() == "4,6,3,5,6,3,5,2,1,0"

    print("Tests passed, starting with the puzzle")

    puzzle = ChronospatialComputer(data.input_file)

    print(puzzle.run_the_program())
    print(puzzle.find_min_A_to_output_the_same_program())
