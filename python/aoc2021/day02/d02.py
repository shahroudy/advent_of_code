import os
from myutils.file_reader import read_lines
from myutils.io_handler import get_input_data


class Dive:
    def __init__(self, filename):
        self.lines = read_lines(filename)

    def position(self):
        depth, horizontal = 0, 0
        for line in self.lines:
            terms = line.split()
            command = terms[0]
            value = int(terms[1])
            if command == "forward":
                horizontal += value
            elif command == "up":
                depth -= value
            elif command == "down":
                depth += value
        return depth * horizontal

    def position_with_aim(self):
        depth, horizontal, aim = 0, 0, 0
        for line in self.lines:
            terms = line.split()
            command = terms[0]
            value = int(terms[1])
            if command == "forward":
                horizontal += value
                depth += aim * value
            elif command == "up":
                aim -= value
            elif command == "down":
                aim += value
        return depth * horizontal


if __name__ == "__main__":
    data = get_input_data(__file__)
    test1 = Dive("test1.txt")
    assert test1.position() == 150
    assert test1.position_with_aim() == 900

    dive = Dive(data.input_file)
    print(dive.position())
    print(dive.position_with_aim())
