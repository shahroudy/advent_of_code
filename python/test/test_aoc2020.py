import os

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    from aoc2020.day01.d01 import ReportRepair

    test = ReportRepair("./python/aoc2020/day01/sample1.txt")
    assert test.multiplication_of_two() == 514579
    assert test.multiplication_of_three() == 241861950


def test_day01():
    from aoc2020.day01.d01 import ReportRepair

    test = ReportRepair(f"{input_folder}/aoc2020_day01.txt")
    assert test.multiplication_of_two() == 494475
    assert test.multiplication_of_three() == 267520550


def test_day02_samples():
    from aoc2020.day02.d02 import PasswordPhilosophy

    test = PasswordPhilosophy("./python/aoc2020/day02/sample1.txt")
    assert test.valid_passwords_count() == 2
    assert test.valid_passwords_position() == 1


def test_day02():
    from aoc2020.day02.d02 import PasswordPhilosophy

    test = PasswordPhilosophy(f"{input_folder}/aoc2020_day02.txt")
    assert test.valid_passwords_count() == 398
    assert test.valid_passwords_position() == 562


def test_day03_samples():
    from aoc2020.day03.d03 import TobogganTrajectory

    test = TobogganTrajectory("./python/aoc2020/day03/sample1.txt")
    assert test.tree_count() == 7
    assert test.multiplication_of_tree_counts_for_all_slopes() == 336


def test_day03():
    from aoc2020.day03.d03 import TobogganTrajectory

    test = TobogganTrajectory(f"{input_folder}/aoc2020_day03.txt")
    assert test.tree_count() == 211
    assert test.multiplication_of_tree_counts_for_all_slopes() == 3584591857


def test_day04_samples():
    from aoc2020.day04.d04 import PassportProcessing

    test = PassportProcessing("./python/aoc2020/day04/sample1.txt")
    assert test.passports_with_required_fields() == 2
    test = PassportProcessing("./python/aoc2020/day04/sample2.txt")
    assert test.fully_valid_passports() == 0
    test = PassportProcessing("./python/aoc2020/day04/sample3.txt")
    assert test.fully_valid_passports() == 4


def test_day04():
    from aoc2020.day04.d04 import PassportProcessing

    test = PassportProcessing(f"{input_folder}/aoc2020_day04.txt")
    assert test.passports_with_required_fields() == 192
    assert test.fully_valid_passports() == 101


def test_day05_samples():
    from aoc2020.day05.d05 import BinaryBoarding

    test = BinaryBoarding("./python/aoc2020/day05/sample1.txt")
    assert test.maximum_seat_id() == 357
    test = BinaryBoarding("./python/aoc2020/day05/sample2.txt")
    assert test.maximum_seat_id() == 820


def test_day05():
    from aoc2020.day05.d05 import BinaryBoarding

    test = BinaryBoarding(f"{input_folder}/aoc2020_day05.txt")
    assert test.maximum_seat_id() == 991
    assert test.id_of_my_seat() == 534


def test_day06_samples():
    from aoc2020.day06.d06 import CustomCustoms

    test = CustomCustoms("./python/aoc2020/day06/sample1.txt")
    assert test.count_anyone_answered() == 11
    assert test.count_everyone_answered() == 6


def test_day06():
    from aoc2020.day06.d06 import CustomCustoms

    test = CustomCustoms(f"{input_folder}/aoc2020_day06.txt")
    assert test.count_anyone_answered() == 6911
    assert test.count_everyone_answered() == 3473


def test_day07_samples():
    from aoc2020.day07.d07 import HandyHaversacks

    test = HandyHaversacks("./python/aoc2020/day07/sample1.txt")
    assert test.bag_colors_containing_shiny_gold() == 4
    assert test.number_of_bags_inside_a_shiny_gold() == 32
    test = HandyHaversacks("./python/aoc2020/day07/sample2.txt")
    assert test.number_of_bags_inside_a_shiny_gold() == 126


def test_day07():
    from aoc2020.day07.d07 import HandyHaversacks

    test = HandyHaversacks(f"{input_folder}/aoc2020_day07.txt")
    assert test.bag_colors_containing_shiny_gold() == 372
    assert test.number_of_bags_inside_a_shiny_gold() == 8015


