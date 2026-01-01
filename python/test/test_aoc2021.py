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


def test_day02_samples():
    from aoc2021.day02.d02 import Dive

    test = Dive("./python/aoc2021/day02/sample1.txt")
    assert test.final_depth() == 150
    assert test.final_depth_with_aim() == 900


def test_day02():
    from aoc2021.day02.d02 import Dive

    test = Dive(f"{input_folder}/aoc2021_day02.txt")
    assert test.final_depth() == 1989014
    assert test.final_depth_with_aim() == 2006917119


def test_day03_samples():
    from aoc2021.day03.d03 import BinaryDiagnostic

    test = BinaryDiagnostic("./python/aoc2021/day03/sample1.txt")
    assert test.power_consumption() == 198
    assert test.life_support_rating() == 230


def test_day03():
    from aoc2021.day03.d03 import BinaryDiagnostic

    test = BinaryDiagnostic(f"{input_folder}/aoc2021_day03.txt")
    assert test.power_consumption() == 3847100
    assert test.life_support_rating() == 4105235


def test_day04_samples():
    from aoc2021.day04.d04 import GiantSquid

    test = GiantSquid("./python/aoc2021/day04/sample1.txt")
    assert test.first_winning_board_score() == 4512
    assert test.last_winning_board_score() == 1924


def test_day04():
    from aoc2021.day04.d04 import GiantSquid

    test = GiantSquid(f"{input_folder}/aoc2021_day04.txt")
    assert test.first_winning_board_score() == 28082
    assert test.last_winning_board_score() == 8224


def test_day05_samples():
    from aoc2021.day05.d05 import HydrothermalVenture

    test = HydrothermalVenture("./python/aoc2021/day05/sample1.txt")
    assert test.count_overlaps(keep_diag=False) == 5
    assert test.count_overlaps(keep_diag=True) == 12


def test_day05():
    from aoc2021.day05.d05 import HydrothermalVenture

    test = HydrothermalVenture(f"{input_folder}/aoc2021_day05.txt")
    assert test.count_overlaps(keep_diag=False) == 5698
    assert test.count_overlaps(keep_diag=True) == 15463


def test_day06_samples():
    from aoc2021.day06.d06 import Lanternfish

    test = Lanternfish("./python/aoc2021/day06/sample1.txt")
    assert test.lanternfish_count(18) == 26
    assert test.lanternfish_count(80) == 5934
    assert test.lanternfish_count(256) == 26984457539


def test_day06():
    from aoc2021.day06.d06 import Lanternfish

    test = Lanternfish(f"{input_folder}/aoc2021_day06.txt")
    assert test.lanternfish_count(80) == 396210
    assert test.lanternfish_count(256) == 1770823541496


def test_day07_samples():
    from aoc2021.day07.d07 import TreacheryOfWhales

    test = TreacheryOfWhales("./python/aoc2021/day07/sample1.txt")
    assert test.least_needed_fuel_to_align(constant_rate=True) == 37
    assert test.least_needed_fuel_to_align(constant_rate=False) == 168


def test_day07():
    from aoc2021.day07.d07 import TreacheryOfWhales

    test = TreacheryOfWhales(f"{input_folder}/aoc2021_day07.txt")
    assert test.least_needed_fuel_to_align(constant_rate=True) == 356992
    assert test.least_needed_fuel_to_align(constant_rate=False) == 101268110


def test_day08_samples():
    from aoc2021.day08.d08 import SevenSegmentSearch

    test = SevenSegmentSearch("./python/aoc2021/day08/sample2.txt")
    assert test.count_simple_digits() == 26
    test = SevenSegmentSearch("./python/aoc2021/day08/sample1.txt")
    assert test.sum_of_all_output_values() == 5353
    test = SevenSegmentSearch("./python/aoc2021/day08/sample2.txt")
    assert test.sum_of_all_output_values() == 61229


def test_day08():
    from aoc2021.day08.d08 import SevenSegmentSearch

    test = SevenSegmentSearch(f"{input_folder}/aoc2021_day08.txt")
    assert test.count_simple_digits() == 383
    assert test.sum_of_all_output_values() == 998900


def test_day09_samples():
    from aoc2021.day09.d09 import SmokeBasin

    test = SmokeBasin("./python/aoc2021/day09/sample1.txt")
    assert test.sum_of_low_point_risk_levels() == 15
    assert test.three_largest_basins() == 1134


