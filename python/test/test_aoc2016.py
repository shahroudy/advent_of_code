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


def test_day09_samples():
    from aoc2016.day09.d09 import ExplosivesInCyberspace

    test = ExplosivesInCyberspace("./python/aoc2016/day09/sample1.txt")
    assert test.get_length(version=1) == 6
    test = ExplosivesInCyberspace("./python/aoc2016/day09/sample2.txt")
    assert test.get_length(version=1) == 7
    test = ExplosivesInCyberspace("./python/aoc2016/day09/sample3.txt")
    assert test.get_length(version=1) == 9
    assert test.get_length(version=2) == 9
    test = ExplosivesInCyberspace("./python/aoc2016/day09/sample4.txt")
    assert test.get_length(version=1) == 11
    test = ExplosivesInCyberspace("./python/aoc2016/day09/sample5.txt")
    assert test.get_length(version=1) == 6
    test = ExplosivesInCyberspace("./python/aoc2016/day09/sample6.txt")
    assert test.get_length(version=1) == 18
    assert test.get_length(version=2) == 20
    test = ExplosivesInCyberspace("./python/aoc2016/day09/sample7.txt")
    assert test.get_length(version=2) == 241920
    test = ExplosivesInCyberspace("./python/aoc2016/day09/sample8.txt")
    assert test.get_length(version=2) == 445


def test_day09():
    from aoc2016.day09.d09 import ExplosivesInCyberspace

    puzzle = ExplosivesInCyberspace(f"{input_folder}/aoc2016_day09.txt")
    assert puzzle.get_length(version=1) == 97714
    assert puzzle.get_length(version=2) == 10762972461


def test_day10_samples():
    from aoc2016.day10.d10 import BalanceBots

    test = BalanceBots("./python/aoc2016/day10/sample1.txt", {2, 5})
    assert test.searched_bot == 2
    test = BalanceBots("./python/aoc2016/day10/sample1.txt", {2, 3})
    assert test.searched_bot == 1
    test = BalanceBots("./python/aoc2016/day10/sample1.txt", {3, 5})
    assert test.searched_bot == 0


def test_day10():
    from aoc2016.day10.d10 import BalanceBots

    puzzle = BalanceBots(f"{input_folder}/aoc2016_day10.txt")
    assert puzzle.searched_bot == 147
    assert puzzle.final_output == 55637


def test_day11_samples():
    from aoc2016.day11.d11 import RadioisotopeThermoelectricGenerators

    test = RadioisotopeThermoelectricGenerators("./python/aoc2016/day11/sample1.txt")
    assert test.min_number_of_steps() == 11


def test_day11():
    from aoc2016.day11.d11 import RadioisotopeThermoelectricGenerators

    puzzle = RadioisotopeThermoelectricGenerators(f"{input_folder}/aoc2016_day11.txt")
    assert puzzle.min_number_of_steps() == 37
    assert puzzle.min_number_of_steps_with_extra_parts() == 61


def test_day12_samples():
    from aoc2016.day12.d12 import LeonardosMonorail

    test = LeonardosMonorail("./python/aoc2016/day12/sample1.txt")
    assert test.run_assembunny_code() == 42


def test_day12():
    from aoc2016.day12.d12 import LeonardosMonorail

    puzzle = LeonardosMonorail(f"{input_folder}/aoc2016_day12.txt")
    assert puzzle.run_assembunny_code() == 318009
    assert puzzle.run_assembunny_code(ignition=1) == 9227663


def test_day13_samples():
    from aoc2016.day13.d13 import AMazeOfTwistyLittleCubicles

    test = AMazeOfTwistyLittleCubicles("./python/aoc2016/day13/sample1.txt")
    assert test.shortest_path_to(7, 4) == 11


def test_day13():
    from aoc2016.day13.d13 import AMazeOfTwistyLittleCubicles

    puzzle = AMazeOfTwistyLittleCubicles(f"{input_folder}/aoc2016_day13.txt")
    assert puzzle.shortest_path_to(31, 39) == 86
    assert puzzle.locations_reachable_by_50_steps() == 127


