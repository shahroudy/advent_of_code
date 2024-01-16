import os

from aoc2018.day13.d13 import MineCartMadness

input_folder = os.environ.get("aoc_inputs")


def test_day13_samples():
    test = MineCartMadness("./python/aoc2018/day13/sample1.txt")
    assert test.first_crash == (7, 3)
    test = MineCartMadness("./python/aoc2018/day13/sample2.txt")
    assert test.last_cart == (6, 4)


def test_day13():
    test = MineCartMadness(f"{input_folder}/aoc2018_day13.txt")
    assert test.first_crash == (58, 93)
    assert test.last_cart == (91, 72)
