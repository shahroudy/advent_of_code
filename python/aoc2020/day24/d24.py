from itertools import product
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data

directions = {
    "e": Point(2, 0),
    "ne": Point(1, -2),
    "se": Point(1, 2),
    "w": Point(-2, 0),
    "nw": Point(-1, -2),
    "sw": Point(-1, 2),
}


class LobbyLayout:
    def __init__(self, filename):
        self.instructions = Path(filename).read_text().splitlines()

    def black_count_after_instructions(self):
        self.blacks = set()
        for instruction in self.instructions:
            remaining_instructions = instruction
            current = Point(0, 0)
            while remaining_instructions:
                for direction, delta in directions.items():
                    if remaining_instructions.startswith(direction):
                        current += delta
                        remaining_instructions = remaining_instructions[len(direction) :]
                        break
            if current in self.blacks:
                self.blacks.remove(current)
            else:
                self.blacks.add(current)
        return len(self.blacks)

    def black_count_after_100_days(self):
        if not hasattr(self, "blacks"):
            self.black_count_after_instructions()

        for _ in range(100):
            new_blacks = set()
            for tile in self.blacks | {f + d for f, d in product(self.blacks, directions.values())}:
                flipped_neighbors = sum(tile + d in self.blacks for d in directions.values())
                if tile in self.blacks:
                    if flipped_neighbors in {1, 2}:
                        new_blacks.add(tile)
                else:
                    if flipped_neighbors == 2:
                        new_blacks.add(tile)
            self.blacks = new_blacks
        return len(self.blacks)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert LobbyLayout("sample1.txt").black_count_after_instructions() == 10
    assert LobbyLayout("sample1.txt").black_count_after_100_days() == 2208

    print("Tests passed, starting with the puzzle")

    puzzle = LobbyLayout(data.input_file)

    print(puzzle.black_count_after_instructions())
    print(puzzle.black_count_after_100_days())
