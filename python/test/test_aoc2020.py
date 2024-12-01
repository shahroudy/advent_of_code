import os

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    from aoc2020.day01.d01 import ReportRepair

    test = ReportRepair("./python/aoc2020/day01/sample1.txt")
    assert test.multiplication_of_two() == 514579
    assert test.multiplication_of_three() == 241861950


def test_day01():
    from aoc2020.day01.d01 import ReportRepair

    test = ReportRepair(f"{input_folder}/aoc2020_day01.txt")
    assert test.multiplication_of_two() == 494475
    assert test.multiplication_of_three() == 267520550


def test_day02_samples():
    from aoc2020.day02.d02 import PasswordPhilosophy

    test = PasswordPhilosophy("./python/aoc2020/day02/sample1.txt")
    assert test.valid_passwords_count() == 2
    assert test.valid_passwords_position() == 1


def test_day02():
    from aoc2020.day02.d02 import PasswordPhilosophy

    test = PasswordPhilosophy(f"{input_folder}/aoc2020_day02.txt")
    assert test.valid_passwords_count() == 398
    assert test.valid_passwords_position() == 562


def test_day03_samples():
    from aoc2020.day03.d03 import TobogganTrajectory

    test = TobogganTrajectory("./python/aoc2020/day03/sample1.txt")
    assert test.tree_count() == 7
    assert test.multiplication_of_tree_counts_for_all_slopes() == 336


def test_day03():
    from aoc2020.day03.d03 import TobogganTrajectory

    test = TobogganTrajectory(f"{input_folder}/aoc2020_day03.txt")
    assert test.tree_count() == 211
    assert test.multiplication_of_tree_counts_for_all_slopes() == 3584591857