def test_day08_samples():
    from aoc2020.day08.d08 import HandheldHalting

    test = HandheldHalting("./python/aoc2020/day08/sample1.txt")
    assert test.acc_value_before_looping() == 5
    assert test.acc_value_after_proper_termination() == 8


def test_day08():
    from aoc2020.day08.d08 import HandheldHalting

    test = HandheldHalting(f"{input_folder}/aoc2020_day08.txt")
    assert test.acc_value_before_looping() == 1930
    assert test.acc_value_after_proper_termination() == 1688


def test_day09_samples():
    from aoc2020.day09.d09 import EncodingError

    test = EncodingError("./python/aoc2020/day09/sample1.txt", 5)
    assert test.first_invalid == 127
    assert test.encryption_weakness() == 62


def test_day09():
    from aoc2020.day09.d09 import EncodingError

    test = EncodingError(f"{input_folder}/aoc2020_day09.txt")
    assert test.first_invalid == 400480901
    assert test.encryption_weakness() == 67587168


def test_day10_samples():
    from aoc2020.day10.d10 import AdapterArray

    test = AdapterArray("./python/aoc2020/day10/sample1.txt")
    assert test.difference_count_multiplications() == 35
    assert test.count_all_possible_ways() == 8
    test = AdapterArray("./python/aoc2020/day10/sample2.txt")
    assert test.difference_count_multiplications() == 220
    assert test.count_all_possible_ways() == 19208


def test_day10():
    from aoc2020.day10.d10 import AdapterArray

    test = AdapterArray(f"{input_folder}/aoc2020_day10.txt")
    assert test.difference_count_multiplications() == 2100
    assert test.count_all_possible_ways() == 16198260678656


def test_day11_samples():
    from aoc2020.day11.d11 import SeatingSystem

    test = SeatingSystem("./python/aoc2020/day11/sample1.txt")
    assert test.occupied_seats_after_equilibrium(False) == 37
    assert test.occupied_seats_after_equilibrium(True) == 26


def test_day11():
    from aoc2020.day11.d11 import SeatingSystem

    test = SeatingSystem(f"{input_folder}/aoc2020_day11.txt")
    assert test.occupied_seats_after_equilibrium(False) == 2283
    assert test.occupied_seats_after_equilibrium(True) == 2054


def test_day12_samples():
    from aoc2020.day12.d12 import RainRisk

    test = RainRisk("./python/aoc2020/day12/sample1.txt")
    assert test.move_ship() == 25
    assert test.move_ship_with_waypoint() == 286


def test_day12():
    from aoc2020.day12.d12 import RainRisk

    test = RainRisk(f"{input_folder}/aoc2020_day12.txt")
    assert test.move_ship() == 521
    assert test.move_ship_with_waypoint() == 22848


def test_day13_samples():
    from aoc2020.day13.d13 import ShuttleSearch

    assert ShuttleSearch("./python/aoc2020/day13/sample1.txt").earliest_bus() == 295
    assert ShuttleSearch("./python/aoc2020/day13/sample1.txt").earliest_match_time() == 1068781
    assert ShuttleSearch("./python/aoc2020/day13/sample2.txt").earliest_match_time() == 3417
    assert ShuttleSearch("./python/aoc2020/day13/sample3.txt").earliest_match_time() == 754018
    assert ShuttleSearch("./python/aoc2020/day13/sample4.txt").earliest_match_time() == 779210
    assert ShuttleSearch("./python/aoc2020/day13/sample5.txt").earliest_match_time() == 1261476
    assert ShuttleSearch("./python/aoc2020/day13/sample6.txt").earliest_match_time() == 1202161486


def test_day13():
    from aoc2020.day13.d13 import ShuttleSearch

    test = ShuttleSearch(f"{input_folder}/aoc2020_day13.txt")
    assert test.earliest_bus() == 261
    assert test.earliest_match_time() == 807435693182510


def test_day14_samples():
    from aoc2020.day14.d14 import DockingData
    from aoc2020.day14.d14_str import DockingData as DockingDataStr

    assert DockingData("./python/aoc2020/day14/sample1.txt").sum_after_value_decode() == 165
    assert DockingData("./python/aoc2020/day14/sample2.txt").sum_after_address_decode() == 208

    assert DockingDataStr("./python/aoc2020/day14/sample1.txt").sum_after_value_decode() == 165
    assert DockingDataStr("./python/aoc2020/day14/sample2.txt").sum_after_address_decode() == 208


