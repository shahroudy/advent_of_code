import os

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    from aoc2025.day01.d01 import SecretEntrance

    test = SecretEntrance("./python/aoc2025/day01/sample1.txt")
    assert test.count_zero_ends() == 3
    assert test.count_zero_passes() == 6


def test_day01():
    from aoc2025.day01.d01 import SecretEntrance

    test = SecretEntrance(f"{input_folder}/aoc2025_day01.txt")
    assert test.count_zero_ends() == 1135
    assert test.count_zero_passes() == 6558


def test_day02_samples():
    from aoc2025.day02.d02 import GiftShop

    test = GiftShop("./python/aoc2025/day02/sample1.txt")
    assert test.sum_of_invalid_ids(only_twice=True) == 1227775554
    assert test.sum_of_invalid_ids(only_twice=False) == 4174379265


def test_day02():
    from aoc2025.day02.d02 import GiftShop

    test = GiftShop(f"{input_folder}/aoc2025_day02.txt")
    assert test.sum_of_invalid_ids(only_twice=True) == 28846518423
    assert test.sum_of_invalid_ids(only_twice=False) == 31578210022


def test_day03_samples():
    from aoc2025.day03.d03 import Lobby

    test = Lobby("./python/aoc2025/day03/sample1.txt")
    assert test.maximum_joltage(2) == 357
    assert test.maximum_joltage(12) == 3121910778619


def test_day03():
    from aoc2025.day03.d03 import Lobby

    test = Lobby(f"{input_folder}/aoc2025_day03.txt")
    assert test.maximum_joltage(2) == 17100
    assert test.maximum_joltage(12) == 170418192256861


def test_day04_samples():
    from aoc2025.day04.d04 import PrintingDepartment

    test = PrintingDepartment("./python/aoc2025/day04/sample1.txt")
    assert test.number_of_accessible_rolls() == 13
    assert test.number_of_removed_rolls() == 43


def test_day04():
    from aoc2025.day04.d04 import PrintingDepartment

    test = PrintingDepartment(f"{input_folder}/aoc2025_day04.txt")
    assert test.number_of_accessible_rolls() == 1344
    assert test.number_of_removed_rolls() == 8112


def test_day05_samples():
    from aoc2025.day05.d05 import Cafeteria

    test = Cafeteria("./python/aoc2025/day05/sample1.txt")
    assert test.available_fresh_ingredients_count() == 3
    assert test.all_fresh_ingredients_count() == 14


def test_day05():
    from aoc2025.day05.d05 import Cafeteria

    test = Cafeteria(f"{input_folder}/aoc2025_day05.txt")
    assert test.available_fresh_ingredients_count() == 623
    assert test.all_fresh_ingredients_count() == 353507173555373


def test_day06_samples():
    from aoc2025.day06.d06 import TrashCompactor

    test = TrashCompactor("./python/aoc2025/day06/sample1.txt")
    assert test.grand_total(False) == 4277556
    assert test.grand_total(True) == 3263827


def test_day06():
    from aoc2025.day06.d06 import TrashCompactor

    test = TrashCompactor(f"{input_folder}/aoc2025_day06.txt")
    assert test.grand_total(False) == 4693159084994
    assert test.grand_total(True) == 11643736116335


def test_day07_samples():
    from aoc2025.day07.d07 import Laboratories

    test = Laboratories("./python/aoc2025/day07/sample1.txt")
    assert test.splits == 21
    assert test.total_paths == 40


def test_day07():
    from aoc2025.day07.d07 import Laboratories

    test = Laboratories(f"{input_folder}/aoc2025_day07.txt")
    assert test.splits == 1562
    assert test.total_paths == 24292631346665


def test_day08_samples():
    from aoc2025.day08.d08 import Playground

    test = Playground("./python/aoc2025/day08/sample1.txt", observe_at_step=10)
    assert test.three_largest_sizes == 40
    assert test.last_connection == 25272


def test_day08():
    from aoc2025.day08.d08 import Playground

    test = Playground(f"{input_folder}/aoc2025_day08.txt", observe_at_step=1000)
    assert test.three_largest_sizes == 133574
    assert test.last_connection == 2435100380


def test_day09_samples():
    from aoc2025.day09.d09 import MovieTheater

    test = MovieTheater("./python/aoc2025/day09/sample1.txt")
    assert test.largest_rectangle() == 50
    assert test.largest_rectangle_within_contour() == 24


def test_day09():
    from aoc2025.day09.d09 import MovieTheater

    test = MovieTheater(f"{input_folder}/aoc2025_day09.txt")
    assert test.largest_rectangle() == 4790063600
    assert test.largest_rectangle_within_contour() == 1516172795


def test_day10_samples():
    from aoc2025.day10.d10 import Factory

    test = Factory("./python/aoc2025/day10/sample1.txt")
    assert test.configure_the_indicator_lights() == 7
    assert test.configure_the_joltage() == 33


def test_day10():
    from aoc2025.day10.d10 import Factory

    test = Factory(f"{input_folder}/aoc2025_day10.txt")
    assert test.configure_the_indicator_lights() == 428
    assert test.configure_the_joltage() == 16613
