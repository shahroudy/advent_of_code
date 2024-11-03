from pathlib import Path

from myutils.io_handler import get_input_data


class CoprocessorConflagration:
    def __init__(self, filename):
        self.code = [line.split() for line in Path(filename).read_text().splitlines()]

    def mul_count(self):
        def get(val):
            return registers[val] if val in registers else int(val)

        registers = {r: 0 for r in "abcdefgh"}
        head, mul_counter = 0, 0
        while head < len(self.code):
            cmd, X, Y = self.code[head]
            head += 1
            if cmd == "set":
                registers[X] = get(Y)
            elif cmd == "sub":
                registers[X] -= get(Y)
            elif cmd == "mul":
                registers[X] *= get(Y)
                mul_counter += 1
            elif cmd == "jnz":
                if get(X) != 0:
                    head += get(Y) - 1
        return mul_counter

    def run_debug_mode(self):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        def value(line):
            return int(self.code[line][2])

        start = value(0) * value(4) - value(5)
        stop = start - value(7)
        step = -value(30)
        return sum(not is_prime(i) for i in range(start, stop + 1, step))


if __name__ == "__main__":
    data = get_input_data(__file__)
    puzzle = CoprocessorConflagration(data.input_file)
    print(puzzle.mul_count())
    print(puzzle.run_debug_mode())
