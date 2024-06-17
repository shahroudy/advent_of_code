import os

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    from aoc2015.day01.d01 import NotQuiteLisp

    test = NotQuiteLisp("./python/aoc2015/day01/sample1.txt")
    assert test.current_floor == 0
    test = NotQuiteLisp("./python/aoc2015/day01/sample2.txt")
    assert test.current_floor == 3
    test = NotQuiteLisp("./python/aoc2015/day01/sample3.txt")
    assert test.current_floor == -3
    test = NotQuiteLisp("./python/aoc2015/day01/sample4.txt")
    assert test.enter_basement == 1
    test = NotQuiteLisp("./python/aoc2015/day01/sample5.txt")
    assert test.enter_basement == 5


def test_day01():
    from aoc2015.day01.d01 import NotQuiteLisp

    puzzle = NotQuiteLisp(f"{input_folder}/aoc2015_day01.txt")
    assert puzzle.current_floor == 74
    assert puzzle.enter_basement == 1795


def test_day02_samples():
    from aoc2015.day02.d02 import IWasToldThereWouldBeNoMath

    test = IWasToldThereWouldBeNoMath("./python/aoc2015/day02/sample1.txt")
    assert test.total_wrapping_paper() == 58
    assert test.total_ribbon() == 34
    test = IWasToldThereWouldBeNoMath("./python/aoc2015/day02/sample2.txt")
    assert test.total_wrapping_paper() == 43
    assert test.total_ribbon() == 14


def test_day02():
    from aoc2015.day02.d02 import IWasToldThereWouldBeNoMath

    puzzle = IWasToldThereWouldBeNoMath(f"{input_folder}/aoc2015_day02.txt")
    assert puzzle.total_wrapping_paper() == 1606483
    assert puzzle.total_ribbon() == 3842356


def test_day03_samples():
    from aoc2015.day03.d03 import PerfectlySphericalHousesInAVacuum

    test = PerfectlySphericalHousesInAVacuum("./python/aoc2015/day03/sample1.txt")
    assert test.visited_houses_santa_alone() == 2
    test = PerfectlySphericalHousesInAVacuum("./python/aoc2015/day03/sample2.txt")
    assert test.visited_houses_santa_alone() == 4
    assert test.visited_houses_santa_and_robosanta() == 3
    test = PerfectlySphericalHousesInAVacuum("./python/aoc2015/day03/sample3.txt")
    assert test.visited_houses_santa_alone() == 2
    assert test.visited_houses_santa_and_robosanta() == 11
    test = PerfectlySphericalHousesInAVacuum("./python/aoc2015/day03/sample4.txt")
    assert test.visited_houses_santa_and_robosanta() == 3


def test_day03():
    from aoc2015.day03.d03 import PerfectlySphericalHousesInAVacuum

    puzzle = PerfectlySphericalHousesInAVacuum(f"{input_folder}/aoc2015_day03.txt")
    assert puzzle.visited_houses_santa_alone() == 2081
    assert puzzle.visited_houses_santa_and_robosanta() == 2341


def test_day04_samples():
    from aoc2015.day04.d04 import TheIdealStockingStuffer

    test = TheIdealStockingStuffer("./python/aoc2015/day04/sample1.txt")
    assert test.mine() == 609043
    test = TheIdealStockingStuffer("./python/aoc2015/day04/sample2.txt")
    assert test.mine() == 1048970


def test_day04():
    from aoc2015.day04.d04 import TheIdealStockingStuffer

    puzzle = TheIdealStockingStuffer(f"{input_folder}/aoc2015_day04.txt")
    assert puzzle.mine() == 282749
    assert puzzle.mine(zeroes=6) == 9962624


def test_day05_samples():
    from aoc2015.day05.d05 import DoesntHeHaveInternElvesForThis

    test = DoesntHeHaveInternElvesForThis("./python/aoc2015/day05/sample1.txt")
    assert test.nice_a == [True, True, False, False, False]
    test = DoesntHeHaveInternElvesForThis("./python/aoc2015/day05/sample2.txt")
    assert test.nice_b == [True, True, False, False]


