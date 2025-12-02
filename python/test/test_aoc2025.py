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
