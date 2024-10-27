from pathlib import Path
from string import ascii_lowercase

from myutils.io_handler import get_input_data


class PermutationPromenade:
    def __init__(self, filename, program_count=16):
        self.process_input(filename)
        self.run_all_dances(program_count)

    def process_input(self, filename):
        self.dance_moves = []
        for line in Path(filename).read_text().strip().split(","):
            cmd = line[0]
            parts = line[1:].split("/")
            if cmd in "xs":
                parts = list(map(int, parts))
            self.dance_moves.append([cmd] + parts)

    def run_all_dances(self, program_count):
        programs = ascii_lowercase[:program_count]
        history = {programs: 0}
        iteration = 0
        fast_forwarded = False
        while iteration < 1e9:
            programs = self.dance(programs)
            iteration += 1
            if iteration == 1:
                self.after_first_dance = programs
            if fast_forwarded:
                continue
            if programs in history:
                period = iteration - history[programs]
                iteration += period * ((1e9 - iteration) // period)
                fast_forwarded = True
            else:
                history[programs] = iteration
        self.after_billions_dance = programs

    def dance(self, programs):
        s = list(programs)
        for cmd, *args in self.dance_moves:
            if cmd == "s":
                (n,) = args
                s = s[-n:] + s[:-n]
            elif cmd == "x":
                n, m = args
                s[n], s[m] = s[m], s[n]
            elif cmd == "p":
                a, b = args
                n, m = s.index(a), s.index(b)
                s[n], s[m] = s[m], s[n]
        return "".join(s)


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = PermutationPromenade("sample1.txt", program_count=5)
    assert test.after_first_dance == "baedc"

    print("Tests passed, starting with the puzzle")

    puzzle = PermutationPromenade(data.input_file)

    print(puzzle.after_first_dance)
    print(puzzle.after_billions_dance)