def test_day14():
    from aoc2020.day14.d14 import DockingData
    from aoc2020.day14.d14_str import DockingData as DockingDataStr

    test = DockingData(f"{input_folder}/aoc2020_day14.txt")
    assert test.sum_after_value_decode() == 11501064782628
    assert test.sum_after_address_decode() == 5142195937660
    test = DockingDataStr(f"{input_folder}/aoc2020_day14.txt")
    assert test.sum_after_value_decode() == 11501064782628
    assert test.sum_after_address_decode() == 5142195937660


def test_day15_samples():
    from aoc2020.day15.d15 import RambunctiousRecitation

    test = RambunctiousRecitation("./python/aoc2020/day15/sample1.txt")
    assert test.whats_nth_spoken_number(2020) == 436
    assert test.whats_nth_spoken_number(30000000) == 175594
    test = RambunctiousRecitation("./python/aoc2020/day15/sample2.txt")
    assert test.whats_nth_spoken_number(2020) == 1
    assert test.whats_nth_spoken_number(30000000) == 2578
    test = RambunctiousRecitation("./python/aoc2020/day15/sample3.txt")
    assert test.whats_nth_spoken_number(2020) == 10
    assert test.whats_nth_spoken_number(30000000) == 3544142
    test = RambunctiousRecitation("./python/aoc2020/day15/sample4.txt")
    assert test.whats_nth_spoken_number(2020) == 27
    assert test.whats_nth_spoken_number(30000000) == 261214
    test = RambunctiousRecitation("./python/aoc2020/day15/sample5.txt")
    assert test.whats_nth_spoken_number(2020) == 78
    assert test.whats_nth_spoken_number(30000000) == 6895259
    test = RambunctiousRecitation("./python/aoc2020/day15/sample6.txt")
    assert test.whats_nth_spoken_number(2020) == 438
    assert test.whats_nth_spoken_number(30000000) == 18
    test = RambunctiousRecitation("./python/aoc2020/day15/sample7.txt")
    assert test.whats_nth_spoken_number(2020) == 1836
    assert test.whats_nth_spoken_number(30000000) == 362


def test_day15():
    from aoc2020.day15.d15 import RambunctiousRecitation

    test = RambunctiousRecitation(f"{input_folder}/aoc2020_day15.txt")
    assert test.whats_nth_spoken_number(2020) == 1325
    assert test.whats_nth_spoken_number(30000000) == 59006


def test_day16_samples():
    from aoc2020.day16.d16 import TicketTranslation

    test = TicketTranslation("./python/aoc2020/day16/sample1.txt")
    assert test.ticket_scanning_error_rate == 71


def test_day16():
    from aoc2020.day16.d16 import TicketTranslation

    test = TicketTranslation(f"{input_folder}/aoc2020_day16.txt")
    assert test.ticket_scanning_error_rate == 23009
    assert test.departure == 10458887314153


def test_day17_samples():
    from aoc2020.day17.d17 import ConwayCubes

    assert ConwayCubes("./python/aoc2020/day17/sample1.txt").calculate_active_cubes_in_3D() == 112
    assert ConwayCubes("./python/aoc2020/day17/sample1.txt").calculate_active_cubes_in_4D() == 848


def test_day17():
    from aoc2020.day17.d17 import ConwayCubes

    test = ConwayCubes(f"{input_folder}/aoc2020_day17.txt")
    assert test.calculate_active_cubes_in_3D() == 448
    assert test.calculate_active_cubes_in_4D() == 2400


def test_day18_samples():
    from aoc2020.day18.d18 import OperationOrder

    assert OperationOrder("./python/aoc2020/day18/sample1.txt").homework() == 71
    assert OperationOrder("./python/aoc2020/day18/sample1.txt").homework_advanced() == 231
    assert OperationOrder("./python/aoc2020/day18/sample2.txt").homework() == 26
    assert OperationOrder("./python/aoc2020/day18/sample2.txt").homework_advanced() == 46
    assert OperationOrder("./python/aoc2020/day18/sample3.txt").homework() == 437
    assert OperationOrder("./python/aoc2020/day18/sample3.txt").homework_advanced() == 1445
    assert OperationOrder("./python/aoc2020/day18/sample4.txt").homework() == 12240
    assert OperationOrder("./python/aoc2020/day18/sample4.txt").homework_advanced() == 669060
    assert OperationOrder("./python/aoc2020/day18/sample5.txt").homework() == 13632
    assert OperationOrder("./python/aoc2020/day18/sample5.txt").homework_advanced() == 23340


