import os
from collections import defaultdict
from pathlib import Path
from myutils.io_handler import get_input_data


class CubeConundrum:
    def __init__(self, filename):
        self.games = {}
        for line in Path(filename).read_text().strip().split("\n"):
            left, right = line.split(":")
            id = int(left.split(" ")[1])
            game_sets = right.split(";")
            mx = defaultdict(int)
            for game_set in game_sets:
                for color_count in game_set.strip().split(","):
                    count, color = color_count.strip().split(" ")
                    mx[color] = max(mx[color], int(count))
            self.games[id] = mx

    def is_possible(self, mins):
        return mins["red"] <= 12 and mins["green"] <= 13 and mins["blue"] <= 14

    def sum_of_possible_games(self):
        return sum([id for id, mins in self.games.items() if self.is_possible(mins)])

    def sum_of_power_of_sets(self):
        return sum([mins["red"] * mins["green"] * mins["blue"] for mins in self.games.values()])


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = CubeConundrum(filename)
    assert answer1 is None or test.sum_of_possible_games() == answer1
    assert answer2 is None or test.sum_of_power_of_sets() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 8, 2286)

    print("Tests passed, starting with the puzzle")

    puzzle = CubeConundrum(data.input_file)
    print(puzzle.sum_of_possible_games())
    print(puzzle.sum_of_power_of_sets())
