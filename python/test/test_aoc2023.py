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
from aoc2023.day13.d13 import PointOfIncidence
from aoc2023.day14.d14 import ParabolicReflectorDish
from aoc2023.day15.d15 import LensLibrary
from aoc2023.day16.d16 import TheFloorWillBeLava
from aoc2023.day17.d17 import ClumsyCrucible
from aoc2023.day18.d18 import LavaductLagoon
from aoc2023.day19.d19 import Aplenty
from aoc2023.day20.d20 import PulsePropagation
from aoc2023.day21.d21 import StepCounter

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


def test_day13_samples():
    test = PointOfIncidence("./python/aoc2023/day13/sample1.txt")
    assert test.sum_of_reflections() == 405
    assert test.sum_of_reflections(smudge_count=1) == 400


def test_day13():
    test = PointOfIncidence(f"{input_folder}/aoc2023_day13.txt")
    assert test.sum_of_reflections() == 36448
    assert test.sum_of_reflections(smudge_count=1) == 35799


def test_day14_samples():
    test = ParabolicReflectorDish("./python/aoc2023/day14/sample1.txt")
    assert test.load_after_single_tilt() == 136
    assert test.load_after_a_billion_cycles() == 64


def test_day14():
    test = ParabolicReflectorDish(f"{input_folder}/aoc2023_day14.txt")
    assert test.load_after_single_tilt() == 109661
    assert test.load_after_a_billion_cycles() == 90176


def test_day15_samples():
    test = LensLibrary("./python/aoc2023/day15/sample1.txt")
    assert test.input_hash() == 52
    test = LensLibrary("./python/aoc2023/day15/sample2.txt")
    assert test.input_hash() == 1320
    assert test.focusing_power_after_HASHMAP_lens_configuration() == 145


def test_day15():
    test = LensLibrary(f"{input_folder}/aoc2023_day15.txt")
    assert test.input_hash() == 519603
    assert test.focusing_power_after_HASHMAP_lens_configuration() == 244342


def test_day16_samples():
    test = TheFloorWillBeLava("./python/aoc2023/day16/sample1.txt")
    assert test.top_left_beam_energized_count() == 46
    assert test.max_beam_energized_count() == 51


def test_day16():
    test = TheFloorWillBeLava(f"{input_folder}/aoc2023_day16.txt")
    assert test.top_left_beam_energized_count() == 8034
    assert test.max_beam_energized_count() == 8225


def test_day17_samples():
    test = ClumsyCrucible("./python/aoc2023/day17/sample1.txt")
    assert test.minimum_heat_loss() == 102
    assert test.minimum_heat_loss(4, 10) == 94
    test = ClumsyCrucible("./python/aoc2023/day17/sample2.txt")
    assert test.minimum_heat_loss(4, 10) == 71


def test_day17():
    test = ClumsyCrucible(f"{input_folder}/aoc2023_day17.txt")
    assert test.minimum_heat_loss() == 797
    assert test.minimum_heat_loss(4, 10) == 914


def test_day18_samples():
    test = LavaductLagoon("./python/aoc2023/day18/sample1.txt")
    assert test.digged_area() == 62
    assert test.digged_area(swapped=True) == 952408144115


def test_day18():
    test = LavaductLagoon(f"{input_folder}/aoc2023_day18.txt")
    assert test.digged_area() == 70026
    assert test.digged_area(swapped=True) == 68548301037382


def test_day19_samples():
    test = Aplenty("./python/aoc2023/day19/sample1.txt")
    assert test.sum_rating_accepted_parts() == 19114
    assert test.count_accepted_distinct_combinations() == 167409079868000


def test_day19():
    test = Aplenty(f"{input_folder}/aoc2023_day19.txt")
    assert test.sum_rating_accepted_parts() == 350678
    assert test.count_accepted_distinct_combinations() == 124831893423809


def test_day20_samples():
    test = PulsePropagation("./python/aoc2023/day20/sample1.txt")
    assert test.lmh == 32000000
    test = PulsePropagation("./python/aoc2023/day20/sample2.txt")
    assert test.lmh == 11687500


def test_day20():
    test = PulsePropagation(f"{input_folder}/aoc2023_day20.txt")
    assert test.lmh == 949764474
    assert test.rx_activated == 243221023462303


def test_day21_samples():
    test = StepCounter("./python/aoc2023/day21/sample1.txt")
    assert test.simple_garden_plots_count(steps=6) == 16


def test_day21():
    test = StepCounter(f"{input_folder}/aoc2023_day21.txt")
    assert test.simple_garden_plots_count(steps=64) == 3770
    assert test.garden_plots_in_indefinite_map(iterations=26501365) == 628206330073385
