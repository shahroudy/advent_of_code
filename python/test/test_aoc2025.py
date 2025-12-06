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
