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


def test_day15_samples():
    from aoc2024.day15.d15 import WarehouseWoes

    test = WarehouseWoes("./python/aoc2024/day15/sample1.txt")
    assert test.move_boxes() == 2028
    test = WarehouseWoes("./python/aoc2024/day15/sample2.txt")
    assert test.move_boxes() == 10092
    assert test.move_boxes(is_second_warehouse=True) == 9021


def test_day15():
    from aoc2024.day15.d15 import WarehouseWoes

    data = f"{input_folder}/aoc2024_day15.txt"

    assert WarehouseWoes(data).move_boxes() == 1429911
    assert WarehouseWoes(data).move_boxes(is_second_warehouse=True) == 1453087


def test_day16_samples():
    from aoc2024.day16.d16 import ReindeerMaze

    test = ReindeerMaze("./python/aoc2024/day16/sample1.txt")
    assert test.lowest_score == 7036
    assert test.best_paths_tile_count == 45
    test = ReindeerMaze("./python/aoc2024/day16/sample2.txt")
    assert test.lowest_score == 11048
    assert test.best_paths_tile_count == 64


def test_day16():
    from aoc2024.day16.d16 import ReindeerMaze

    data = f"{input_folder}/aoc2024_day16.txt"
    puzzle = ReindeerMaze(data)
    assert puzzle.lowest_score == 89460
    assert puzzle.best_paths_tile_count == 504


def test_day17_samples():
    from aoc2024.day17.d17 import ChronospatialComputer

    test = ChronospatialComputer("./python/aoc2024/day17/sample1.txt")
    assert test.run_the_program() == "4,6,3,5,6,3,5,2,1,0"


def test_day17():
    from aoc2024.day17.d17 import ChronospatialComputer

    data = f"{input_folder}/aoc2024_day17.txt"
    puzzle = ChronospatialComputer(data)

    assert puzzle.run_the_program() == "1,5,3,0,2,5,2,5,3"
    assert puzzle.find_min_A_to_output_the_same_program() == 108107566389757


def test_day18_samples():
    from aoc2024.day18.d18 import RAMRun

    assert RAMRun("./python/aoc2024/day18/sample1.txt", 6).min_steps_to_reach_goal(12) == 22
    assert RAMRun("./python/aoc2024/day18/sample1.txt", 6).first_blocking_byte(12) == "6,1"


def test_day18():
    from aoc2024.day18.d18 import RAMRun

    data = f"{input_folder}/aoc2024_day18.txt"

    assert RAMRun(data, 70).min_steps_to_reach_goal(1024) == 280
    assert RAMRun(data, 70).first_blocking_byte(1024) == "28,56"


def test_day19_samples():
    from aoc2024.day19.d19 import LinenLayout

    test = LinenLayout("./python/aoc2024/day19/sample1.txt")
    assert test.number_of_possible_patters() == 6
    assert test.sum_of_all_possible_ways() == 16


def test_day19():
    from aoc2024.day19.d19 import LinenLayout

    data = f"{input_folder}/aoc2024_day19.txt"

    assert LinenLayout(data).number_of_possible_patters() == 313
    assert LinenLayout(data).sum_of_all_possible_ways() == 666491493769758


def test_day20_samples():
    from aoc2024.day20.d20 import RaceCondition

    assert RaceCondition("./python/aoc2024/day20/sample1.txt").cheat_count(2, 1) == 44
    assert RaceCondition("./python/aoc2024/day20/sample1.txt").cheat_count(20, 50) == 285


def test_day20():
    from aoc2024.day20.d20 import RaceCondition

    data = f"{input_folder}/aoc2024_day20.txt"

    puzzle = RaceCondition(data)

    assert puzzle.cheat_count(2, 100) == 1365
    assert puzzle.cheat_count(20, 100) == 986082


def test_day21_samples():
    from aoc2024.day21.d21 import KeypadConundrum

    assert KeypadConundrum("./python/aoc2024/day21/sample1.txt").sum_of_complexities(2) == 68 * 29
    assert KeypadConundrum("./python/aoc2024/day21/sample2.txt").sum_of_complexities(2) == 60 * 980
    assert KeypadConundrum("./python/aoc2024/day21/sample3.txt").sum_of_complexities(2) == 68 * 179
    assert KeypadConundrum("./python/aoc2024/day21/sample4.txt").sum_of_complexities(2) == 64 * 456
    assert KeypadConundrum("./python/aoc2024/day21/sample5.txt").sum_of_complexities(2) == 64 * 379
    assert KeypadConundrum("./python/aoc2024/day21/sample6.txt").sum_of_complexities(2) == 126384


def test_day21():
    from aoc2024.day21.d21 import KeypadConundrum

    data = f"{input_folder}/aoc2024_day21.txt"

    assert KeypadConundrum(data).sum_of_complexities(2) == 222670
    assert KeypadConundrum(data).sum_of_complexities(25) == 271397390297138


def test_day22_samples():
    from aoc2024.day22.d22 import MonkeyMarket

    assert MonkeyMarket("./python/aoc2024/day22/sample1.txt").sum_of_final_secrets == 37327623
    assert MonkeyMarket("./python/aoc2024/day22/sample2.txt").most_bananas == 23


def test_day22():
    from aoc2024.day22.d22 import MonkeyMarket

    data = f"{input_folder}/aoc2024_day22.txt"

    puzzle = MonkeyMarket(data)

    assert puzzle.sum_of_final_secrets == 21147129593
    assert puzzle.most_bananas == 2445


def test_day23_samples():
    from aoc2024.day23.d23 import LANParty

    assert LANParty("./python/aoc2024/day23/sample1.txt").triple_count_with_t() == 7
    assert LANParty("./python/aoc2024/day23/sample1.txt").password() == "co,de,ka,ta"


def test_day23():
    from aoc2024.day23.d23 import LANParty

    data = f"{input_folder}/aoc2024_day23.txt"

    puzzle = LANParty(data)

    assert puzzle.triple_count_with_t() == 1173
    assert puzzle.password() == "cm,de,ez,gv,hg,iy,or,pw,qu,rs,sn,uc,wq"


def test_day24_samples():
    from aoc2024.day24.d24 import CrossedWires

    assert CrossedWires("./python/aoc2024/day24/sample1.txt").generated_output() == 4
    assert CrossedWires("./python/aoc2024/day24/sample2.txt").generated_output() == 2024


def test_day24():
    from aoc2024.day24.d24 import CrossedWires

    data = f"{input_folder}/aoc2024_day24.txt"

    puzzle = CrossedWires(data)

    assert puzzle.generated_output() == 47666458872582
    assert puzzle.swapped_wires() == "dnt,gdf,gwc,jst,mcm,z05,z15,z30"


def test_day25_samples():
    from aoc2024.day25.d25 import CodeChronicle

    assert CodeChronicle("./python/aoc2024/day25/sample1.txt").count_fit_pairs() == 3


def test_day25():
    from aoc2024.day25.d25 import CodeChronicle

    data = f"{input_folder}/aoc2024_day25.txt"

    puzzle = CodeChronicle(data)

    assert puzzle.count_fit_pairs() == 3116
