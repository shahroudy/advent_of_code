import os
from collections import defaultdict, deque
from myutils.file_reader import read_int_list
from aoc2019.day09.d09 import IntcodeComputer
from myutils.io_handler import get_input_data


class SetAndForget:

    def __init__(self, filename):
        self.program = read_int_list(filename)

    def reset(self):
        self.computer = IntcodeComputer(self.program.copy())

    def analyze_output(self, input, just_final_output=False):
        output = self.computer.compute(input)
        if just_final_output:
            return output.pop()
        output = "".join(map(chr, output))
        self.map = defaultdict(int)  # 0: ., 1: #
        row, col = 0, 0
        self.cols = 0
        for cell in output:
            if cell == "\n":
                if self.cols == 0:
                    self.cols = col
                col = 0
                row += 1
                continue
            if cell in "v^><":
                self.y, self.x = row, col
                if cell == "^":
                    self.dy, self.dx = -1, 0
                elif cell == "v":
                    self.dy, self.dx = 1, 0
                elif cell == "<":
                    self.dy, self.dx = 0, -1
                elif cell == ">":
                    self.dy, self.dx = 0, 1
            elif cell == "#":
                self.map[(row, col)] = 1
            elif cell == ".":
                self.map[(row, col)] = 0
            else:
                break
            col += 1
        self.rows = row
        print(output)

    def alignment(self):
        self.reset()
        self.analyze_output([])
        mask = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
        total = 0
        for cell in list(self.map.keys()):
            y, x = cell
            for mask_cell in mask:
                dy, dx = mask_cell
                if not self.map[(y + dy, x + dx)]:
                    break
            else:
                total += x * y
                self.map[(y, x)] = 2
        return total

    def calculate_plain_program(self):
        input = []
        map = self.map.copy()
        y, x = self.y, self.x
        dy, dx = self.dy, self.dx
        fc = 0
        while True:
            rcount = 0
            while map[(y + dy, x + dx)] == 0 and rcount < 4:
                dy, dx = -dx, dy
                rcount += 1
            if rcount == 0:
                fc += 1
                y += dy
                x += dx
                map[(y, x)] -= 1
            else:
                if fc:
                    input.append(str(fc))
                    fc = 0
                if rcount == 1:
                    input.append("L")
                elif rcount == 3:
                    input.append("R")
                elif rcount == 4:
                    break
                else:
                    raise Exception("Rotated Back!")
        return input

    def cleaning(self):
        self.program[0] = 2
        self.reset()
        input = self.calculate_plain_program()
        print(",".join(input))

        # Manually analyzed!
        input = (
            "A,A,C,B,C,B,C,B,B,A\n" "L,10,R,8,R,8\n" "R,10,L,12,R,10\n" "L,10,L,12,R,8,R,10\n" "n\n"
        )
        input = deque(map(ord, input))
        collected = self.analyze_output(input, just_final_output=True)
        print(f"Collected Dust: {collected}")


if __name__ == "__main__":
    data = get_input_data(__file__)
    sg = SetAndForget(data.input_file)
    sg.alignment()
    sg.cleaning()
