import os

from aoc2015.day01.d01 import NotQuiteLisp
from aoc2015.day02.d02 import IWasToldThereWouldBeNoMath
from aoc2015.day03.d03 import PerfectlySphericalHousesInAVacuum
from aoc2015.day04.d04 import TheIdealStockingStuffer
from aoc2015.day05.d05 import DoesntHeHaveInternElvesForThis
from aoc2015.day06.d06 import ProbablyAFireHazard
from aoc2015.day07.d07 import SomeAssemblyRequired
from aoc2015.day08.d08 import Matchsticks
from aoc2015.day09.d09 import AllInASingleNight

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


def test_day04_samples():
    test = TheIdealStockingStuffer("./python/aoc2015/day04/sample1.txt")
    assert test.mine() == 609043
    test = TheIdealStockingStuffer("./python/aoc2015/day04/sample2.txt")
    assert test.mine() == 1048970


def test_day04():
    puzzle = TheIdealStockingStuffer(f"{input_folder}/aoc2015_day04.txt")
    assert puzzle.mine() == 282749
    assert puzzle.mine(zeroes=6) == 9962624


def test_day05_samples():
    test = DoesntHeHaveInternElvesForThis("./python/aoc2015/day05/sample1.txt")
    assert test.nice_a == [True, True, False, False, False]
    test = DoesntHeHaveInternElvesForThis("./python/aoc2015/day05/sample2.txt")
    assert test.nice_b == [True, True, False, False]


def test_day05():
    puzzle = DoesntHeHaveInternElvesForThis(f"{input_folder}/aoc2015_day05.txt")
    assert sum(puzzle.nice_a) == 258
    assert sum(puzzle.nice_b) == 53


def test_day06_samples():
    test = ProbablyAFireHazard("./python/aoc2015/day06/sample1.txt")
    assert test.lit_lights() == 1000000
    test = ProbablyAFireHazard("./python/aoc2015/day06/sample2.txt")
    assert test.lit_lights() == 1000
    test = ProbablyAFireHazard("./python/aoc2015/day06/sample3.txt")
    assert test.lit_lights() == 0
    test = ProbablyAFireHazard("./python/aoc2015/day06/sample4.txt")
    assert test.brightness_sum() == 1
    test = ProbablyAFireHazard("./python/aoc2015/day06/sample5.txt")
    assert test.brightness_sum() == 2000000


def test_day06():
    puzzle = ProbablyAFireHazard(f"{input_folder}/aoc2015_day06.txt")
    assert puzzle.lit_lights() == 543903
    assert puzzle.brightness_sum() == 14687245


def test_day07_samples():
    test = SomeAssemblyRequired("./python/aoc2015/day07/sample1.txt")
    assert test.first_execution() == 65079


def test_day07():
    puzzle = SomeAssemblyRequired(f"{input_folder}/aoc2015_day07.txt")
    assert puzzle.first_execution() == 46065
    assert puzzle.second_execution() == 14134


def test_day08_samples():
    test = Matchsticks("./python/aoc2015/day08/sample1.txt")
    assert test.extra_chars_from_string_literals() == 12
    assert test.extra_chars_from_encoding() == 19


def test_day08():
    puzzle = Matchsticks(f"{input_folder}/aoc2015_day08.txt")
    assert puzzle.extra_chars_from_string_literals() == 1333
    assert puzzle.extra_chars_from_encoding() == 2046


def test_day09_samples():
    test = AllInASingleNight("./python/aoc2015/day09/sample1.txt")
    assert test.min_distance == 605
    assert test.max_distance == 982


def test_day09():
    puzzle = AllInASingleNight(f"{input_folder}/aoc2015_day09.txt")
    assert puzzle.min_distance == 117
    assert puzzle.max_distance == 909
