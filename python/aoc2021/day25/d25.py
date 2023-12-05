import os
from pathlib import Path


class SeaCucumber:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.load_sea()

    def load_sea(self):
        self.sea = dict()
        row = 0
        for line in self.lines:
            col = 0
            for ch in line:
                self.sea[(row, col)] = ch
                col += 1
            if row == 0:
                self.cols = col
            col = 0
            row += 1
        self.rows = row

    def move_sea_cucumbers(self):
        iterations = 0
        moved = True
        while moved:
            moved = False
            iterations += 1
            for dr, dc, ch in [(0, 1, ">"), (1, 0, "v")]:
                moving = dict()
                for location, destination in self.sea.items():
                    if destination == ch:
                        destination = (
                            (location[0] + dr) % self.rows,
                            (location[1] + dc) % self.cols,
                        )
                        if self.sea[destination] == ".":
                            moving[location] = destination
                if moving:
                    moved = True
                for location, destination in moving.items():
                    self.sea[destination] = ch
                    self.sea[location] = "."
        return iterations


if __name__ == "__main__":

    test1 = SeaCucumber("test1.txt")
    assert test1.move_sea_cucumbers() == 58
    input_file = f'{os.environ.get("aoc_inputs")}/aoc2021_day25.txt'
    sea_cucumber = SeaCucumber(input_file)
    print(sea_cucumber.move_sea_cucumbers())
