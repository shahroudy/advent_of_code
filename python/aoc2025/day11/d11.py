from functools import cache
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import find_all_per_line_re


class Reactor:
    def __init__(self, fn):
        self.outs = {d[0]: set(d[1:]) for d in find_all_per_line_re(r"(\w+)", Path(fn).read_text())}

    @cache
    def find_ways(self, start, goal, avoid=tuple()):
        if start == goal:
            return 1
        return sum(self.find_ways(n, goal, avoid) for n in self.outs[start] if n not in avoid)

    def you_to_out_paths(self):
        return self.find_ways("you", "out")

    def svr_to_out_paths_through_fft_dac(self):
        server_to_fft = self.find_ways("svr", "fft", ("dac", "out"))
        fft_to_dac = self.find_ways("fft", "dac", ("svr", "out"))
        dac_to_out = self.find_ways("dac", "out", ("svr", "fft"))

        fft_to_out = self.find_ways("svr", "dac", ("fft", "out"))
        dac_to_fft = self.find_ways("dac", "fft", ("svr", "out"))
        fft_to_out = self.find_ways("fft", "out", ("svr", " dac"))

        return server_to_fft * fft_to_dac * dac_to_out + fft_to_out * dac_to_fft * fft_to_out


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Reactor("sample1.txt").you_to_out_paths() == 5
    assert Reactor("sample2.txt").svr_to_out_paths_through_fft_dac() == 2

    print("Tests passed, starting with the puzzle")

    puzzle = Reactor(data.input_file)

    print(puzzle.you_to_out_paths())
    print(puzzle.svr_to_out_paths_through_fft_dac())
