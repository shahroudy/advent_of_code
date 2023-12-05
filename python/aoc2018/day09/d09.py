import os
from collections import deque
from pathlib import Path


class MarbleMania:
    def __init__(self, filename):
        input_words = Path(filename).read_text().strip().split()
        self.players, self.max_marble = [int(w) for w in input_words if w.isnumeric()]

    def winnin_elf_score(self, factor=1):
        circle = deque([0])
        scores = [0] * self.players
        for marble in range(1, self.max_marble * factor + 1):
            if marble % 23:
                circle.rotate(-1)
                circle.append(marble)
            else:
                circle.rotate(7)
                scores[marble % self.players] += marble + circle.pop()
                circle.rotate(-1)
        return max(scores)


if __name__ == "__main__":

    assert MarbleMania("test1.txt").winnin_elf_score() == 32
    assert MarbleMania("test2.txt").winnin_elf_score() == 8317
    assert MarbleMania("test3.txt").winnin_elf_score() == 146373
    assert MarbleMania("test4.txt").winnin_elf_score() == 2764
    assert MarbleMania("test5.txt").winnin_elf_score() == 54718
    assert MarbleMania("test6.txt").winnin_elf_score() == 37305

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2018_day09.txt'
    marble_mania = MarbleMania(input_file)
    print(marble_mania.winnin_elf_score())
    print(marble_mania.winnin_elf_score(100))
