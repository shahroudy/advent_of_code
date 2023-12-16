import os
from functools import cache
from pathlib import Path


class TheFloorWillBeLava:
    def __init__(self, filename):
        self.map = dict()
        for row, line in enumerate(Path(filename).read_text().strip().splitlines()):
            for col, ch in enumerate(line):
                self.map[(col, row)] = ch
        self.rows, self.cols = row + 1, col + 1
        self.directions = {"e": (1, 0), "w": (-1, 0), "n": (0, -1), "s": (0, 1)}

    @cache
    def next_beams(self, beam):
        direction = beam[2]
        next_location = tuple(beam[i] + self.directions[direction][i] for i in range(2))
        if next_location in self.map:
            next_tile = self.map[next_location]
            if next_tile == "\\":
                if direction == "e":
                    next_dir = "s"
                elif direction == "w":
                    next_dir = "n"
                elif direction == "n":
                    next_dir = "w"
                elif direction == "s":
                    next_dir = "e"
            elif next_tile == "/":
                if direction == "e":
                    next_dir = "n"
                elif direction == "w":
                    next_dir = "s"
                elif direction == "n":
                    next_dir = "e"
                elif direction == "s":
                    next_dir = "w"
            elif next_tile == "-":
                if direction in "ns":
                    next_dir = "ew"
                else:
                    next_dir = direction
            elif next_tile == "|":
                if direction in "ew":
                    next_dir = "ns"
                else:
                    next_dir = direction
            else:
                next_dir = direction
            return [(next_location[0], next_location[1], nd) for nd in next_dir]
        else:
            return []

    def energizer_count(self, beam):
        history = set()
        beams = [beam]
        while beams:
            next_beams = []
            for beam in beams:
                for next in self.next_beams(beam):
                    if next not in history:
                        next_beams.append(next)
                        history.add(next)
            beams = next_beams
        return len(set(b[:2] for b in history))

    def top_left_beam_energized_count(self):
        return self.energizer_count((-1, 0, "e"))

    def max_beam_energized_count(self):
        candidate_beams = []
        for y in range(self.rows):
            candidate_beams.append((-1, y, "e"))
            candidate_beams.append((self.cols, y, "w"))
        for x in range(self.cols):
            candidate_beams.append((x, -1, "s"))
            candidate_beams.append((x, self.rows, "n"))
        return max(self.energizer_count(beam) for beam in candidate_beams)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = TheFloorWillBeLava(filename)
    assert answer1 is None or test.top_left_beam_energized_count() == answer1
    assert answer2 is None or test.max_beam_energized_count() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 46, 51)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day16.txt'
    puzzle = TheFloorWillBeLava(input_file)
    print(puzzle.top_left_beam_energized_count())
    print(puzzle.max_beam_energized_count())
