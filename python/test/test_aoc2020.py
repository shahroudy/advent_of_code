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


def test_day04_samples():
    from aoc2020.day04.d04 import PassportProcessing

    test = PassportProcessing("./python/aoc2020/day04/sample1.txt")
    assert test.passports_with_required_fields() == 2
    test = PassportProcessing("./python/aoc2020/day04/sample2.txt")
    assert test.fully_valid_passports() == 0
    test = PassportProcessing("./python/aoc2020/day04/sample3.txt")
    assert test.fully_valid_passports() == 4


def test_day04():
    from aoc2020.day04.d04 import PassportProcessing

    test = PassportProcessing(f"{input_folder}/aoc2020_day04.txt")
    assert test.passports_with_required_fields() == 192
    assert test.fully_valid_passports() == 101


def test_day05_samples():
    from aoc2020.day05.d05 import BinaryBoarding

    test = BinaryBoarding("./python/aoc2020/day05/sample1.txt")
    assert test.maximum_seat_id() == 357
    test = BinaryBoarding("./python/aoc2020/day05/sample2.txt")
    assert test.maximum_seat_id() == 820


def test_day05():
    from aoc2020.day05.d05 import BinaryBoarding

    test = BinaryBoarding(f"{input_folder}/aoc2020_day05.txt")
    assert test.maximum_seat_id() == 991
    assert test.id_of_my_seat() == 534


def test_day06_samples():
    from aoc2020.day06.d06 import CustomCustoms

    test = CustomCustoms("./python/aoc2020/day06/sample1.txt")
    assert test.count_anyone_answered() == 11
    assert test.count_everyone_answered() == 6


def test_day06():
    from aoc2020.day06.d06 import CustomCustoms

    test = CustomCustoms(f"{input_folder}/aoc2020_day06.txt")
    assert test.count_anyone_answered() == 6911
    assert test.count_everyone_answered() == 3473


def test_day07_samples():
    from aoc2020.day07.d07 import HandyHaversacks

    test = HandyHaversacks("./python/aoc2020/day07/sample1.txt")
    assert test.bag_colors_containing_shiny_gold() == 4
    assert test.number_of_bags_inside_a_shiny_gold() == 32
    test = HandyHaversacks("./python/aoc2020/day07/sample2.txt")
    assert test.number_of_bags_inside_a_shiny_gold() == 126


def test_day07():
    from aoc2020.day07.d07 import HandyHaversacks

    test = HandyHaversacks(f"{input_folder}/aoc2020_day07.txt")
    assert test.bag_colors_containing_shiny_gold() == 372
    assert test.number_of_bags_inside_a_shiny_gold() == 8015


def test_day08_samples():
    from aoc2020.day08.d08 import HandheldHalting

    test = HandheldHalting("./python/aoc2020/day08/sample1.txt")
    assert test.acc_value_before_looping() == 5
    assert test.acc_value_after_proper_termination() == 8


def test_day08():
    from aoc2020.day08.d08 import HandheldHalting

    test = HandheldHalting(f"{input_folder}/aoc2020_day08.txt")
    assert test.acc_value_before_looping() == 1930
    assert test.acc_value_after_proper_termination() == 1688


def test_day09_samples():
    from aoc2020.day09.d09 import EncodingError

    test = EncodingError("./python/aoc2020/day09/sample1.txt", 5)
    assert test.first_invalid == 127
    assert test.encryption_weakness() == 62


def test_day09():
    from aoc2020.day09.d09 import EncodingError

    test = EncodingError(f"{input_folder}/aoc2020_day09.txt")
    assert test.first_invalid == 400480901
    assert test.encryption_weakness() == 67587168
