import os
import re
from itertools import product
from pathlib import Path


class SandSlabs:
    def __init__(self, filename):
        lines = Path(filename).read_text().strip().splitlines()
        br = []
        for nums in [list(map(int, re.findall(r"-?\d+", line))) for line in lines]:
            mM = [sorted([nums[i], nums[i + 3]]) for i in range(3)]
            br.append(list(product(*[range(mM[i][0], mM[i][1] + 1) for i in range(3)])))
        self.bricks = {i: b for i, b in enumerate(sorted(br, key=lambda x: min(b[2] for b in x)))}
        self.simulate()

    def find_fixed_bricks(self, bricks, falling, occupied):
        sitting = set()
        while falling:
            no_more_sitting = True
            for n in falling:
                for x, y, z in bricks[n]:
                    if z <= 1 or (x, y, z - 1) in occupied:
                        sitting.add(n)
                        for x, y, z in bricks[n]:
                            occupied.add((x, y, z))
                        no_more_sitting = False
                        break
            falling -= sitting
            if no_more_sitting:
                break
        return sitting

    def simulate(self):
        falling = set(range(len(self.bricks)))
        occupied = set()
        while falling:
            fixed = self.find_fixed_bricks(self.bricks, falling, occupied)
            for f in falling:
                self.bricks[f] = [(x, y, z - 1) for x, y, z in self.bricks[f]]

        # check what will fall
        self.disintegrated_count = len(self.bricks)
        self.sum_falling_removing_other_bricks = 0
        for n in self.bricks.keys():
            falling = set(range(len(self.bricks))) - {n}
            cur_bricks = {k: v.copy() for k, v in self.bricks.items() if k != n}
            occupied = set()
            fell = False
            while falling and not fell:
                fixed = self.find_fixed_bricks(cur_bricks, falling, occupied)
                if len(fixed) == 0 and len(falling) > 0:
                    fell = True
                    self.disintegrated_count -= 1
                    self.sum_falling_removing_other_bricks += len(falling)
                    break


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = SandSlabs(filename)
    assert answer1 is None or test.disintegrated_count == answer1
    assert answer2 is None or test.sum_falling_removing_other_bricks == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 5, 7)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day22.txt'
    puzzle = SandSlabs(input_file)
    print(puzzle.disintegrated_count)
    print(puzzle.sum_falling_removing_other_bricks)