def test_day05():
    from aoc2015.day05.d05 import DoesntHeHaveInternElvesForThis

    puzzle = DoesntHeHaveInternElvesForThis(f"{input_folder}/aoc2015_day05.txt")
    assert sum(puzzle.nice_a) == 258
    assert sum(puzzle.nice_b) == 53


def test_day06_samples():
    from aoc2015.day06.d06 import ProbablyAFireHazard

    test = ProbablyAFireHazard("./python/aoc2015/day06/sample1.txt")
    assert test.lit_lights() == 1000000
    test = ProbablyAFireHazard("./python/aoc2015/day06/sample2.txt")
    assert test.lit_lights() == 1000
    test = ProbablyAFireHazard("./python/aoc2015/day06/sample3.txt")
    assert test.lit_lights() == 0
    test = ProbablyAFireHazard("./python/aoc2015/day06/sample4.txt")
    assert test.brightness_sum() == 1
    test = ProbablyAFireHazard("./python/aoc2015/day06/sample5.txt")
    assert test.brightness_sum() == 2000000


def test_day06():
    from aoc2015.day06.d06 import ProbablyAFireHazard

    puzzle = ProbablyAFireHazard(f"{input_folder}/aoc2015_day06.txt")
    assert puzzle.lit_lights() == 543903
    assert puzzle.brightness_sum() == 14687245


def test_day07_samples():
    from aoc2015.day07.d07 import SomeAssemblyRequired

    test = SomeAssemblyRequired("./python/aoc2015/day07/sample1.txt")
    assert test.first_execution() == 65079


def test_day07():
    from aoc2015.day07.d07 import SomeAssemblyRequired

    puzzle = SomeAssemblyRequired(f"{input_folder}/aoc2015_day07.txt")
    assert puzzle.first_execution() == 46065
    assert puzzle.second_execution() == 14134


def test_day08_samples():
    from aoc2015.day08.d08 import Matchsticks

    test = Matchsticks("./python/aoc2015/day08/sample1.txt")
    assert test.extra_chars_from_string_literals() == 12
    assert test.extra_chars_from_encoding() == 19


def test_day08():
    from aoc2015.day08.d08 import Matchsticks

    puzzle = Matchsticks(f"{input_folder}/aoc2015_day08.txt")
    assert puzzle.extra_chars_from_string_literals() == 1333
    assert puzzle.extra_chars_from_encoding() == 2046


def test_day09_samples():
    from aoc2015.day09.d09 import AllInASingleNight

    test = AllInASingleNight("./python/aoc2015/day09/sample1.txt")
    assert test.min_distance == 605
    assert test.max_distance == 982


def test_day09():
    from aoc2015.day09.d09 import AllInASingleNight

    puzzle = AllInASingleNight(f"{input_folder}/aoc2015_day09.txt")
    assert puzzle.min_distance == 117
    assert puzzle.max_distance == 909


def test_day10_samples():
    from aoc2015.day10.d10 import ElvesLookElvesSay

    def test(input):
        return "".join(map(str, ElvesLookElvesSay().look_and_say(input)))

    assert test("1") == "11"
    assert test("11") == "21"
    assert test("21") == "1211"
    assert test("1211") == "111221"
    assert test("111221") == "312211"


def test_day10():
    from aoc2015.day10.d10 import ElvesLookElvesSay

    puzzle = ElvesLookElvesSay(f"{input_folder}/aoc2015_day10.txt")
    assert puzzle.length_of_result(40) == 360154
    assert puzzle.length_of_result(50) == 5103798


def test_day11_samples():
    from aoc2015.day11.d11 import CorporatePolicy

    test = CorporatePolicy(pwd="hijklmmn")
    assert test.has_increasing_straight()
    assert test.has_invalid_letters()

    test = CorporatePolicy(pwd="abbceffg")
    assert test.has_two_pairs()
    assert not test.has_increasing_straight()

    assert not CorporatePolicy(pwd="abbcegjk").has_two_pairs()

    assert CorporatePolicy(pwd="abcdefgh").find_next_valid_password() == "abcdffaa"
    assert CorporatePolicy(pwd="ghijklmn").find_next_valid_password() == "ghjaabcc"


