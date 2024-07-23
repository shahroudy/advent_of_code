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


def test_day04_samples():
    from aoc2016.day04.d04 import SecurityThroughObscurity

    test = SecurityThroughObscurity("./python/aoc2016/day04/sample1.txt")
    assert test.sum_of_real_sector_ids() == 1514
    assert test.decrypt("qzmt-zixmtkozy-ivhz", 343) == "very encrypted name"


def test_day04():
    from aoc2016.day04.d04 import SecurityThroughObscurity

    puzzle = SecurityThroughObscurity(f"{input_folder}/aoc2016_day04.txt")
    assert puzzle.sum_of_real_sector_ids() == 245102
    assert puzzle.sector_id_of_northpole_storage() == 324


def test_day05_samples():
    from aoc2016.day05.d05 import HowAboutANiceGameOfChess

    test = HowAboutANiceGameOfChess("./python/aoc2016/day05/sample1.txt")
    assert test.first_password == "18f47a30"
    assert test.second_password == "05ace8e3"


def test_day05():
    from aoc2016.day05.d05 import HowAboutANiceGameOfChess

    puzzle = HowAboutANiceGameOfChess(f"{input_folder}/aoc2016_day05.txt")
    assert puzzle.first_password == "1a3099aa"
    assert puzzle.second_password == "694190cd"


def test_day06_samples():
    from aoc2016.day06.d06 import SignalsAndNoise

    test = SignalsAndNoise("./python/aoc2016/day06/sample1.txt")
    assert test.most_common == "easter"
    assert test.least_common == "advent"


def test_day06():
    from aoc2016.day06.d06 import SignalsAndNoise

    puzzle = SignalsAndNoise(f"{input_folder}/aoc2016_day06.txt")
    assert puzzle.most_common == "mshjnduc"
    assert puzzle.least_common == "apfeeebz"


def test_day07_samples():
    from aoc2016.day07.d07 import InternetProtocolVersion7

    assert InternetProtocolVersion7("./python/aoc2016/day07/sample1.txt").TLS_count() == 2
    assert InternetProtocolVersion7("./python/aoc2016/day07/sample2.txt").SSL_count() == 3


def test_day07():
    from aoc2016.day07.d07 import InternetProtocolVersion7

    puzzle = InternetProtocolVersion7(f"{input_folder}/aoc2016_day07.txt")
    assert puzzle.TLS_count() == 105
    assert puzzle.SSL_count() == 258


def test_day08_samples():
    from aoc2016.day08.d08 import TwoFactorAuthentication

    test = TwoFactorAuthentication("./python/aoc2016/day08/sample1.txt")
    assert test.lit_led_count() == 6


def test_day08():
    from aoc2016.day08.d08 import TwoFactorAuthentication

    puzzle = TwoFactorAuthentication(f"{input_folder}/aoc2016_day08.txt")
    assert puzzle.lit_led_count() == 115
