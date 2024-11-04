import os

input_folder = os.environ.get("aoc_inputs")


def test_day01_samples():
    from aoc2017.day01.d01 import InverseCaptcha

    test = InverseCaptcha("./python/aoc2017/day01/sample1.txt")
    assert test.solve_with_next_item() == 3
    test = InverseCaptcha("./python/aoc2017/day01/sample2.txt")
    assert test.solve_with_next_item() == 4
    test = InverseCaptcha("./python/aoc2017/day01/sample3.txt")
    assert test.solve_with_halfway_around() == 0
    test = InverseCaptcha("./python/aoc2017/day01/sample4.txt")
    assert test.solve_with_halfway_around() == 4
    test = InverseCaptcha("./python/aoc2017/day01/sample5.txt")
    assert test.solve_with_halfway_around() == 12
    test = InverseCaptcha("./python/aoc2017/day01/sample6.txt")
    assert test.solve_with_halfway_around() == 4


def test_day01():
    from aoc2017.day01.d01 import InverseCaptcha

    input_file = f"{input_folder}/aoc2017_day01.txt"
    puzzle = InverseCaptcha(input_file)
    assert puzzle.solve_with_next_item() == 1089
    assert puzzle.solve_with_halfway_around() == 1156


def test_day02_samples():
    from aoc2017.day02.d02 import CorruptionChecksum

    test = CorruptionChecksum("./python/aoc2017/day02/sample1.txt")
    assert test.max_min_checksum() == 18
    test = CorruptionChecksum("./python/aoc2017/day02/sample2.txt")
    assert test.divisible_checksum() == 9


def test_day02():
    from aoc2017.day02.d02 import CorruptionChecksum

    input_file = f"{input_folder}/aoc2017_day02.txt"
    puzzle = CorruptionChecksum(input_file)
    assert puzzle.max_min_checksum() == 41887
    assert puzzle.divisible_checksum() == 226


def test_day03_samples():
    from aoc2017.day03.d03 import SpiralMemory

    test = SpiralMemory(12)
    assert test.simple_spiral() == 3
    test = SpiralMemory(23)
    assert test.simple_spiral() == 2
    test = SpiralMemory(1024)
    assert test.simple_spiral() == 31


def test_day03():
    from aoc2017.day03.d03 import SpiralMemory

    input_file = f"{input_folder}/aoc2017_day03.txt"
    puzzle = SpiralMemory(input_file)
    assert puzzle.simple_spiral() == 552
    assert puzzle.summation_spiral() == 330785


def test_day04_samples():
    from aoc2017.day04.d04 import HighEntropyPassphrases

    test = HighEntropyPassphrases("./python/aoc2017/day04/sample1.txt")
    assert test.number_of_simple_valid_passphrases() == 2
    test = HighEntropyPassphrases("./python/aoc2017/day04/sample2.txt")
    assert test.number_of_valid_passphrases_with_no_rearranging() == 3


def test_day04():
    from aoc2017.day04.d04 import HighEntropyPassphrases

    input_file = f"{input_folder}/aoc2017_day04.txt"
    puzzle = HighEntropyPassphrases(input_file)
    assert puzzle.number_of_simple_valid_passphrases() == 325
    assert puzzle.number_of_valid_passphrases_with_no_rearranging() == 119


def test_day05_samples():
    from aoc2017.day05.d05 import AMazeofTwistyTrampolinesAllAlike

    test = AMazeofTwistyTrampolinesAllAlike("./python/aoc2017/day05/sample1.txt")
    assert test.simple_jumps() == 5
    assert test.strange_jumps() == 10


def test_day05():
    from aoc2017.day05.d05 import AMazeofTwistyTrampolinesAllAlike

    input_file = f"{input_folder}/aoc2017_day05.txt"
    puzzle = AMazeofTwistyTrampolinesAllAlike(input_file)
    assert puzzle.simple_jumps() == 355965
    assert puzzle.strange_jumps() == 26948068


def test_day06_samples():
    from aoc2017.day06.d06 import MemoryReallocation

    test = MemoryReallocation("./python/aoc2017/day06/sample1.txt")
    assert test.cycle_count() == 5
    assert test.cycles_from_last_occurrence() == 4


