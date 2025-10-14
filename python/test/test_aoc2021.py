import os

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    from aoc2021.day01.d01 import SonarSweep

    test = SonarSweep("./python/aoc2021/day01/sample1.txt")
    assert test.depth_increments() == 7
    assert test.depth_windows_increments() == 5


def test_day01():
    from aoc2021.day01.d01 import SonarSweep

    test = SonarSweep(f"{input_folder}/aoc2021_day01.txt")
    assert test.depth_increments() == 1665
    assert test.depth_windows_increments() == 1702


def test_day02_samples():
    from aoc2021.day02.d02 import Dive

    test = Dive("./python/aoc2021/day02/sample1.txt")
    assert test.final_depth() == 150
    assert test.final_depth_with_aim() == 900


def test_day02():
    from aoc2021.day02.d02 import Dive

    test = Dive(f"{input_folder}/aoc2021_day02.txt")
    assert test.final_depth() == 1989014
    assert test.final_depth_with_aim() == 2006917119


def test_day03_samples():
    from aoc2021.day03.d03 import BinaryDiagnostic

    test = BinaryDiagnostic("./python/aoc2021/day03/sample1.txt")
    assert test.power_consumption() == 198
    assert test.life_support_rating() == 230


def test_day03():
    from aoc2021.day03.d03 import BinaryDiagnostic

    test = BinaryDiagnostic(f"{input_folder}/aoc2021_day03.txt")
    assert test.power_consumption() == 3847100
    assert test.life_support_rating() == 4105235


def test_day04_samples():
    from aoc2021.day04.d04 import GiantSquid

    test = GiantSquid("./python/aoc2021/day04/sample1.txt")
    assert test.first_winning_board_score() == 4512
    assert test.last_winning_board_score() == 1924


def test_day04():
    from aoc2021.day04.d04 import GiantSquid

    test = GiantSquid(f"{input_folder}/aoc2021_day04.txt")
    assert test.first_winning_board_score() == 28082
    assert test.last_winning_board_score() == 8224


def test_day05_samples():
    from aoc2021.day05.d05 import HydrothermalVenture

    test = HydrothermalVenture("./python/aoc2021/day05/sample1.txt")
    assert test.count_overlaps(keep_diag=False) == 5
    assert test.count_overlaps(keep_diag=True) == 12


def test_day05():
    from aoc2021.day05.d05 import HydrothermalVenture

    test = HydrothermalVenture(f"{input_folder}/aoc2021_day05.txt")
    assert test.count_overlaps(keep_diag=False) == 5698
    assert test.count_overlaps(keep_diag=True) == 15463


def test_day06_samples():
    from aoc2021.day06.d06 import Lanternfish

    test = Lanternfish("./python/aoc2021/day06/sample1.txt")
    assert test.lanternfish_count(18) == 26
    assert test.lanternfish_count(80) == 5934
    assert test.lanternfish_count(256) == 26984457539


def test_day06():
    from aoc2021.day06.d06 import Lanternfish

    test = Lanternfish(f"{input_folder}/aoc2021_day06.txt")
    assert test.lanternfish_count(80) == 396210
    assert test.lanternfish_count(256) == 1770823541496


def test_day07_samples():
    from aoc2021.day07.d07 import TreacheryOfWhales

    test = TreacheryOfWhales("./python/aoc2021/day07/sample1.txt")
    assert test.least_needed_fuel_to_align(constant_rate=True) == 37
    assert test.least_needed_fuel_to_align(constant_rate=False) == 168


def test_day07():
    from aoc2021.day07.d07 import TreacheryOfWhales

    test = TreacheryOfWhales(f"{input_folder}/aoc2021_day07.txt")
    assert test.least_needed_fuel_to_align(constant_rate=True) == 356992
    assert test.least_needed_fuel_to_align(constant_rate=False) == 101268110


def test_day08_samples():
    from aoc2021.day08.d08 import SevenSegmentSearch

    test = SevenSegmentSearch("./python/aoc2021/day08/sample2.txt")
    assert test.count_simple_digits() == 26
    test = SevenSegmentSearch("./python/aoc2021/day08/sample1.txt")
    assert test.sum_of_all_output_values() == 5353
    test = SevenSegmentSearch("./python/aoc2021/day08/sample2.txt")
    assert test.sum_of_all_output_values() == 61229


def test_day08():
    from aoc2021.day08.d08 import SevenSegmentSearch

    test = SevenSegmentSearch(f"{input_folder}/aoc2021_day08.txt")
    assert test.count_simple_digits() == 383
    assert test.sum_of_all_output_values() == 998900


def test_day09_samples():
    from aoc2021.day09.d09 import SmokeBasin

    test = SmokeBasin("./python/aoc2021/day09/sample1.txt")
    assert test.sum_of_low_point_risk_levels() == 15
    assert test.three_largest_basins() == 1134


def test_day09():
    from aoc2021.day09.d09 import SmokeBasin

    test = SmokeBasin(f"{input_folder}/aoc2021_day09.txt")
    assert test.sum_of_low_point_risk_levels() == 444
    assert test.three_largest_basins() == 1168440
