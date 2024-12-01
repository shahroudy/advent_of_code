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
