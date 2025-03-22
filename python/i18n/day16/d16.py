from functools import cache
from pathlib import Path


class EightBitUnboxing:
    def __init__(self, filename):
        self.grid = Path(filename).read_text(encoding="CP437").splitlines()

        self.connections = {  # values are number of connections in (right, down, left, up) order
            "│": (0, 1, 0, 1),
            "┤": (0, 1, 1, 1),
            "╡": (0, 1, 2, 1),
            "╢": (0, 2, 1, 2),
            "╖": (0, 2, 1, 0),
            "╕": (0, 1, 2, 0),
            "╣": (0, 2, 2, 2),
            "║": (0, 2, 0, 2),
            "╗": (0, 2, 2, 0),
            "╝": (0, 0, 2, 2),
            "╜": (0, 0, 1, 2),
            "╛": (0, 0, 2, 1),
            "┐": (0, 1, 1, 0),
            "└": (1, 0, 0, 1),
            "┴": (1, 0, 1, 1),
            "┬": (1, 1, 1, 0),
            "├": (1, 1, 0, 1),
            "─": (1, 0, 1, 0),
            "┼": (1, 1, 1, 1),
            "╞": (2, 1, 0, 1),
            "╟": (1, 2, 0, 2),
            "╚": (2, 0, 0, 2),
            "╔": (2, 2, 0, 0),
            "╩": (2, 0, 2, 2),
            "╦": (2, 2, 2, 0),
            "╠": (2, 2, 0, 2),
            "═": (2, 0, 2, 0),
            "╬": (2, 2, 2, 2),
            "╧": (2, 0, 2, 1),
            "╨": (1, 0, 1, 2),
            "╤": (2, 1, 2, 0),
            "╥": (1, 2, 1, 0),
            "╙": (1, 0, 0, 2),
            "╘": (2, 0, 0, 1),
            "╒": (2, 1, 0, 0),
            "╓": (1, 2, 0, 0),
            "╫": (1, 2, 1, 2),
            "╪": (2, 1, 2, 1),
            "┘": (0, 0, 1, 1),
            "┌": (1, 1, 0, 0),
        }
        self.code_to_char = {v: k for k, v in self.connections.items()}
        self.directions = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}

    @cache
    def rotations(self, x):
        history = set()
        result = []
        for i in range(4):
            if x not in history:
                result.append((x, i))
                history.add(x)
            x = (x[3], x[0], x[1], x[2])  # rotate the tuple
        return result

    def needed_rotations(self, sample=False):
        grid = self.grid if sample else [line[7:-7] for line in self.grid[5:-6]]

        initial_state = {
            (x, y): self.connections[ch]
            for y, line in enumerate(grid)
            for x, ch in enumerate(line)
            if ch in self.connections.keys()
        }
        cols, rows = len(grid[0]), len(grid)
        current = {(0, -1): self.connections["│"], (cols - 1, rows): self.connections["│"]}
        initial_state |= current

        rotation_steps = 0
        while set(current) < set(initial_state):
            for current_tile in set(initial_state) - set(current):
                x, y, code = *current_tile, initial_state[current_tile]
                possible_rotations = []
                for rotated, steps in self.rotations(code):
                    for side in range(4):
                        dx, dy = self.directions[side]
                        n = (x + dx, y + dy)
                        if (n not in initial_state) and (rotated[side] != 0):
                            break
                        if n in current and rotated[side] != current[n][(side + 2) % 4]:
                            break
                    else:  # it's a match
                        possible_rotations.append((rotated, steps))
                if len(possible_rotations) == 1:
                    match, steps = possible_rotations[0]
                    current[current_tile] = match
                    rotation_steps += steps
        return rotation_steps


if __name__ == "__main__":
    assert EightBitUnboxing("test-input").needed_rotations(True) == 34
    print("Tests passed, starting with the puzzle")
    print(EightBitUnboxing("input").needed_rotations(False))
