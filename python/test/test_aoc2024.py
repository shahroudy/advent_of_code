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


def test_day03_samples():
    from aoc2024.day03.d03 import MullItOver

    test = MullItOver("./python/aoc2024/day03/sample1.txt")
    assert test.sum_of_all_multiplications() == 161
    test = MullItOver("./python/aoc2024/day03/sample2.txt")
    assert test.sum_of_all_multiplications(True) == 48


def test_day03():
    from aoc2024.day03.d03 import MullItOver

    test = MullItOver(f"{input_folder}/aoc2024_day03.txt")
    assert test.sum_of_all_multiplications() == 168539636
    assert test.sum_of_all_multiplications(True) == 97529391


def test_day04_samples():
    from aoc2024.day04.d04 import CeresSearch

    test = CeresSearch("./python/aoc2024/day04/sample1.txt")
    assert test.count_XMAS() == 18
    assert test.count_X_MAS() == 9


def test_day04():
    from aoc2024.day04.d04 import CeresSearch

    test = CeresSearch(f"{input_folder}/aoc2024_day04.txt")
    assert test.count_XMAS() == 2401
    assert test.count_X_MAS() == 1822


def test_day05_samples():
    from aoc2024.day05.d05 import PrintQueue

    test = PrintQueue("./python/aoc2024/day05/sample1.txt")
    assert test.not_changed_medians_sum == 143
    assert test.changed_medians_sum == 123


def test_day05():
    from aoc2024.day05.d05 import PrintQueue

    test = PrintQueue(f"{input_folder}/aoc2024_day05.txt")
    assert test.not_changed_medians_sum == 6041
    assert test.changed_medians_sum == 4884


def test_day06_samples():
    from aoc2024.day06.d06 import GuardGallivant

    test = GuardGallivant("./python/aoc2024/day06/sample1.txt")
    assert test.number_of_visited_positions() == 41
    assert test.number_of_looping_obstructions() == 6


def test_day06():
    from aoc2024.day06.d06 import GuardGallivant

    test = GuardGallivant(f"{input_folder}/aoc2024_day06.txt")
    assert test.number_of_visited_positions() == 5162
    assert test.number_of_looping_obstructions() == 1909


def test_day07_samples():
    from aoc2024.day07.d07 import BridgeRepair

    test = BridgeRepair("./python/aoc2024/day07/sample1.txt")
    assert test.total_calibration(2) == 3749
    assert test.total_calibration(3) == 11387


def test_day07():
    from aoc2024.day07.d07 import BridgeRepair

    test = BridgeRepair(f"{input_folder}/aoc2024_day07.txt")
    assert test.total_calibration(2) == 3312271365652
    assert test.total_calibration(3) == 509463489296712


def test_day08_samples():
    from aoc2024.day08.d08 import ResonantCollinearity

    test = ResonantCollinearity("./python/aoc2024/day08/sample1.txt")
    assert test.count_antinode() == 14
    assert test.count_antinode(True) == 34
    test = ResonantCollinearity("./python/aoc2024/day08/sample2.txt")
    assert test.count_antinode(True) == 9


def test_day08():
    from aoc2024.day08.d08 import ResonantCollinearity

    test = ResonantCollinearity(f"{input_folder}/aoc2024_day08.txt")
    assert test.count_antinode() == 359
    assert test.count_antinode(True) == 1293


def test_day09_samples():
    from aoc2024.day09.d09 import DiskFragmenter

    test = DiskFragmenter("./python/aoc2024/day09/sample1.txt")
    assert test.checksum_after_moving_files() == 1928
    assert test.checksum_after_moving_files_in_blocks() == 2858


def test_day09():
    from aoc2024.day09.d09 import DiskFragmenter

    test = DiskFragmenter(f"{input_folder}/aoc2024_day09.txt")
    assert test.checksum_after_moving_files() == 6432869891895
    assert test.checksum_after_moving_files_in_blocks() == 6467290479134