def test_day06():
    from aoc2017.day06.d06 import MemoryReallocation

    input_file = f"{input_folder}/aoc2017_day06.txt"
    puzzle = MemoryReallocation(input_file)
    assert puzzle.cycle_count() == 12841
    assert puzzle.cycles_from_last_occurrence() == 8038


def test_day07_samples():
    from aoc2017.day07.d07 import RecursiveCircus

    test = RecursiveCircus("./python/aoc2017/day07/sample1.txt")
    assert test.bottom_program() == "tknk"
    assert test.proper_weight_of_unbalanced_program() == 60


def test_day07():
    from aoc2017.day07.d07 import RecursiveCircus

    input_file = f"{input_folder}/aoc2017_day07.txt"
    puzzle = RecursiveCircus(input_file)
    assert puzzle.bottom_program() == "vtzay"
    assert puzzle.proper_weight_of_unbalanced_program() == 910


def test_day08_samples():
    from aoc2017.day08.d08 import HeardYouLikeRegisters

    test = HeardYouLikeRegisters("./python/aoc2017/day08/sample1.txt")
    assert test.max_register_value() == 1
    assert test.max_register_value_over_time() == 10


def test_day08():
    from aoc2017.day08.d08 import HeardYouLikeRegisters

    input_file = f"{input_folder}/aoc2017_day08.txt"
    puzzle = HeardYouLikeRegisters(input_file)
    assert puzzle.max_register_value() == 5221
    assert puzzle.max_register_value_over_time() == 7491


def test_day09_samples():
    from aoc2017.day09.d09 import StreamProcessing

    test = StreamProcessing("./python/aoc2017/day09/sample1.txt")
    assert test.total_score() == 5
    test = StreamProcessing("./python/aoc2017/day09/sample2.txt")
    assert test.total_score() == 16
    test = StreamProcessing("./python/aoc2017/day09/sample3.txt")
    assert test.total_score() == 1
    test = StreamProcessing("./python/aoc2017/day09/sample4.txt")
    assert test.total_score() == 9
    test = StreamProcessing("./python/aoc2017/day09/sample5.txt")
    assert test.total_score() == 3
    test = StreamProcessing("./python/aoc2017/day09/sample6.txt")
    assert test.non_cancelled_chars_in_garbage() == 10


def test_day09():
    from aoc2017.day09.d09 import StreamProcessing

    input_file = f"{input_folder}/aoc2017_day09.txt"
    puzzle = StreamProcessing(input_file)
    assert puzzle.total_score() == 12803
    assert puzzle.non_cancelled_chars_in_garbage() == 6425


def test_day10_samples():
    from aoc2017.day10.d10 import KnotHash

    test = KnotHash("./python/aoc2017/day10/sample1.txt")
    assert test.single_knot_hash(5) == 12
    test = KnotHash("./python/aoc2017/day10/sample2.txt")
    assert test.full_knot_hash() == "a2582a3a0e66e6e86e3812dcb672a272"
    test = KnotHash("./python/aoc2017/day10/sample3.txt")
    assert test.full_knot_hash() == "33efeb34ea91902bb2f59c9920caa6cd"
    test = KnotHash("./python/aoc2017/day10/sample4.txt")
    assert test.full_knot_hash() == "3efbe78a8d82f29979031a4aa0b16a9d"
    test = KnotHash("./python/aoc2017/day10/sample5.txt")
    assert test.full_knot_hash() == "63960835bcdc130f0b66d7ff4f6a5a8e"


def test_day10():
    from aoc2017.day10.d10 import KnotHash

    input_file = f"{input_folder}/aoc2017_day10.txt"
    puzzle = KnotHash(input_file)
    assert puzzle.single_knot_hash() == 11413
    assert puzzle.full_knot_hash() == "7adfd64c2a03a4968cf708d1b7fd418d"


def test_day11_samples():
    from aoc2017.day11.d11 import HexEd

    test = HexEd("./python/aoc2017/day11/sample1.txt")
    assert test.final_dist == 3
    test = HexEd("./python/aoc2017/day11/sample2.txt")
    assert test.final_dist == 0
    test = HexEd("./python/aoc2017/day11/sample3.txt")
    assert test.final_dist == 2
    test = HexEd("./python/aoc2017/day11/sample4.txt")
    assert test.final_dist == 3


