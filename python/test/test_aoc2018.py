import os

from aoc2018.day13.d13 import MineCartMadness
from aoc2018.day14.d14 import ChocolateCharts

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


def test_day14_samples():
    test = ChocolateCharts()
    assert test.calc1(9) == "5158916779"
    assert test.calc1(5) == "0124515891"
    assert test.calc1(18) == "9251071085"
    assert test.calc1(2018) == "5941429882"
    assert test.calc2("51589") == 9
    assert test.calc2("01245") == 5
    assert test.calc2("92510") == 18
    assert test.calc2("59414") == 2018


def test_day14():
    puzzle = ChocolateCharts()
    assert puzzle.calc1(165061) == "5992684592"
    assert puzzle.calc2("165061") == 20181148
