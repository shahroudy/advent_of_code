from pathlib import Path

from myutils.io_handler import get_input_data


class GuardGallivant:
    def __init__(self, filename):
        self.input_text = Path(filename).read_text()
        self.process_blocks_map()
        self.visited_first, _ = self.travel()

    def process_blocks_map(self):
        dir_chars = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
        self.turn_right = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
        lines = self.input_text.splitlines()
        self.cells = set()
        self.blocks = set()
        self.start = None
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                if ch in dir_chars:
                    self.start = ((col, row), dir_chars[ch])
                if ch == "#":
                    self.blocks.add((col, row))
                self.cells.add((col, row))
        self.rows, self.cols = row + 1, col + 1

    def travel(self, blocks=None):
        blocks = blocks or self.blocks
        current, direction = self.start
        visited = {current}
        history = {(current, direction)}
        looped = False
        while True:
            new = (current[0] + direction[0], current[1] + direction[1])
            if new not in self.cells:
                break
            while new in blocks:
                new = current
                direction = self.turn_right[direction]
            visited.add(new)
            current = new
            if (current, direction) in history:
                looped = True
                break
            history.add((current, direction))
        return visited, looped

    def number_of_visited_positions(self):
        return len(self.visited_first)

    def number_of_looping_obstructions(self):
        res = 0
        for obstruction in self.visited_first:
            _, looped = self.travel(self.blocks | {obstruction})
            if looped:
                res += 1
        return res


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert GuardGallivant("sample1.txt").number_of_visited_positions() == 41
    assert GuardGallivant("sample1.txt").number_of_looping_obstructions() == 6

    print("Tests passed, starting with the puzzle")

    puzzle = GuardGallivant(data.input_file)

    print(puzzle.number_of_visited_positions())
    print(puzzle.number_of_looping_obstructions())
