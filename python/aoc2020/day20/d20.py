import re
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data
from myutils.matrix import find_all_points_with_value, flip, rotate, sub_matrix, tile_side
from myutils.utils import multiply


class JurassicJigsaw:
    def __init__(self, filename):
        self.tiles = {}
        for tile_text in Path(filename).read_text().split("\n\n"):
            id = int(re.search(r"(\d+)", tile_text).group(1))
            self.tiles[id] = tuple(tile_text.splitlines()[1:])
        self.sea_monster = (
            "                  # ",
            "#    ##    ##    ###",
            " #  #  #  #  #  #   ",
        )
        self.side_length = int(len(self.tiles) ** 0.5)
        self.grid = {}

    def find_corner_ids(self):
        self.side_ids = defaultdict(set)
        for (id, tile), side_no in product(self.tiles.items(), range(4)):
            self.side_ids[tile_side(tile, side_no, canonical=True)].add(id)
        ids_of_unique_sides = [ids.copy().pop() for ids in self.side_ids.values() if len(ids) == 1]
        unique_side_count_for_ids = Counter(ids_of_unique_sides)
        self.corner_ids = [id for id, c in unique_side_count_for_ids.items() if c == 2]
        assert len(self.corner_ids) == 4
        return multiply(self.corner_ids)

    def set_grid_tile(self, row, col):
        if row == 0 and col == 0:
            tl = self.corner_ids[0]
            self.grid[col, row] = tl
            # rotate the top left tile so that the unique sides are on the top and left
            while max(len(self.side_ids[tile_side(self.tiles[tl], s, True)]) for s in [0, 3]) > 1:
                self.tiles[tl] = rotate(self.tiles[tl])
            return
        ref_id, side_no = (self.grid[col, row - 1], 0) if col == 0 else (self.grid[col - 1, row], 3)
        ref_tile = tile_side(self.tiles[ref_id], (side_no + 2) % 4)
        ids = self.side_ids.get(ref_tile, self.side_ids[ref_tile[::-1]])
        id = (ids - {ref_id}).pop()
        self.grid[col, row] = id
        for rotate_times, flipped in product(range(4), [False, True]):
            rotated = rotate(self.tiles[id], rotate_times)
            if flipped:
                rotated = flip(rotated)
            if tile_side(rotated, side_no) == ref_tile:
                self.tiles[id] = rotated
                break

    def habitats_water_roughness(self):
        if not hasattr(self, "corner_ids"):
            self.find_corner_ids()

        for row, col in product(range(self.side_length), repeat=2):
            self.set_grid_tile(row, col)

        full_image_points = set()
        cut_tile_side_len = len(self.tiles[self.corner_ids[0]]) - 2
        for row, col in product(range(self.side_length), repeat=2):
            tile = sub_matrix(self.tiles[self.grid[col, row]], 1, -1, 1, -1)
            for p in find_all_points_with_value(tile, "#"):
                full_image_points.add(p + Point(col * cut_tile_side_len, row * cut_tile_side_len))

        monster_pattern_points = []
        for rotate_times, flipped in product(range(4), [False, True]):
            rotated = rotate(self.sea_monster, rotate_times)
            if flipped:
                rotated = flip(rotated)
            s = find_all_points_with_value(rotated, "#")
            monster_pattern_points.append(s)

        monster_points = set()
        for monster_tile in monster_pattern_points:
            for row, col in product(range(cut_tile_side_len * self.side_length), repeat=2):
                c = Point(col, row)
                if all(c + p in full_image_points for p in monster_tile):
                    monster_points.update(p + c for p in monster_tile)
        return len(full_image_points) - len(monster_points)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert JurassicJigsaw("sample1.txt").find_corner_ids() == 20899048083289
    assert JurassicJigsaw("sample1.txt").habitats_water_roughness() == 273

    print("Tests passed, starting with the puzzle")

    puzzle = JurassicJigsaw(data.input_file)

    print(puzzle.find_corner_ids())
    print(puzzle.habitats_water_roughness())
