import os

from aoc2015.day01.d01 import NotQuiteLisp

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    test = NotQuiteLisp("./python/aoc2015/day01/sample1.txt")
    assert test.current_floor == 0
    test = NotQuiteLisp("./python/aoc2015/day01/sample2.txt")
    assert test.current_floor == 3
    test = NotQuiteLisp("./python/aoc2015/day01/sample3.txt")
    assert test.current_floor == -3
    test = NotQuiteLisp("./python/aoc2015/day01/sample4.txt")
    assert test.enter_basement == 1
    test = NotQuiteLisp("./python/aoc2015/day01/sample5.txt")
    assert test.enter_basement == 5


def test_day01():
    puzzle = NotQuiteLisp(f"{input_folder}/aoc2015_day01.txt")
    assert puzzle.current_floor == 74
    assert puzzle.enter_basement == 1795
