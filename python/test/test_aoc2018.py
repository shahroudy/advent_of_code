import os

from aoc2018.day13.d13 import MineCartMadness
from aoc2018.day14.d14 import ChocolateCharts
from aoc2018.day15.d15 import BeverageBandits
from aoc2018.day16.d16 import ChronalClassification
from aoc2018.day17.d17 import ReservoirResearch
from aoc2018.day18.d18 import SettlersOfTheNorthPole

input_folder = os.environ.get("aoc_inputs")


def test_day13_samples():
    test = MineCartMadness("./python/aoc2018/day13/sample1.txt")
    assert test.first_crash == (7, 3)
    test = MineCartMadness("./python/aoc2018/day13/sample2.txt")
    assert test.last_cart == (6, 4)


def test_day13():
    test = MineCartMadness(f"{input_folder}/aoc2018_day13.txt")
    assert test.first_crash == (58, 93)
    assert test.last_cart == (91, 72)


def test_day14_samples():
    test = ChocolateCharts()
    assert test.calc1(9) == "5158916779"
    assert test.calc1(5) == "0124515891"
    assert test.calc1(18) == "9251071085"
    assert test.calc1(2018) == "5941429882"
    assert test.calc2("51589") == 9
    assert test.calc2("01245") == 5
    assert test.calc2("92510") == 18
    assert test.calc2("59414") == 2018


def test_day14():
    puzzle = ChocolateCharts()
    assert puzzle.calc1(165061) == "5992684592"
    assert puzzle.calc2("165061") == 20181148


def test_day15_samples():
    test = BeverageBandits("./python/aoc2018/day15/sample1.txt")
    assert test.run_battle() == 27730
    assert test.run_flawless_battle_with_minimum_attack_power() == 4988
    test = BeverageBandits("./python/aoc2018/day15/sample2.txt")
    assert test.run_battle() == 36334
    test = BeverageBandits("./python/aoc2018/day15/sample3.txt")
    assert test.run_battle() == 39514
    assert test.run_flawless_battle_with_minimum_attack_power() == 31284
    test = BeverageBandits("./python/aoc2018/day15/sample4.txt")
    assert test.run_battle() == 27755
    assert test.run_flawless_battle_with_minimum_attack_power() == 3478
    test = BeverageBandits("./python/aoc2018/day15/sample5.txt")
    assert test.run_battle() == 28944
    assert test.run_flawless_battle_with_minimum_attack_power() == 6474
    test = BeverageBandits("./python/aoc2018/day15/sample6.txt")
    assert test.run_battle() == 18740
    assert test.run_flawless_battle_with_minimum_attack_power() == 1140


def test_day15():
    puzzle = BeverageBandits(f"{input_folder}/aoc2018_day15.txt")
    assert puzzle.run_battle() == 228730
    assert puzzle.run_flawless_battle_with_minimum_attack_power() == 33621


def test_day16():
    puzzle = ChronalClassification(f"{input_folder}/aoc2018_day16.txt")
    assert puzzle.find_matches() == 500
    assert puzzle.run_opcode_program() == 533


def test_day17_samples():
    test = ReservoirResearch("./python/aoc2018/day17/sample1.txt")
    assert test.water_reached_count() == 57
    assert test.remaining_water_count() == 29
    test = ReservoirResearch("./python/aoc2018/day17/sample2.txt")
    assert test.water_reached_count() == 96
    assert test.remaining_water_count() == 65


def test_day17():
    puzzle = ReservoirResearch(f"{input_folder}/aoc2018_day17.txt")
    assert puzzle.water_reached_count() == 34541
    assert puzzle.remaining_water_count() == 28000


def test_day18_samples():
    test = SettlersOfTheNorthPole("./python/aoc2018/day18/sample1.txt")
    assert test.simulate() == 1147


def test_day18():
    puzzle = SettlersOfTheNorthPole(f"{input_folder}/aoc2018_day18.txt")
    assert puzzle.simulate() == 531417
    assert puzzle.simulate(minutes=1000000000) == 205296


def test_day19_samples():
    from aoc2018.day19.d19 import GoWithTheFlow

    test = GoWithTheFlow("./python/aoc2018/day19/sample1.txt")
    assert test.run_background_process() == 6


def test_day19():
    from aoc2018.day19.d19 import GoWithTheFlow

    puzzle = GoWithTheFlow(f"{input_folder}/aoc2018_day19.txt")
    assert puzzle.run_background_process() == 2072
    assert puzzle.set_reg_0_and_run_background_process() == 27578880


def test_day20_samples():
    from aoc2018.day20.d20 import ARegularMap

    assert ARegularMap("./python/aoc2018/day20/sample1.txt").calc1 == 3
    assert ARegularMap("./python/aoc2018/day20/sample2.txt").calc1 == 10
    assert ARegularMap("./python/aoc2018/day20/sample3.txt").calc1 == 18
    assert ARegularMap("./python/aoc2018/day20/sample4.txt").calc1 == 23
    assert ARegularMap("./python/aoc2018/day20/sample5.txt").calc1 == 31


def test_day20():
    from aoc2018.day20.d20 import ARegularMap

    puzzle = ARegularMap(f"{input_folder}/aoc2018_day20.txt")
    assert puzzle.calc1 == 4025
    assert puzzle.calc2 == 8186


def test_day21_samples():
    from aoc2018.day21.d21 import ChronalConversion

    test = ChronalConversion("./python/aoc2018/day21/sample1.txt")
    assert test.register_0_value_for_fewest_instructions_executed_before_halt() == 6


def test_day21():
    from aoc2018.day21.d21 import ChronalConversion

    puzzle = ChronalConversion(f"{input_folder}/aoc2018_day21.txt")
    assert puzzle.register_0_value_for_fewest_instructions_executed_before_halt() == 7224964
    assert puzzle.register_0_value_for_maximum_instructions_executed_before_halt() == 13813247


def test_day22_samples():
    from aoc2018.day22.d22 import ModeMaze

    assert ModeMaze("./python/aoc2018/day22/sample1.txt").total_risk_level() == 114
    assert ModeMaze("./python/aoc2018/day22/sample1.txt").fastest_way_to_reach_the_target() == 45


def test_day22_dijkstra_samples():
    from aoc2018.day22.d22_dijkstra import ModeMaze

    assert ModeMaze("./python/aoc2018/day22/sample1.txt").total_risk_level() == 114
    assert ModeMaze("./python/aoc2018/day22/sample1.txt").fastest_way_to_reach_the_target() == 45


def test_day22():
    from aoc2018.day22.d22 import ModeMaze

    puzzle = ModeMaze(f"{input_folder}/aoc2018_day22.txt")

    assert puzzle.total_risk_level() == 11843
    assert puzzle.fastest_way_to_reach_the_target() == 1078


def test_day22_dijkstra():
    from aoc2018.day22.d22_dijkstra import ModeMaze as ModeMazeDijkstra

    puzzle = ModeMazeDijkstra(f"{input_folder}/aoc2018_day22.txt")

    assert puzzle.total_risk_level() == 11843
    assert puzzle.fastest_way_to_reach_the_target() == 1078
