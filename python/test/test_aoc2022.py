import os

from aoc2022.day01.d01 import CalorieCounting
from aoc2022.day02.d02 import RockPaperScissors
from aoc2022.day03.d03 import RucksackReorganization
from aoc2022.day04.d04 import CampCleanup
from aoc2022.day05.d05 import SupplyStacks
from aoc2022.day06.d06 import TuningTrouble
from aoc2022.day07.d07 import NoSpaceLeftOnDevice
from aoc2022.day08.d08 import TreetopTreeHouse
from aoc2022.day09.d09 import RopeBridge
from aoc2022.day10.d10 import CathodeRayTube
from aoc2022.day11.d11 import MonkeyInTheMiddle
from aoc2022.day12.d12 import HillClimbingAlgorithm
from aoc2022.day13.d13 import DistressSignal
from aoc2022.day14.d14 import RegolithReservoir
from aoc2022.day15.d15 import BeaconExclusionZone

# day16
from aoc2022.day17.d17 import PyroclasticFlow
from aoc2022.day18.d18 import BoilingBoulders

# day 19
from aoc2022.day20.d20 import GrovePositioningSystem
from aoc2022.day21.d21 import MonkeyMath
from aoc2022.day22.d22 import MonkeyMap
from aoc2022.day23.d23 import UnstableDiffusion
from aoc2022.day24.d24 import BlizzardBasin
from aoc2022.day25.d25 import FullOfHotAir

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    test = CalorieCounting("./python/aoc2022/day01/sample1.txt")
    assert test.max_cal_elf() == 24000
    assert test.max_cal_three_elves() == 45000


def test_day01():
    test = CalorieCounting(f"{input_folder}/aoc2022_day01.txt")
    assert test.max_cal_elf() == 69281
    assert test.max_cal_three_elves() == 201524


def test_day02_samples():
    test = RockPaperScissors("./python/aoc2022/day02/sample1.txt")
    assert test.total_score_first_strategy() == 15
    assert test.total_score_second_strategy() == 12


def test_day02():
    test = RockPaperScissors(f"{input_folder}/aoc2022_day02.txt")
    assert test.total_score_first_strategy() == 13526
    assert test.total_score_second_strategy() == 14204


def test_day03_samples():
    test = RucksackReorganization("./python/aoc2022/day03/sample1.txt")
    assert test.sum_of_common_items() == 157
    assert test.sum_of_badges() == 70


def test_day03():
    test = RucksackReorganization(f"{input_folder}/aoc2022_day03.txt")
    assert test.sum_of_common_items() == 8053
    assert test.sum_of_badges() == 2425


def test_day04_samples():
    test = CampCleanup("./python/aoc2022/day04/sample1.txt")
    assert test.sub_super_set_count() == 2
    assert test.overlapping_count() == 4


def test_day04():
    test = CampCleanup(f"{input_folder}/aoc2022_day04.txt")
    assert test.sub_super_set_count() == 459
    assert test.overlapping_count() == 779


def test_day05_samples():
    test = SupplyStacks("./python/aoc2022/day05/sample1.txt")
    assert test.move_one_by_one() == "CMZ"
    assert test.move_them_together() == "MCD"


def test_day05():
    test = SupplyStacks(f"{input_folder}/aoc2022_day05.txt")
    assert test.move_one_by_one() == "TWSGQHNHL"
    assert test.move_them_together() == "JNRSCDWPP"


def test_day06_samples():
    test = TuningTrouble("./python/aoc2022/day06/sample1.txt")
    assert test.char_count(4) == 7
    assert test.char_count(14) == 19


def test_day06():
    test = TuningTrouble(f"{input_folder}/aoc2022_day06.txt")
    assert test.char_count(4) == 1920
    assert test.char_count(14) == 2334


def test_day07_samples():
    test = NoSpaceLeftOnDevice("./python/aoc2022/day07/sample1.txt")
    assert test.sum_of_all_small_dirs() == 95437
    assert test.min_dir_size_to_delete() == 24933642


def test_day07():
    test = NoSpaceLeftOnDevice(f"{input_folder}/aoc2022_day07.txt")
    assert test.sum_of_all_small_dirs() == 1141028
    assert test.min_dir_size_to_delete() == 8278005


def test_day08_samples():
    test = TreetopTreeHouse("./python/aoc2022/day08/sample1.txt")
    assert test.trees_visible_from_outside() == 21
    assert test.highest_scenic_score() == 8


def test_day08():
    test = TreetopTreeHouse(f"{input_folder}/aoc2022_day08.txt")
    assert test.trees_visible_from_outside() == 1546
    assert test.highest_scenic_score() == 519064


def test_day09_samples():
    test = RopeBridge("./python/aoc2022/day09/sample1.txt")
    assert test.pull_the_damn_rope() == 13
    test = RopeBridge("./python/aoc2022/day09/sample2.txt")
    assert test.pull_the_damn_rope(10) == 36


def test_day09():
    test = RopeBridge(f"{input_folder}/aoc2022_day09.txt")
    assert test.pull_the_damn_rope() == 6181
    assert test.pull_the_damn_rope(10) == 2386


def test_day10_samples():
    test = CathodeRayTube("./python/aoc2022/day10/sample1.txt")
    assert test.sum_signal_strengths() == 13140