def test_day14_samples():
    from aoc2016.day14.d14 import OneTimePad

    test = OneTimePad("./python/aoc2016/day14/sample1.txt")
    assert test.find_64th_key() == 22728
    assert test.find_64th_key(2016) == 22551


def test_day14():
    from aoc2016.day14.d14 import OneTimePad

    puzzle = OneTimePad(f"{input_folder}/aoc2016_day14.txt")
    assert puzzle.find_64th_key() == 35186
    assert puzzle.find_64th_key(2016) == 22429


def test_day15_samples():
    from aoc2016.day15.d15 import TimingIsEverything

    test = TimingIsEverything("./python/aoc2016/day15/sample1.txt")
    assert test.fist_capsule_passing_time() == 5


def test_day15():
    from aoc2016.day15.d15 import TimingIsEverything

    puzzle = TimingIsEverything(f"{input_folder}/aoc2016_day15.txt")
    assert puzzle.fist_capsule_passing_time() == 400589
    assert puzzle.fist_capsule_passing_time(extra_disc=True) == 3045959


def test_day16_samples():
    from aoc2016.day16.d16 import Puzzle

    test = Puzzle("./python/aoc2016/day16/sample1.txt")
    assert test.checksum() == "01100"


def test_day16():
    from aoc2016.day16.d16 import Puzzle

    puzzle = Puzzle(f"{input_folder}/aoc2016_day16.txt")
    assert puzzle.checksum(disk_len=272) == "10101001010100001"
    assert puzzle.checksum(disk_len=35651584) == "10100001110101001"


def test_day17_samples():
    from aoc2016.day17.d17 import TwoStepsForward

    test = TwoStepsForward("./python/aoc2016/day17/sample1.txt")
    assert test.shortest_path() == "DDRRRD"
    assert test.length_of_longest_path() == 370
    test = TwoStepsForward("./python/aoc2016/day17/sample2.txt")
    assert test.shortest_path() == "DDUDRLRRUDRD"
    assert test.length_of_longest_path() == 492
    test = TwoStepsForward("./python/aoc2016/day17/sample3.txt")
    assert test.shortest_path() == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"
    assert test.length_of_longest_path() == 830


def test_day17():
    from aoc2016.day17.d17 import TwoStepsForward

    puzzle = TwoStepsForward(f"{input_folder}/aoc2016_day17.txt")
    assert puzzle.shortest_path() == "DUDDRLRRRD"
    assert puzzle.length_of_longest_path() == 578


def test_day18_samples():
    from aoc2016.day18.d18 import LikeARogue

    test = LikeARogue("./python/aoc2016/day18/sample1.txt")
    assert test.safe_count(3) == 6
    test = LikeARogue("./python/aoc2016/day18/sample2.txt")
    assert test.safe_count(10) == 38


def test_day18():
    from aoc2016.day18.d18 import LikeARogue

    puzzle = LikeARogue(f"{input_folder}/aoc2016_day18.txt")
    assert puzzle.safe_count(40) == 1961
    assert puzzle.safe_count(400000) == 20000795


def test_day19_samples():
    from aoc2016.day19.d19 import AnElephantNamedJoseph

    test = AnElephantNamedJoseph(5)
    assert test.who_wins_grab_from_left() == 3
    assert test.who_wins_grab_from_front() == 2
    test = AnElephantNamedJoseph(20)
    assert test.who_wins_grab_from_front() == 13
    test = AnElephantNamedJoseph(100)
    assert test.who_wins_grab_from_front() == 19
    test = AnElephantNamedJoseph(200)
    assert test.who_wins_grab_from_front() == 157
    test = AnElephantNamedJoseph(999)
    assert test.who_wins_grab_from_front() == 270


def test_day19():
    from aoc2016.day19.d19 import AnElephantNamedJoseph

    puzzle = AnElephantNamedJoseph(f"{input_folder}/aoc2016_day19.txt")
    assert puzzle.who_wins_grab_from_left() == 1834903
    assert puzzle.who_wins_grab_from_front() == 1420280
