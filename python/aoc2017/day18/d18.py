from collections import deque
from pathlib import Path
from string import ascii_lowercase

from myutils.io_handler import get_input_data


class Duet:
    def __init__(self, filename):
        self.inp = [line.split(" ") for line in Path(filename).read_text().splitlines()]

    def value(self, x, registers):
        return registers[x] if x in registers else int(x)

    def recovered_frequency(self):
        registers = {c: 0 for c in ascii_lowercase}
        head = 0
        while 0 <= head < len(self.inp):
            cmd, *args = self.inp[head]
            if cmd == "snd":
                last_sound = self.value(args[0], registers)
            elif cmd == "set":
                registers[args[0]] = self.value(args[1], registers)
            elif cmd == "add":
                registers[args[0]] += self.value(args[1], registers)
            elif cmd == "mul":
                registers[args[0]] *= self.value(args[1], registers)
            elif cmd == "mod":
                registers[args[0]] %= self.value(args[1], registers)
            elif cmd == "rcv":
                if (self.value(args[0], registers)) != 0:
                    return last_sound
            elif cmd == "jgz":
                if (self.value(args[0], registers)) > 0:
                    head += (self.value(args[1], registers)) - 1
            head += 1

    def program(self, program_number=0):
        registers = {c: 0 for c in ascii_lowercase}
        registers["p"] = program_number
        snd_buf, rcv_buf = self.buffers if program_number else self.buffers[::-1]
        head = 0
        while 0 <= head < len(self.inp):
            cmd, *args = self.inp[head]
            if cmd == "set":
                registers[args[0]] = self.value(args[1], registers)
            elif cmd == "add":
                registers[args[0]] += self.value(args[1], registers)
            elif cmd == "mul":
                registers[args[0]] *= self.value(args[1], registers)
            elif cmd == "mod":
                registers[args[0]] %= self.value(args[1], registers)
            elif cmd == "jgz":
                if (self.value(args[0], registers)) > 0:
                    head += (self.value(args[1], registers)) - 1
            elif cmd == "snd":
                snd_buf.append(self.value(args[0], registers))
                self.program_one_sent_signals += program_number
            elif cmd == "rcv":
                if rcv_buf:
                    registers[args[0]] = rcv_buf.popleft()
                else:
                    yield True
                    head -= 1
            head += 1
        return False

    def sent_values_before_deadlock(self):
        self.program_one_sent_signals = 0
        self.buffers = [deque(), deque()]
        programs = [self.program(0), self.program(1)]
        program_running = [True, True]
        while any(program_running):
            for p in range(2):
                program_running[p] = program_running[p] and next(programs[p])
            if not any(self.buffers):
                break
        return self.program_one_sent_signals


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Duet("sample1.txt").recovered_frequency() == 4
    assert Duet("sample2.txt").sent_values_before_deadlock() == 3

    print("Tests passed, starting with the puzzle")

    puzzle = Duet(data.input_file)

    print(puzzle.recovered_frequency())
    print(puzzle.sent_values_before_deadlock())