def test_day11():
    from aoc2015.day11.d11 import CorporatePolicy

    puzzle = CorporatePolicy(f"{input_folder}/aoc2015_day11.txt")
    assert puzzle.find_next_valid_password() == "hepxxyzz"
    assert puzzle.find_next_valid_password() == "heqaabcc"


def test_day12_samples():
    from aoc2015.day12.d12 import JSAbacusFrameworkIO

    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample1.txt")
    assert test.sum_all_ints() == 6
    assert test.sum_no_red_ints() == 6
    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample2.txt")
    assert test.sum_all_ints() == 6
    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample3.txt")
    assert test.sum_all_ints() == 3
    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample4.txt")
    assert test.sum_all_ints() == 3
    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample5.txt")
    assert test.sum_all_ints() == 0
    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample6.txt")
    assert test.sum_all_ints() == 0
    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample7.txt")
    assert test.sum_all_ints() == 0
    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample8.txt")
    assert test.sum_all_ints() == 0
    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample9.txt")
    assert test.sum_no_red_ints() == 4
    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample10.txt")
    assert test.sum_no_red_ints() == 0
    test = JSAbacusFrameworkIO("./python/aoc2015/day12/sample11.txt")
    assert test.sum_no_red_ints() == 6


def test_day12():
    from aoc2015.day12.d12 import JSAbacusFrameworkIO

    puzzle = JSAbacusFrameworkIO(f"{input_folder}/aoc2015_day12.txt")
    assert puzzle.sum_all_ints() == 119433
    assert puzzle.sum_no_red_ints() == 68466


def test_day13_samples():
    from aoc2015.day13.d13 import KnightsOfTheDinnerTable

    test = KnightsOfTheDinnerTable("./python/aoc2015/day13/sample1.txt")
    assert test.optimal_happiness() == 330


def test_day13():
    from aoc2015.day13.d13 import KnightsOfTheDinnerTable

    puzzle = KnightsOfTheDinnerTable(f"{input_folder}/aoc2015_day13.txt")
    assert puzzle.optimal_happiness() == 618
    assert puzzle.optimal_happiness_with_me() == 601


def test_day14_samples():
    from aoc2015.day14.d14 import ReindeerOlympics

    test = ReindeerOlympics("./python/aoc2015/day14/sample1.txt")
    assert test.max_distance_of_reindeers_after() == 1120
    assert test.max_score_reindeer_for_all_seconds() == 689


def test_day14():
    from aoc2015.day14.d14 import ReindeerOlympics

    puzzle = ReindeerOlympics(f"{input_folder}/aoc2015_day14.txt")
    assert puzzle.max_distance_of_reindeers_after(2503) == 2696
    assert puzzle.max_score_reindeer_for_all_seconds(2503) == 1084


def test_day15_samples():
    from aoc2015.day15.d15 import ScienceForHungryPeople

    test = ScienceForHungryPeople("./python/aoc2015/day15/sample1.txt")
    assert test.find_highest_score_recipe() == 62842880
    assert test.find_highest_score_recipe(calories_goal=500) == 57600000


def test_day15():
    from aoc2015.day15.d15 import ScienceForHungryPeople

    puzzle = ScienceForHungryPeople(f"{input_folder}/aoc2015_day15.txt")
    assert puzzle.find_highest_score_recipe() == 13882464
    assert puzzle.find_highest_score_recipe(calories_goal=500) == 11171160


def test_day16():
    from aoc2015.day16.d16 import AuntSue

    puzzle = AuntSue(f"{input_folder}/aoc2015_day16.txt")
    assert puzzle.find_aunt_sue_1() == 40
    assert puzzle.find_aunt_sue_2() == 241


def test_day17_samples():
    from aoc2015.day17.d17 import NoSuchThingAsTooMuch

    test = NoSuchThingAsTooMuch("./python/aoc2015/day17/sample1.txt")
    assert test.total_number_of_ways() == 4
    assert test.number_of_ways_with_min_containers() == 3


