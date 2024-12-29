import re
from collections import Counter, defaultdict
from functools import cache
from itertools import permutations, product
from pathlib import Path

from myutils.geometry import DIR_CHARS, Point
from myutils.io_handler import get_input_data


class KeypadConundrum:
    def __init__(self, filename):
        self.door_codes = Path(filename).read_text().splitlines()

        self.physical = {
            ch: Point(x, y)
            for y, row in enumerate(["789", "456", "123", "X0A"])
            for x, ch in enumerate(row)
        }
        self.directional = {
            ch: Point(x, y) for y, line in enumerate(["X^A", "<v>"]) for x, ch in enumerate(line)
        }

    @cache
    def distance_in_dir_kb(self, from_button, to_button):
        return self.directional[from_button].manhattan_dist(self.directional[to_button])

    @cache
    def moves_in_keyboard(self, from_button, to_button, is_physical_keyboard=False):
        keyboard = self.physical if is_physical_keyboard else self.directional
        delta = keyboard[to_button] - keyboard[from_button]
        moves = ">" * delta.x + "<" * -delta.x + "v" * delta.y + "^" * -delta.y
        per = set(permutations(moves))
        minimal_set, min_length = set(), float("inf")
        for p in per:
            current = keyboard[from_button]
            for ch in p:
                current = current + DIR_CHARS[ch]
                if keyboard["X"] == current:
                    break
            else:
                moves = "".join(p) + "A"
                length = sum(self.distance_in_dir_kb(a, b) for a, b in zip(moves[:-1], moves[1:]))
                if length < min_length:
                    minimal_set, min_length = {moves}, length
                elif length == min_length:
                    minimal_set.add(moves)
        return minimal_set

    def change_counter_dict(self, sequence):
        full_sequence = "A" + sequence
        return dict(Counter(zip(full_sequence[:-1], full_sequence[1:])))

    def key_in_keyboard(self, input, is_physical_keyboard=False):
        input_frequencies = self.change_counter_dict(input) if isinstance(input, str) else input
        frequencies = [defaultdict(int)]
        for input_move, input_frequency in input_frequencies.items():
            next_results = []
            possible_moves = self.moves_in_keyboard(*input_move, is_physical_keyboard)
            for so_far_frequencies, needed_move in product(frequencies, possible_moves):
                new_frequencies = so_far_frequencies.copy()
                for move, frequency in self.change_counter_dict(needed_move).items():
                    new_frequencies[move] += input_frequency * frequency
                next_results.append(new_frequencies)
            frequencies = next_results
        return frequencies

    def sum_of_complexities(self, robot_count=2):
        complexities_sum = 0
        for door_code in self.door_codes:
            frequencies = self.key_in_keyboard(door_code, is_physical_keyboard=True)
            for _ in range(robot_count):
                frequencies = [d for m in frequencies for d in self.key_in_keyboard(m)]
                min_size = min(sum(d.values()) for d in frequencies)
                frequencies = [d for d in frequencies if sum(d.values()) == min_size]
            complexities_sum += min_size * int(re.match(r"(\d+)", door_code).group())
        return complexities_sum


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert KeypadConundrum("sample1.txt").sum_of_complexities(2) == 68 * 29
    assert KeypadConundrum("sample2.txt").sum_of_complexities(2) == 60 * 980
    assert KeypadConundrum("sample3.txt").sum_of_complexities(2) == 68 * 179
    assert KeypadConundrum("sample4.txt").sum_of_complexities(2) == 64 * 456
    assert KeypadConundrum("sample5.txt").sum_of_complexities(2) == 64 * 379
    assert KeypadConundrum("sample6.txt").sum_of_complexities(2) == 126384

    print("Tests passed, starting with the puzzle")

    puzzle = KeypadConundrum(data.input_file)

    assert puzzle.sum_of_complexities(2) == 222670
    assert puzzle.sum_of_complexities(25) == 271397390297138

    print(puzzle.sum_of_complexities(2))
    print(puzzle.sum_of_complexities(25))