def test_day09():
    from aoc2021.day09.d09 import SmokeBasin

    test = SmokeBasin(f"{input_folder}/aoc2021_day09.txt")
    assert test.sum_of_low_point_risk_levels() == 444
    assert test.three_largest_basins() == 1168440


def test_day10_samples():
    from aoc2021.day10.d10 import SyntaxScoring

    test = SyntaxScoring("./python/aoc2021/day10/sample1.txt")
    assert test.total_syntax_error_score() == 26397
    assert test.middle_incomplete_score() == 288957


def test_day10():
    from aoc2021.day10.d10 import SyntaxScoring

    test = SyntaxScoring(f"{input_folder}/aoc2021_day10.txt")
    assert test.total_syntax_error_score() == 367059
    assert test.middle_incomplete_score() == 1952146692


def test_day11_samples():
    from aoc2021.day11.d11 import DumboOctopus

    test = DumboOctopus("./python/aoc2021/day11/sample1.txt")
    assert test.flash_count(step_count=2) == 9

    test = DumboOctopus("./python/aoc2021/day11/sample2.txt")
    assert test.flash_count() == 1656
    assert test.first_step_of_all_flash() == 195


def test_day11():
    from aoc2021.day11.d11 import DumboOctopus

    test = DumboOctopus(f"{input_folder}/aoc2021_day11.txt")
    assert test.flash_count() == 1705
    assert test.first_step_of_all_flash() == 265


def test_day12_samples():
    from aoc2021.day12.d12 import PassagePathing

    test = PassagePathing("./python/aoc2021/day12/sample1.txt")
    assert test.path_count(allowed_repeats=0) == 10
    assert test.path_count(allowed_repeats=1) == 36

    test = PassagePathing("./python/aoc2021/day12/sample2.txt")
    assert test.path_count(allowed_repeats=0) == 19
    assert test.path_count(allowed_repeats=1) == 103

    test = PassagePathing("./python/aoc2021/day12/sample3.txt")
    assert test.path_count(allowed_repeats=0) == 226
    assert test.path_count(allowed_repeats=1) == 3509


def test_day12():
    from aoc2021.day12.d12 import PassagePathing

    test = PassagePathing(f"{input_folder}/aoc2021_day12.txt")
    assert test.path_count(allowed_repeats=0) == 4970
    assert test.path_count(allowed_repeats=1) == 137948


def test_day13_samples():
    from aoc2021.day13.d13 import TransparentOrigami

    test = TransparentOrigami("./python/aoc2021/day13/sample1.txt")
    assert test.point_count_after_first_fold() == 17
    assert test.code_after_all_folds() == "#####\n#...#\n#...#\n#...#\n#####"


def test_day13():
    from aoc2021.day13.d13 import TransparentOrigami

    test = TransparentOrigami(f"{input_folder}/aoc2021_day13.txt")
    assert test.point_count_after_first_fold() == 664
    assert test.code_after_all_folds() == (
        "####.####...##.#..#.####.#....###..#...\n"
        "#....#.......#.#.#.....#.#....#..#.#...\n"
        "###..###.....#.##.....#..#....###..#...\n"
        "#....#.......#.#.#...#...#....#..#.#...\n"
        "#....#....#..#.#.#..#....#....#..#.#...\n"
        "####.#.....##..#..#.####.####.###..####"
    )


def test_day14_samples():
    from aoc2021.day14.d14 import ExtendedPolymerization

    test = ExtendedPolymerization("./python/aoc2021/day14/sample1.txt")
    assert test.quantity_difference_between_most_and_least_common(steps=0) == 1
    assert test.quantity_difference_between_most_and_least_common(steps=1) == 1
    assert test.quantity_difference_between_most_and_least_common(steps=10) == 1588
    assert test.quantity_difference_between_most_and_least_common(steps=40) == 2188189693529


def test_day14():
    from aoc2021.day14.d14 import ExtendedPolymerization

    test = ExtendedPolymerization(f"{input_folder}/aoc2021_day14.txt")
    assert test.quantity_difference_between_most_and_least_common(steps=10) == 2975
    assert test.quantity_difference_between_most_and_least_common(steps=40) == 3015383850689