def test_day11():
    from aoc2017.day11.d11 import HexEd

    input_file = f"{input_folder}/aoc2017_day11.txt"
    puzzle = HexEd(input_file)
    assert puzzle.final_dist == 675
    assert puzzle.farthest_dist == 1424


def test_day12_samples():
    from aoc2017.day12.d12 import DigitalPlumber

    test = DigitalPlumber("./python/aoc2017/day12/sample1.txt")
    assert test.group_size_of_zero() == 6
    assert test.group_count() == 2


def test_day12():
    from aoc2017.day12.d12 import DigitalPlumber

    input_file = f"{input_folder}/aoc2017_day12.txt"
    puzzle = DigitalPlumber(input_file)
    assert puzzle.group_size_of_zero() == 288
    assert puzzle.group_count() == 211


def test_day13_samples():
    from aoc2017.day13.d13 import PacketScanners

    test = PacketScanners("./python/aoc2017/day13/sample1.txt")
    assert test.trip_severity() == 24
    assert test.delay_not_to_get_caught() == 10


def test_day13():
    from aoc2017.day13.d13 import PacketScanners

    input_file = f"{input_folder}/aoc2017_day13.txt"
    puzzle = PacketScanners(input_file)
    assert puzzle.trip_severity() == 1580
    assert puzzle.delay_not_to_get_caught() == 3943252


def test_day14_samples():
    from aoc2017.day14.d14 import DiskDefragmentation

    test = DiskDefragmentation("./python/aoc2017/day14/sample1.txt")
    assert test.one_count == 8108
    assert test.region_count == 1242


def test_day14():
    from aoc2017.day14.d14 import DiskDefragmentation

    input_file = f"{input_folder}/aoc2017_day14.txt"
    puzzle = DiskDefragmentation(input_file)
    assert puzzle.one_count == 8140
    assert puzzle.region_count == 1182


def test_day15_samples():
    from aoc2017.day15.d15 import DuelingGenerators

    test = DuelingGenerators("./python/aoc2017/day15/sample1.txt")
    assert test.judges_final_count() == 588
    assert test.judges_final_count_more_picky() == 309


def test_day15():
    from aoc2017.day15.d15 import DuelingGenerators

    input_file = f"{input_folder}/aoc2017_day15.txt"
    puzzle = DuelingGenerators(input_file)
    assert puzzle.judges_final_count() == 567
    assert puzzle.judges_final_count_more_picky() == 323


def test_day16_samples():
    from aoc2017.day16.d16 import PermutationPromenade

    test = PermutationPromenade("./python/aoc2017/day16/sample1.txt", program_count=5)
    assert test.after_first_dance == "baedc"


def test_day16():
    from aoc2017.day16.d16 import PermutationPromenade

    input_file = f"{input_folder}/aoc2017_day16.txt"
    puzzle = PermutationPromenade(input_file)
    assert puzzle.after_first_dance == "dcmlhejnifpokgba"
    assert puzzle.after_billions_dance == "ifocbejpdnklamhg"


def test_day17_samples():
    from aoc2017.day17.d17 import Spinlock

    test = Spinlock(3)
    assert test.value_after_2017() == 638


def test_day17():
    from aoc2017.day17.d17 import Spinlock

    input_file = f"{input_folder}/aoc2017_day17.txt"
    puzzle = Spinlock(input_file)
    assert puzzle.value_after_2017() == 772
    assert puzzle.value_after_0_on_50_million_steps() == 42729050


def test_day18_samples():
    from aoc2017.day18.d18 import Duet

    test = Duet("./python/aoc2017/day18/sample1.txt")
    assert test.recovered_frequency() == 4
    test = Duet("./python/aoc2017/day18/sample2.txt")
    assert test.sent_values_before_deadlock() == 3


def test_day18():
    from aoc2017.day18.d18 import Duet

    input_file = f"{input_folder}/aoc2017_day18.txt"
    puzzle = Duet(input_file)
    assert puzzle.recovered_frequency() == 8600
    assert puzzle.sent_values_before_deadlock() == 7239


def test_day19_samples():
    from aoc2017.day19.d19 import ASeriesOfTubes

    test = ASeriesOfTubes("./python/aoc2017/day19/sample1.txt")
    assert test.seen_letters == "ABCDEF"
    assert test.steps == 38