def test_day17():
    from aoc2015.day17.d17 import NoSuchThingAsTooMuch

    puzzle = NoSuchThingAsTooMuch(f"{input_folder}/aoc2015_day17.txt")
    assert puzzle.total_number_of_ways(150) == 1304
    assert puzzle.number_of_ways_with_min_containers(150) == 18


def test_day18_samples():
    from aoc2015.day18.d18 import LikeAGifForYourYard

    test = LikeAGifForYourYard("./python/aoc2015/day18/sample1.txt")
    assert test.animate_grid(steps=4) == 4
    assert test.animate_grid(steps=5, set_corners=True) == 17


def test_day18():
    from aoc2015.day18.d18 import LikeAGifForYourYard

    puzzle = LikeAGifForYourYard(f"{input_folder}/aoc2015_day18.txt")
    assert puzzle.animate_grid(steps=100) == 768
    assert puzzle.animate_grid(steps=100, set_corners=True) == 781


def test_day19_samples():
    from aoc2015.day19.d19 import MedicineForRudolph

    test = MedicineForRudolph("./python/aoc2015/day19/sample1.txt")
    assert test.distinct_derivable_molecules() == 4
    test = MedicineForRudolph("./python/aoc2015/day19/sample2.txt")
    assert test.distinct_derivable_molecules() == 7
    test = MedicineForRudolph("./python/aoc2015/day19/sample3.txt")
    assert test.min_steps_to_derive_the_medicine() == 3
    test = MedicineForRudolph("./python/aoc2015/day19/sample4.txt")
    assert test.min_steps_to_derive_the_medicine() == 6


def test_day19():
    from aoc2015.day19.d19 import MedicineForRudolph

    puzzle = MedicineForRudolph(f"{input_folder}/aoc2015_day19.txt")
    assert puzzle.distinct_derivable_molecules() == 518
    assert puzzle.min_steps_to_derive_the_medicine() == 200


def test_day20_samples():
    from aoc2015.day20.d20 import InfiniteElvesAndInfiniteHouses

    test = InfiniteElvesAndInfiniteHouses(120)
    assert test.lowest_house_number(deliver=10, infinite=True) == 6
    test = InfiniteElvesAndInfiniteHouses(150)
    assert test.lowest_house_number(deliver=10, infinite=True) == 8
    test = InfiniteElvesAndInfiniteHouses(130)
    assert test.lowest_house_number(deliver=10, infinite=True) == 8


def test_day20():
    from aoc2015.day20.d20 import InfiniteElvesAndInfiniteHouses

    puzzle = InfiniteElvesAndInfiniteHouses(f"{input_folder}/aoc2015_day20.txt")
    assert puzzle.lowest_house_number(deliver=10, infinite=True) == 665280
    assert puzzle.lowest_house_number(deliver=11, infinite=False) == 705600


def test_day21_samples():
    from aoc2015.day21.d21 import RPGSimulator20XX

    test = RPGSimulator20XX()
    assert test.fight(8, 5, 5, 12, 7, 2)


def test_day21():
    from aoc2015.day21.d21 import RPGSimulator20XX

    puzzle = RPGSimulator20XX(f"{input_folder}/aoc2015_day21.txt")
    assert puzzle.min_winning_cost == 91
    assert puzzle.max_losing_cost == 158


def test_day22_samples():
    from aoc2015.day22.d22 import State, WizardSimulator20XX

    test1 = WizardSimulator20XX(initial_state=State(0, 10, 250, 13, 0, 0, 0), boss_damage=8)
    assert test1.search() == 53 + 173
    test2 = WizardSimulator20XX(initial_state=State(0, 10, 250, 14, 0, 0, 0), boss_damage=8)
    assert test2.search() == 229 + 113 + 73 + 173 + 53


def test_day22():
    from aoc2015.day22.d22 import WizardSimulator20XX

    assert WizardSimulator20XX(f"{input_folder}/aoc2015_day22.txt").search() == 953
    assert WizardSimulator20XX(f"{input_folder}/aoc2015_day22.txt", hard_mode=True).search() == 1289
