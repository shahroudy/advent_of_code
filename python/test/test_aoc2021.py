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