def test_day19():
    from aoc2017.day19.d19 import ASeriesOfTubes

    input_file = f"{input_folder}/aoc2017_day19.txt"
    puzzle = ASeriesOfTubes(input_file)
    assert puzzle.seen_letters == "EPYDUXANIT"
    assert puzzle.steps == 17544


def test_day20_samples():
    from aoc2017.day20.d20 import ParticleSwarm

    test = ParticleSwarm("./python/aoc2017/day20/sample1.txt")
    assert test.closest_particle() == 0
    test = ParticleSwarm("./python/aoc2017/day20/sample2.txt")
    assert test.count_no_colliding_particles() == 1


def test_day20():
    from aoc2017.day20.d20 import ParticleSwarm

    input_file = f"{input_folder}/aoc2017_day20.txt"
    puzzle = ParticleSwarm(input_file)
    assert puzzle.closest_particle() == 300
    assert puzzle.count_no_colliding_particles() == 502


def test_day21_samples():
    from aoc2017.day21.d21 import FractalArt

    test = FractalArt("./python/aoc2017/day21/sample1.txt")
    assert test.pixel_count_after_expansion(iterations=2) == 12


def test_day21_numpy_samples():
    from aoc2017.day21.d21_numpy import FractalArt

    test = FractalArt("./python/aoc2017/day21/sample1.txt")
    assert test.pixel_count_after_expansion(iterations=2) == 12


def test_day21():
    from aoc2017.day21.d21 import FractalArt

    input_file = f"{input_folder}/aoc2017_day21.txt"
    puzzle = FractalArt(input_file)
    assert puzzle.pixel_count_after_expansion(iterations=5) == 167
    assert puzzle.pixel_count_after_expansion(iterations=18) == 2425195


def test_day21_numpy():
    from aoc2017.day21.d21_numpy import FractalArt

    input_file = f"{input_folder}/aoc2017_day21.txt"
    puzzle = FractalArt(input_file)
    assert puzzle.pixel_count_after_expansion(iterations=5) == 167
    assert puzzle.pixel_count_after_expansion(iterations=18) == 2425195


def test_day22_samples():
    from aoc2017.day22.d22 import SporificaVirus

    test = SporificaVirus("./python/aoc2017/day22/sample1.txt")
    assert test.count_infection_bursts(7) == 5
    assert test.count_infection_bursts(70) == 41
    assert test.count_infection_bursts(10000) == 5587
    assert test.count_infection_bursts_evolved(100) == 26
    assert test.count_infection_bursts_evolved(10000000) == 2511944


def test_day22():
    from aoc2017.day22.d22 import SporificaVirus

    input_file = f"{input_folder}/aoc2017_day22.txt"
    puzzle = SporificaVirus(input_file)
    assert puzzle.count_infection_bursts() == 5406
    assert puzzle.count_infection_bursts_evolved() == 2511640


def test_day23():
    from aoc2017.day23.d23 import CoprocessorConflagration

    input_file = f"{input_folder}/aoc2017_day23.txt"
    puzzle = CoprocessorConflagration(input_file)
    assert puzzle.mul_count() == 3969
    assert puzzle.run_debug_mode() == 917


def test_day24_samples():
    from aoc2017.day24.d24 import ElectromagneticMoat

    test = ElectromagneticMoat("./python/aoc2017/day24/sample1.txt")
    assert test.find_strongest_bridge() == 31
    assert test.find_strongest_bridge(ignore_length=False) == 19


def test_day24():
    from aoc2017.day24.d24 import ElectromagneticMoat

    input_file = f"{input_folder}/aoc2017_day24.txt"
    puzzle = ElectromagneticMoat(input_file)
    assert puzzle.find_strongest_bridge() == 1511
    assert puzzle.find_strongest_bridge(ignore_length=False) == 1471


def test_day25_samples():
    from aoc2017.day25.d25 import TheHaltingProblem

    test = TheHaltingProblem("./python/aoc2017/day25/sample1.txt")
    assert test.diagnostic_checksum() == 3


def test_day25():
    from aoc2017.day25.d25 import TheHaltingProblem

    input_file = f"{input_folder}/aoc2017_day25.txt"
    puzzle = TheHaltingProblem(input_file)
    assert puzzle.diagnostic_checksum() == 2725
