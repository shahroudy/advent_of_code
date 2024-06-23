import os

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    from aoc2016.day01.d01 import NoTimeforATaxicab

    test = NoTimeforATaxicab("./python/aoc2016/day01/sample1.txt")
    assert test.distance_of_final_position() == 5
    test = NoTimeforATaxicab("./python/aoc2016/day01/sample2.txt")
    assert test.distance_of_final_position() == 2
    test = NoTimeforATaxicab("./python/aoc2016/day01/sample3.txt")
    assert test.distance_of_final_position() == 12
    test = NoTimeforATaxicab("./python/aoc2016/day01/sample4.txt")
    assert test.distance_of_first_revisited_position() == 4


def test_day01():
    from aoc2016.day01.d01 import NoTimeforATaxicab

    puzzle = NoTimeforATaxicab(f"{input_folder}/aoc2016_day01.txt")
    assert puzzle.distance_of_final_position() == 242
    assert puzzle.distance_of_first_revisited_position() == 150


def test_day02_samples():
    from aoc2016.day02.d02 import BathroomSecurity

    test = BathroomSecurity("./python/aoc2016/day02/sample1.txt")
    assert test.key_in("./python/aoc2016/day02/keypad1.txt") == "1985"
    assert test.key_in("./python/aoc2016/day02/keypad2.txt") == "5DB3"


def test_day02():
    from aoc2016.day02.d02 import BathroomSecurity

    puzzle = BathroomSecurity(f"{input_folder}/aoc2016_day02.txt")
    assert puzzle.key_in("./python/aoc2016/day02/keypad1.txt") == "33444"
    assert puzzle.key_in("./python/aoc2016/day02/keypad2.txt") == "446A6"


def test_day03_samples():
    from aoc2016.day03.d03 import SquaresWithThreeSides

    test = SquaresWithThreeSides("./python/aoc2016/day03/sample1.txt")
    assert test.sum_possible_horizontal() == 2
    assert test.sum_possible_vertical() == 3


def test_day03():
    from aoc2016.day03.d03 import SquaresWithThreeSides

    puzzle = SquaresWithThreeSides(f"{input_folder}/aoc2016_day03.txt")
    assert puzzle.sum_possible_horizontal() == 993
    assert puzzle.sum_possible_vertical() == 1849
