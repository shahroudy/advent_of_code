import os

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    from aoc2024.day01.d01 import HistorianHysteria

    test = HistorianHysteria("./python/aoc2024/day01/sample1.txt")
    assert test.total_distance() == 11
    assert test.similarity_score() == 31


def test_day01():
    from aoc2024.day01.d01 import HistorianHysteria

    test = HistorianHysteria(f"{input_folder}/aoc2024_day01.txt")
    assert test.total_distance() == 2375403
    assert test.similarity_score() == 23082277


def test_day02_samples():
    from aoc2024.day02.d02 import RedNosedReports

    test = RedNosedReports("./python/aoc2024/day02/sample1.txt")
    assert test.safe_count(0) == 2
    assert test.safe_count(1) == 4


def test_day02():
    from aoc2024.day02.d02 import RedNosedReports

    test = RedNosedReports(f"{input_folder}/aoc2024_day02.txt")
    assert test.safe_count(0) == 472
    assert test.safe_count(1) == 520
