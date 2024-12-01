import os
from collections import defaultdict, deque

from myutils.file_reader import read_int_list
from myutils.io_handler import get_input_data


class IntcodeComputer:
    def __init__(self, program: list):
        self.init_program = program.copy()
        self.reset(deque())

    def load_program(self):
        self.program = defaultdict(int)
        for i in range(len(self.init_program)):
            self.program[i] = self.init_program[i]

    def reset(self, input: deque):
        self.load_program()
        self.head = 0
        self.input = input
        self.output = deque()
        self.halted = False
        self.relbase = 0

    def read_op_code(self):
        code = self.program[self.head]
        parts = [code % 100]
        code //= 100
        for _ in range(3):
            parts.append(code % 10)
            code //= 10
        return parts

    def read_one_operand(self, mode):
        self.head += 1
        operand = self.program[self.head]
        if mode == 0:
            operand = self.program[operand]
        elif mode == 2:
            operand = self.program[operand + self.relbase]
        elif mode == 1:
            pass
        else:
            raise Exception("Invalid mode!")
        return operand

    def read_operands(self, command):
        args = []
        arg_count = {99: 0, 1: 2, 2: 2, 3: 0, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 1}
        no_args = arg_count[command[0]]
        for i in range(no_args):
            args.append(self.read_one_operand(command[i + 1]))
        return args

    def write(self, address, value):
        self.program[address] = value

    def execute_command(self, command):
        op = command[0]
        args = self.read_operands(command)
        if op == 99:
            self.halted = True
        elif op in [1, 2, 7, 8, 3]:
            value = 0
            if op == 1:
                value = args[0] + args[1]
            elif op == 2:
                value = args[0] * args[1]
            elif op == 7:
                value = 1 if args[0] < args[1] else 0
            elif op == 8:
                value = 1 if args[0] == args[1] else 0
            elif op == 3:
                value = self.input.popleft()
            address = self.read_one_operand(1)
            if command[1 + len(args)] == 2:
                address += self.relbase
            self.write(address, value)
        elif op == 4:
            self.output.append(args[0])
        elif op in [5, 6]:
            if (op == 5 and args[0] != 0) or (op == 6 and args[0] == 0):
                self.head = args[1]
                return False
        elif op == 9:
            self.relbase += args[0]
        else:
            print("ERROR")
        self.head += 1

    def compute(self, input: deque):
        self.reset(input)
        while not self.halted:
            command = self.read_op_code()
            self.execute_command(command)
        return self.output

    def compute_while_input(self):
        while not self.halted:
            command = self.read_op_code()
            if (command[0] == 3) and (len(self.input) == 0):
                output = self.output
                self.output = deque()
                return output
            self.execute_command(command)
        output = self.output
        self.output = deque()
        return output

    # below code is added for day 7 usage
    def set_phase(self, phase):
        self.input.append(phase)

    def step(self, input=None):
        """
        This mode was originally used in day 7 code,
        it just starts with an input and stops when an output is generated,
        it will be returned with a new input later,
        this will go on till the computer halts!
        For day 11 and 13 code, this has been changed to output multiple codes
        """
        if input is not None:
            self.input.append(input)
        while not self.halted:
            command = self.read_op_code()
            if (command[0] == 3) and (len(self.input) == 0):
                break
            self.execute_command(command)
        out = self.output
        self.output = deque()
        return out


if __name__ == "__main__":
    data = get_input_data(__file__)
    test1 = read_int_list("test1.txt")
    computer_test1 = IntcodeComputer(test1)
    assert computer_test1.compute(deque()) == deque(test1)

    test2 = read_int_list("test2.txt")
    computer_test2 = IntcodeComputer(test2)
    test_output = computer_test2.compute(deque())
    assert len(str(test_output.pop())) == 16

    test3 = read_int_list("test3.txt")
    computer_test3 = IntcodeComputer(test3)
    assert computer_test3.compute(deque()).pop() == 1125899906842624

    prog = read_int_list(data.input_file)
    computer = IntcodeComputer(prog)
    print(computer.compute(deque([1])))
    print(computer.compute(deque([2])))