def test_day15_samples():
    from aoc2021.day15.d15 import Chiton

    test = Chiton("./python/aoc2021/day15/sample1.txt")
    assert test.lowest_total_risk(extend_map=False) == 40
    assert test.lowest_total_risk(extend_map=True) == 315


def test_day15():
    from aoc2021.day15.d15 import Chiton

    test = Chiton(f"{input_folder}/aoc2021_day15.txt")
    assert test.lowest_total_risk(extend_map=False) == 562
    assert test.lowest_total_risk(extend_map=True) == 2874


def test_day16_samples():
    from aoc2021.day16.d16 import PacketDecoder

    assert PacketDecoder("./python/aoc2021/day16/sample1.txt").sum_of_packet_versions == 6
    assert PacketDecoder("./python/aoc2021/day16/sample2.txt").sum_of_packet_versions == 16
    assert PacketDecoder("./python/aoc2021/day16/sample3.txt").sum_of_packet_versions == 12
    assert PacketDecoder("./python/aoc2021/day16/sample4.txt").sum_of_packet_versions == 23
    assert PacketDecoder("./python/aoc2021/day16/sample5.txt").sum_of_packet_versions == 31

    assert PacketDecoder("./python/aoc2021/day16/sample1.txt").root_packet_value() == 2021
    assert PacketDecoder("./python/aoc2021/day16/sample6.txt").root_packet_value() == 3
    assert PacketDecoder("./python/aoc2021/day16/sample7.txt").root_packet_value() == 54
    assert PacketDecoder("./python/aoc2021/day16/sample8.txt").root_packet_value() == 7
    assert PacketDecoder("./python/aoc2021/day16/sample9.txt").root_packet_value() == 9
    assert PacketDecoder("./python/aoc2021/day16/sample10.txt").root_packet_value() == 1
    assert PacketDecoder("./python/aoc2021/day16/sample11.txt").root_packet_value() == 0
    assert PacketDecoder("./python/aoc2021/day16/sample12.txt").root_packet_value() == 0
    assert PacketDecoder("./python/aoc2021/day16/sample13.txt").root_packet_value() == 1


def test_day16():
    from aoc2021.day16.d16 import PacketDecoder

    test = PacketDecoder(f"{input_folder}/aoc2021_day16.txt")
    assert test.sum_of_packet_versions == 883
    assert test.root_packet_value() == 1675198555015


def test_day17_samples():
    from aoc2021.day17.d17 import TrickShot

    test = TrickShot("./python/aoc2021/day17/sample1.txt")
    assert test.highest_y == 45
    assert test.shot_count == 112


def test_day17():
    from aoc2021.day17.d17 import TrickShot

    test = TrickShot(f"{input_folder}/aoc2021_day17.txt")
    assert test.highest_y == 3916
    assert test.shot_count == 2986


def test_day18_samples():
    from aoc2021.day18.d18 import Snailfish

    test = Snailfish("./python/aoc2021/day18/sample1.txt")
    assert test.final_sum() == 4140
    assert test.max_sum_of_pairs() == 3993


def test_day18():
    from aoc2021.day18.d18 import Snailfish

    test = Snailfish(f"{input_folder}/aoc2021_day18.txt")
    assert test.final_sum() == 4008
    assert test.max_sum_of_pairs() == 4667


def test_day19_samples():
    from aoc2021.day19.d19 import BeaconScanner

    test1 = BeaconScanner("./python/aoc2021/day19/sample1.txt")
    assert test1.count_all_beacons() == 79
    assert test1.max_distance_between_scanners() == 3621


def test_day19():
    from aoc2021.day19.d19 import BeaconScanner

    test1 = BeaconScanner(f"{input_folder}/aoc2021_day19.txt")
    assert test1.count_all_beacons() == 313
    assert test1.max_distance_between_scanners() == 10656


def test_day20_samples():
    from aoc2021.day20.d20 import TrenchMap

    test1 = TrenchMap("./python/aoc2021/day20/sample1.txt")
    assert test1.enhance(2) == 35
    assert test1.enhance(50) == 3351


def test_day20():
    from aoc2021.day20.d20 import TrenchMap

    test1 = TrenchMap(f"{input_folder}/aoc2021_day20.txt")
    assert test1.enhance(2) == 4873
    assert test1.enhance(50) == 16394