def test_day18():
    from aoc2020.day18.d18 import OperationOrder

    test = OperationOrder(f"{input_folder}/aoc2020_day18.txt")
    assert test.homework() == 650217205854
    assert test.homework_advanced() == 20394514442037


def test_day19_samples():
    from aoc2020.day19.d19 import MonsterMessages

    assert MonsterMessages("./python/aoc2020/day19/sample1.txt").count_matching_simple() == 2
    assert MonsterMessages("./python/aoc2020/day19/sample2.txt").count_matching_simple() == 3
    assert MonsterMessages("./python/aoc2020/day19/sample2.txt").count_matching_looped() == 12

    from aoc2020.day19.d19_lark import MonsterMessages as MonsterMessagesLark

    assert MonsterMessagesLark("./python/aoc2020/day19/sample1.txt").count_matching_simple() == 2
    assert MonsterMessagesLark("./python/aoc2020/day19/sample2.txt").count_matching_simple() == 3
    assert MonsterMessagesLark("./python/aoc2020/day19/sample2.txt").count_matching_looped() == 12


def test_day19():
    from aoc2020.day19.d19 import MonsterMessages

    test = MonsterMessages(f"{input_folder}/aoc2020_day19.txt")
    assert test.count_matching_simple() == 142
    assert test.count_matching_looped() == 294

    from aoc2020.day19.d19_lark import MonsterMessages as MonsterMessagesLark

    test = MonsterMessagesLark(f"{input_folder}/aoc2020_day19.txt")
    assert test.count_matching_simple() == 142
    assert test.count_matching_looped() == 294


def test_day20_samples():
    from aoc2020.day20.d20 import JurassicJigsaw

    test = JurassicJigsaw("./python/aoc2020/day20/sample1.txt")
    assert test.find_corner_ids() == 20899048083289
    assert test.habitats_water_roughness() == 273


def test_day20():
    from aoc2020.day20.d20 import JurassicJigsaw

    test = JurassicJigsaw(f"{input_folder}/aoc2020_day20.txt")
    assert test.find_corner_ids() == 7901522557967
    assert test.habitats_water_roughness() == 2476


def test_day21_samples():
    from aoc2020.day21.d21 import AllergenAssessment

    test = AllergenAssessment("./python/aoc2020/day21/sample1.txt")
    assert test.no_allergen_ingredient_count() == 5
    assert test.canonical_dangerous_ingredient_list() == "mxmxvkd,sqjhc,fvjkl"


def test_day21():
    from aoc2020.day21.d21 import AllergenAssessment

    test = AllergenAssessment(f"{input_folder}/aoc2020_day21.txt")
    assert test.no_allergen_ingredient_count() == 2098
    assert (
        test.canonical_dangerous_ingredient_list()
        == "ppdplc,gkcplx,ktlh,msfmt,dqsbql,mvqkdj,ggsz,hbhsx"
    )


def test_day22_samples():
    from aoc2020.day22.d22 import CrabCombat

    test = CrabCombat("./python/aoc2020/day22/sample1.txt")
    assert test.result_of_combat() == 306
    assert test.result_of_combat(recursive=True) == 291


def test_day22():
    from aoc2020.day22.d22 import CrabCombat

    test = CrabCombat(f"{input_folder}/aoc2020_day22.txt")
    assert test.result_of_combat() == 35013
    assert test.result_of_combat(recursive=True) == 32806


def test_day23_samples():
    from aoc2020.day23.d23 import CrabCups

    test = CrabCups("./python/aoc2020/day23/sample1.txt")
    assert test.crab_mix_simple(10) == 92658374
    assert test.crab_mix_simple() == 67384529
    assert test.crab_mix_many() == 149245887792


def test_day23():
    from aoc2020.day23.d23 import CrabCups

    test = CrabCups(f"{input_folder}/aoc2020_day23.txt")
    assert test.crab_mix_simple() == 49576328
    assert test.crab_mix_many() == 511780369955
