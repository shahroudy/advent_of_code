import os

from aoc2023.day01.d01 import Trebuchet
from aoc2023.day02.d02 import CubeConundrum
from aoc2023.day03.d03 import GearRatios
from aoc2023.day04.d04 import Scratchcards
from aoc2023.day05.d05 import IfYouGiveASeedAFertilizer
from aoc2023.day06.d06 import WaitForIt
from aoc2023.day07.d07 import CamelCards
from aoc2023.day08.d08 import HauntedWasteland
from aoc2023.day09.d09 import MirageMaintenance
from aoc2023.day10.d10 import PipeMaze
from aoc2023.day11.d11 import CosmicExpansion
from aoc2023.day12.d12 import HotSprings

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    test = Trebuchet("./python/aoc2023/day01/sample1.txt")
    assert test.sum_of_first_and_last_digits() == 142
    test = Trebuchet("./python/aoc2023/day01/sample2.txt")
    assert test.sum_of_first_and_last_alphanumeric_digits() == 281


def test_day01():
    test = Trebuchet(f"{input_folder}/aoc2023_day01.txt")
    assert test.sum_of_first_and_last_digits() == 55816
    assert test.sum_of_first_and_last_alphanumeric_digits() == 54980


def test_day02_samples():
    test = CubeConundrum("./python/aoc2023/day02/sample1.txt")
    assert test.sum_of_possible_games() == 8
    assert test.sum_of_power_of_sets() == 2286


def test_day02():
    test = CubeConundrum(f"{input_folder}/aoc2023_day02.txt")
    assert test.sum_of_possible_games() == 2207
    assert test.sum_of_power_of_sets() == 62241


def test_day03_samples():
    test = GearRatios("./python/aoc2023/day03/sample1.txt")
    assert test.sum_of_part_numbers_in_engine_schematic() == 4361
    assert test.sum_of_gear_ratios() == 467835


def test_day03():
    test = GearRatios(f"{input_folder}/aoc2023_day03.txt")
    assert test.sum_of_part_numbers_in_engine_schematic() == 554003
    assert test.sum_of_gear_ratios() == 87263515


def test_day04_samples():
    test = Scratchcards("./python/aoc2023/day04/sample1.txt")
    assert test.sum_of_points() == 13
    assert test.sum_of_card_copies() == 30


def test_day04():
    test = Scratchcards(f"{input_folder}/aoc2023_day04.txt")
    assert test.sum_of_points() == 20407
    assert test.sum_of_card_copies() == 23806951


def test_day05_samples():
    test = IfYouGiveASeedAFertilizer("./python/aoc2023/day05/sample1.txt")
    assert test.min_location_for_input_seeds() == 35
    assert test.min_location_for_input_seed_ranges() == 46


def test_day05():
    test = IfYouGiveASeedAFertilizer(f"{input_folder}/aoc2023_day05.txt")
    assert test.min_location_for_input_seeds() == 196167384
    assert test.min_location_for_input_seed_ranges() == 125742456


def test_day06_samples():
    test = WaitForIt("./python/aoc2023/day06/sample1.txt")
    assert test.ways_to_beat_records() == 288
    assert test.ways_to_beat_the_combined_record() == 71503


def test_day06():
    test = WaitForIt(f"{input_folder}/aoc2023_day06.txt")
    assert test.ways_to_beat_records() == 1710720
    assert test.ways_to_beat_the_combined_record() == 35349468


def test_day07_samples():
    test = CamelCards("./python/aoc2023/day07/sample1.txt")
    assert test.total_winnings() == 6440
    assert test.total_winnings(joker=True) == 5905


def test_day07():
    test = CamelCards(f"{input_folder}/aoc2023_day07.txt")
    assert test.total_winnings() == 251287184
    assert test.total_winnings(joker=True) == 250757288


def test_day08_samples():
    test = HauntedWasteland("./python/aoc2023/day08/sample1.txt")
    assert test.navigate_human() == 2
    test = HauntedWasteland("./python/aoc2023/day08/sample2.txt")
    assert test.navigate_human() == 6
    test = HauntedWasteland("./python/aoc2023/day08/sample3.txt")
    assert test.navigate_ghost() == 6


def test_day08():
    test = HauntedWasteland(f"{input_folder}/aoc2023_day08.txt")
    assert test.navigate_human() == 20569
    assert test.navigate_ghost() == 21366921060721


def test_day09_samples():
    test = MirageMaintenance("./python/aoc2023/day09/sample1.txt")
    assert test.sum_lasts == 114
    assert test.sum_firsts == 2


def test_day09():
    test = MirageMaintenance(f"{input_folder}/aoc2023_day09.txt")
    assert test.sum_lasts == 1974232246
    assert test.sum_firsts == 928


def test_day10_samples():
    test = PipeMaze("./python/aoc2023/day10/sample1.txt")
    assert test.loop_length() == 4
    assert test.count_inner_points() == 1
    test = PipeMaze("./python/aoc2023/day10/sample2.txt")
    assert test.loop_length() == 8
    assert test.count_inner_points() == 1
    test = PipeMaze("./python/aoc2023/day10/sample3.txt")
    assert test.count_inner_points() == 4
    test = PipeMaze("./python/aoc2023/day10/sample4.txt")
    assert test.count_inner_points() == 8
    test = PipeMaze("./python/aoc2023/day10/sample5.txt")
    assert test.count_inner_points() == 10


def test_day10():
    test = PipeMaze(f"{input_folder}/aoc2023_day10.txt")
    assert test.loop_length() == 6725
    assert test.count_inner_points() == 383


def test_day11_samples():
    test = CosmicExpansion("./python/aoc2023/day11/sample1.txt")
    assert test.sum_distance_between_expanded_galaxies(2) == 374
    assert test.sum_distance_between_expanded_galaxies(10) == 1030
    assert test.sum_distance_between_expanded_galaxies(100) == 8410


def test_day11():
    test = CosmicExpansion(f"{input_folder}/aoc2023_day11.txt")
    assert test.sum_distance_between_expanded_galaxies() == 9214785
    assert test.sum_distance_between_expanded_galaxies(1000000) == 613686987427


def test_day12_samples():
    test = HotSprings("./python/aoc2023/day12/sample1.txt")
    assert test.sum_of_different_arrangements() == 1
    assert test.sum_of_different_arrangements(rep=5) == 1
    test = HotSprings("./python/aoc2023/day12/sample2.txt")
    assert test.sum_of_different_arrangements() == 4
    assert test.sum_of_different_arrangements(rep=5) == 16384
    test = HotSprings("./python/aoc2023/day12/sample3.txt")
    assert test.sum_of_different_arrangements() == 1
    assert test.sum_of_different_arrangements(rep=5) == 1
    test = HotSprings("./python/aoc2023/day12/sample4.txt")
    assert test.sum_of_different_arrangements() == 1
    assert test.sum_of_different_arrangements(rep=5) == 16
    test = HotSprings("./python/aoc2023/day12/sample5.txt")
    assert test.sum_of_different_arrangements() == 4
    assert test.sum_of_different_arrangements(rep=5) == 2500
    test = HotSprings("./python/aoc2023/day12/sample6.txt")
    assert test.sum_of_different_arrangements() == 10
    assert test.sum_of_different_arrangements(rep=5) == 506250


def test_day12():
    test = HotSprings(f"{input_folder}/aoc2023_day12.txt")
    assert test.sum_of_different_arrangements() == 7350
    assert test.sum_of_different_arrangements(rep=5) == 200097286528151