def test_day10():
    test = CathodeRayTube(f"{input_folder}/aoc2022_day10.txt")
    assert test.sum_signal_strengths() == 11960


def test_day11_samples():
    test = MonkeyInTheMiddle("./python/aoc2022/day11/sample1.txt")
    assert test.monkey_business(relief=True) == 10605
    assert test.monkey_business(relief=False) == 2713310158


def test_day11():
    test = MonkeyInTheMiddle(f"{input_folder}/aoc2022_day11.txt")
    assert test.monkey_business(relief=True) == 58056
    assert test.monkey_business(relief=False) == 15048718170


def test_day12_samples():
    test = HillClimbingAlgorithm("./python/aoc2022/day12/sample1.txt")
    assert test.start_to_E_dist() == 31
    assert test.min_a_to_E_dist() == 29


def test_day12():
    test = HillClimbingAlgorithm(f"{input_folder}/aoc2022_day12.txt")
    assert test.start_to_E_dist() == 339
    assert test.min_a_to_E_dist() == 332


def test_day13_samples():
    test = DistressSignal("./python/aoc2022/day13/sample1.txt")
    assert test.sum_of_right_ordered_signals() == 13
    assert test.decoder_key() == 140


def test_day13():
    test = DistressSignal(f"{input_folder}/aoc2022_day13.txt")
    assert test.sum_of_right_ordered_signals() == 5580
    assert test.decoder_key() == 26200


def test_day14_samples():
    test = RegolithReservoir("./python/aoc2022/day14/sample1.txt")
    assert test.rested_sands(have_floor=False) == 24
    assert test.rested_sands(have_floor=True) == 93


def test_day14():
    test = RegolithReservoir(f"{input_folder}/aoc2022_day14.txt")
    assert test.rested_sands(have_floor=False) == 737
    assert test.rested_sands(have_floor=True) == 28145


def test_day15_samples():
    test = BeaconExclusionZone("./python/aoc2022/day15/sample1.txt")
    assert test.no_beacon_count_in_row() == 26
    assert test.tuning_freq_of_hidden_beacon() == 56000011


def test_day15():
    test = BeaconExclusionZone(f"{input_folder}/aoc2022_day15.txt")
    assert test.no_beacon_count_in_row(2000000) == 4811413
    assert test.tuning_freq_of_hidden_beacon(4000000) == 13171855019123


def test_day17_samples():
    test = PyroclasticFlow("./python/aoc2022/day17/sample1.txt")
    assert test.calc_height_after(2022) == 3068
    assert test.calc_height_after(1000000000000) == 1514285714288


def test_day17():
    test = PyroclasticFlow(f"{input_folder}/aoc2022_day17.txt")
    assert test.calc_height_after(2022) == 3153
    assert test.calc_height_after(1000000000000) == 1553665689155


def test_day18_samples():
    test = BoilingBoulders("./python/aoc2022/day18/sample1.txt")
    assert test.open_sides() == 64
    assert test.reachable_sides() == 58


def test_day18():
    test = BoilingBoulders(f"{input_folder}/aoc2022_day18.txt")
    assert test.open_sides() == 3374
    assert test.reachable_sides() == 2010


def test_day20_samples():
    test = GrovePositioningSystem("./python/aoc2022/day20/sample1.txt")
    assert test.decrypt(simple_decryption=True) == 3
    assert test.decrypt(simple_decryption=False) == 1623178306


def test_day20():
    test = GrovePositioningSystem(f"{input_folder}/aoc2022_day20.txt")
    assert test.decrypt(simple_decryption=True) == 6640
    assert test.decrypt(simple_decryption=False) == 11893839037215


def test_day21_samples():
    test = MonkeyMath("./python/aoc2022/day21/sample1.txt")
    assert test.yell_root() == 152
    assert test.match_root() == 301


def test_day21():
    test = MonkeyMath(f"{input_folder}/aoc2022_day21.txt")
    assert test.yell_root() == 194058098264286
    assert test.match_root() == 3592056845086


def test_day22_samples():
    test = MonkeyMap("./python/aoc2022/day22/sample1.txt")
    assert test.final_password() == 6032


def test_day22():
    test = MonkeyMap(f"{input_folder}/aoc2022_day22.txt")
    assert test.final_password(simple_wrap=True) == 190066
    assert test.final_password(simple_wrap=False) == 134170


def test_day23_samples():
    test = UnstableDiffusion("./python/aoc2022/day23/sample1.txt")
    assert test.spread_the_elves() == (110, 20)


def test_day23():
    test = UnstableDiffusion(f"{input_folder}/aoc2022_day23.txt")
    assert test.spread_the_elves() == (4068, 968)


def test_day24_samples():
    test = BlizzardBasin("./python/aoc2022/day24/sample1.txt")
    assert test.reach_the_goal_with_snacks() == (18, 54)


def test_day24():
    test = BlizzardBasin(f"{input_folder}/aoc2022_day24.txt")
    assert test.reach_the_goal_with_snacks() == (230, 713)


def test_day25_samples():
    test = FullOfHotAir("./python/aoc2022/day25/sample1.txt")
    assert test.sum_of_snafu_numbers() == "2=-1=0"


def test_day25():
    test = FullOfHotAir(f"{input_folder}/aoc2022_day25.txt")
    assert test.sum_of_snafu_numbers() == "2-1-110-=01-1-0-0==2"
