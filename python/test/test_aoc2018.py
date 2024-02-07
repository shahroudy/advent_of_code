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
