import re
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.matrix import flip, rotate, tuple_matrix


class FractalArt:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.exp = {}
        for line in lines:
            left, right = re.split(r" => ", line)
            right = self.make_list_tile(right.split("/"))
            left = self.make_list_tile(left.split("/"))
            for tile in (left, flip(left)):
                for k in range(4):
                    self.exp[tuple_matrix(rotate(tile, k))] = right

    def make_list_tile(self, tile):
        return [list(row) for row in tile]

    def pixel_count_after_expansion(self, iterations=5):
        cur = self.make_list_tile([".#.", "..#", "###"])
        for _ in range(iterations):
            next = []
            for tile_size in (2, 3):
                if len(cur) % tile_size == 0:
                    new_tile_size = tile_size + 1
                    for row in range(0, len(cur), tile_size):
                        new_rows = [[] for _ in range(new_tile_size)]
                        for col in range(0, len(cur), tile_size):
                            tile = [cur[row + r][col : col + tile_size] for r in range(tile_size)]
                            new_tile = self.exp[tuple_matrix(tile)]
                            for r in range(new_tile_size):
                                new_rows[r].extend(new_tile[r])
                        next.extend(new_rows)
                    break
            cur = next
        return sum(sum(ch == "#" for ch in row) for row in cur)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert FractalArt("sample1.txt").pixel_count_after_expansion(iterations=2) == 12

    print("Tests passed, starting with the puzzle")

    puzzle = FractalArt(data.input_file)

    print(puzzle.pixel_count_after_expansion(iterations=5))
    print(puzzle.pixel_count_after_expansion(iterations=18))
