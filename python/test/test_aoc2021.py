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