def test_day10_samples():
    from aoc2024.day10.d10 import HoofIt

    assert HoofIt("./python/aoc2024/day10/sample1.txt").count_of_all_reachable_targets() == 1
    assert HoofIt("./python/aoc2024/day10/sample2.txt").count_of_all_reachable_targets() == 2
    assert HoofIt("./python/aoc2024/day10/sample3.txt").count_of_all_reachable_targets() == 4
    assert HoofIt("./python/aoc2024/day10/sample4.txt").count_of_all_reachable_targets() == 3
    assert HoofIt("./python/aoc2024/day10/sample5.txt").count_of_all_reachable_targets() == 36

    assert HoofIt("./python/aoc2024/day10/sample6.txt").sum_of_path_counts() == 3
    assert HoofIt("./python/aoc2024/day10/sample7.txt").sum_of_path_counts() == 13
    assert HoofIt("./python/aoc2024/day10/sample8.txt").sum_of_path_counts() == 227
    assert HoofIt("./python/aoc2024/day10/sample9.txt").sum_of_path_counts() == 81


def test_day10():
    from aoc2024.day10.d10 import HoofIt

    puzzle = HoofIt(f"{input_folder}/aoc2024_day10.txt")

    assert puzzle.count_of_all_reachable_targets() == 652
    assert puzzle.sum_of_path_counts() == 1432


def test_day11_samples():
    from aoc2024.day11.d11 import PlutonianPebbles

    assert PlutonianPebbles("./python/aoc2024/day11/sample1.txt").stone_count_after(1) == 3
    assert PlutonianPebbles("./python/aoc2024/day11/sample1.txt").stone_count_after(2) == 4
    assert PlutonianPebbles("./python/aoc2024/day11/sample1.txt").stone_count_after(3) == 5
    assert PlutonianPebbles("./python/aoc2024/day11/sample1.txt").stone_count_after(4) == 9
    assert PlutonianPebbles("./python/aoc2024/day11/sample1.txt").stone_count_after(5) == 13
    assert PlutonianPebbles("./python/aoc2024/day11/sample1.txt").stone_count_after(6) == 22
    assert PlutonianPebbles("./python/aoc2024/day11/sample1.txt").stone_count_after(25) == 55312


def test_day11():
    from aoc2024.day11.d11 import PlutonianPebbles

    data = f"{input_folder}/aoc2024_day11.txt"

    assert PlutonianPebbles(data).stone_count_after(25) == 189092
    assert PlutonianPebbles(data).stone_count_after(75) == 224869647102559


def test_day12_samples():
    from aoc2024.day12.d12 import GardenGroups

    assert GardenGroups("./python/aoc2024/day12/sample1.txt").total_price() == 140
    assert GardenGroups("./python/aoc2024/day12/sample2.txt").total_price() == 772
    assert GardenGroups("./python/aoc2024/day12/sample3.txt").total_price() == 1930

    assert GardenGroups("./python/aoc2024/day12/sample1.txt").total_price_discounted() == 80
    assert GardenGroups("./python/aoc2024/day12/sample2.txt").total_price_discounted() == 436
    assert GardenGroups("./python/aoc2024/day12/sample3.txt").total_price_discounted() == 1206
    assert GardenGroups("./python/aoc2024/day12/sample4.txt").total_price_discounted() == 368


def test_day12():
    from aoc2024.day12.d12 import GardenGroups

    data = f"{input_folder}/aoc2024_day12.txt"

    assert GardenGroups(data).total_price() == 1421958
    assert GardenGroups(data).total_price_discounted() == 885394


def test_day13_samples():
    from aoc2024.day13.d13 import ClawContraption

    assert ClawContraption("./python/aoc2024/day13/sample1.txt").min_tokens_for_most_win() == 480


def test_day13():
    from aoc2024.day13.d13 import ClawContraption

    data = f"{input_folder}/aoc2024_day13.txt"

    assert ClawContraption(data).min_tokens_for_most_win() == 25751
    assert ClawContraption(data).min_tokens_for_most_win(10000000000000) == 108528956728655


def test_day14_samples():
    from aoc2024.day14.d14 import RestroomRedoubt

    test = RestroomRedoubt("./python/aoc2024/day14/sample1.txt", cols=11, rows=7)
    assert test.safety_factor() == 12


def test_day14():
    from aoc2024.day14.d14 import RestroomRedoubt

    data = f"{input_folder}/aoc2024_day14.txt"
    puzzle = RestroomRedoubt(data, cols=101, rows=103)
    assert puzzle.safety_factor() == 215476074
    assert puzzle.time_to_display_easter_egg(display=False) == 6285
