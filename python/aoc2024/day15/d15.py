from functools import reduce
from pathlib import Path

from myutils.geometry import DIR_CHARS, Point
from myutils.io_handler import get_input_data


class WarehouseWoes:
    def __init__(self, filename):
        grid_text, moves_text = Path(filename).read_text().split("\n\n")
        self.init_walls, self.init_boxes = set(), set()
        for row, line in enumerate(grid_text.splitlines()):
            for col, ch in enumerate(line):
                p = Point(col, row)
                if ch == "@":
                    self.starting_position = p
                if ch == "#":
                    self.init_walls.add(p)
                if ch == "O":
                    self.init_boxes.add(p)
        self.moves = moves_text.replace("\n", "").strip()

    def move_boxes(self, is_second_warehouse=False, display=False):
        def display_current_layout():
            for y in range(min(p.y for p in walls), max(p.y for p in walls) + 1):
                for x in range(min(p.x for p in walls), max(p.x for p in walls) + 1):
                    p = Point(x, y)
                    if p in walls:
                        print("#", end="")
                    elif p in boxes:
                        print("[" if is_second_warehouse else "O", end="")
                    elif is_second_warehouse and p - ext in boxes:
                        print("]", end="")
                    elif p == robot:
                        print(move_command, end="")
                    else:
                        print(".", end="")
                print()
            print()

        if not is_second_warehouse:
            robot = self.starting_position
            walls = self.init_walls
            boxes = self.init_boxes.copy()
        else:
            fac, ext = Point(2, 1), Point(1, 0)
            robot = self.starting_position * Point(2, 1)
            walls = reduce(set.union, [{w * fac, w * fac + ext} for w in self.init_walls])
            boxes = {b * fac for b in self.init_boxes}

        for move_command in self.moves:
            move = DIR_CHARS[move_command]
            if display:
                display_current_layout()
            to_be_occupied = {robot + move}
            moving_boxes = set()
            while to_be_occupied:
                p = to_be_occupied.pop()
                if p in walls:
                    break  # we hit a wall, there's no room to move
                if p in boxes:
                    if p not in moving_boxes:
                        moving_boxes.add(p)
                        to_be_occupied.add(p + move)
                        if is_second_warehouse:
                            to_be_occupied.add(p + ext + move)
                if is_second_warehouse and (q := p - ext) in boxes:
                    if q not in moving_boxes:
                        moving_boxes.add(q)
                        to_be_occupied.add(q + move)
                        to_be_occupied.add(p + move)
            else:
                boxes = boxes - moving_boxes | {n + move for n in moving_boxes}
                robot = robot + move
        if display:
            display_current_layout()
        return sum(c.y * 100 + c.x for c in boxes)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert WarehouseWoes("sample1.txt").move_boxes() == 2028
    assert WarehouseWoes("sample2.txt").move_boxes() == 10092
    assert WarehouseWoes("sample2.txt").move_boxes(is_second_warehouse=True) == 9021

    print("Tests passed, starting with the puzzle")

    puzzle = WarehouseWoes(data.input_file)

    print(puzzle.move_boxes())
    print(puzzle.move_boxes(is_second_warehouse=True))
