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
        self.input = Path(filename).read_text().strip()

    def look_and_say(self, s=""):
        if s == "":
            s = self.input
        result = ""
        cnt = 1
        pre = ""
        for ch in s:
            if ch == pre:
                cnt += 1
            else:
                if pre != "":
                    result = f"{result}{cnt}{pre}"
                pre = ch
                cnt = 1
        result = f"{result}{cnt}{pre}"
        return result

    def calc1(self, n=40):
        s = self.input
        from time import time

        for i in range(n):
            t = time()
            s = self.look_and_say(s)
            print(i + 1, len(s), time() - t)
        return len(s)

    def calc2(self):
        return self.calc1(50)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = Puzzle(filename)
    assert answer1 is None or test.look_and_say() == answer1
    assert answer2 is None or test.calc2() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", "11", None)
    test_samples("sample2.txt", "21", None)
    test_samples("sample3.txt", "1211", None)
    test_samples("sample4.txt", "111221", None)
    test_samples("sample5.txt", "312211", None)

    print("Tests passed, starting with the puzzle")

    puzzle = Puzzle(data.input_file)

    # print(puzzle.calc1())
    print(puzzle.calc2())
