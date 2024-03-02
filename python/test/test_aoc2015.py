import os

from aoc2015.day01.d01 import NotQuiteLisp
from aoc2015.day02.d02 import IWasToldThereWouldBeNoMath
from aoc2015.day03.d03 import PerfectlySphericalHousesInAVacuum

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


def test_day02_samples():
    test = IWasToldThereWouldBeNoMath("./python/aoc2015/day02/sample1.txt")
    assert test.total_wrapping_paper() == 58
    assert test.total_ribbon() == 34
    test = IWasToldThereWouldBeNoMath("./python/aoc2015/day02/sample2.txt")
    assert test.total_wrapping_paper() == 43
    assert test.total_ribbon() == 14


def test_day02():
    puzzle = IWasToldThereWouldBeNoMath(f"{input_folder}/aoc2015_day02.txt")
    assert puzzle.total_wrapping_paper() == 1606483
    assert puzzle.total_ribbon() == 3842356


def test_day03_samples():
    test = PerfectlySphericalHousesInAVacuum("./python/aoc2015/day03/sample1.txt")
    assert test.visited_houses_santa_alone() == 2
    test = PerfectlySphericalHousesInAVacuum("./python/aoc2015/day03/sample2.txt")
    assert test.visited_houses_santa_alone() == 4
    assert test.visited_houses_santa_and_robosanta() == 3
    test = PerfectlySphericalHousesInAVacuum("./python/aoc2015/day03/sample3.txt")
    assert test.visited_houses_santa_alone() == 2
    assert test.visited_houses_santa_and_robosanta() == 11
    test = PerfectlySphericalHousesInAVacuum("./python/aoc2015/day03/sample4.txt")
    assert test.visited_houses_santa_and_robosanta() == 3


def test_day03():
    puzzle = PerfectlySphericalHousesInAVacuum(f"{input_folder}/aoc2015_day03.txt")
    assert puzzle.visited_houses_santa_alone() == 2081
    assert puzzle.visited_houses_santa_and_robosanta() == 2341
