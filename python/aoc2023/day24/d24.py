import os
import re
from itertools import combinations
from pathlib import Path

from sympy import Eq, Symbol, symbols
from sympy.solvers import solve


class NeverTellMeTheOdds:
    def __init__(self, filename):
        lines = Path(filename).read_text().strip().splitlines()
        self.hailstones = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

    def colliding_hailstone_pairs(self, low=7, high=27):
        colliding_count = 0
        for (x1, y1, _, dx1, dy1, _), (x2, y2, _, dx2, dy2, _) in combinations(self.hailstones, 2):
            # x = x1+t1*dx1 = x2+t2*dx2
            # y = y1+t1*dy1 = y2+t2*dy2
            # t1 = (x2-x1+t2*dx2)/dx1
            # t2 = (y1-y2+t1*dy1)/dy2
            # t1 = (x2-x1+((y1-y2+t1*dy1)/dy2)*dx2)/dx1
            # t1 = x2/dx1-x1/dx1+ ((y1-y2+t1*dy1)/dy2)*dx2/dx1
            # t1 = x2/dx1-x1/dx1+ (y1-y2)*dx2/(dx1*dy2) + t1*dy1*dx2/(dy2*dx1)
            # t1*(1-dy1*dx2/(dy2*dx1)) = x2/dx1-x1/dx1+ (y1-y2)*dx2/(dx1*dy2)
            try:
                t1 = (x2 / dx1 - x1 / dx1 + (y1 - y2) * dx2 / (dx1 * dy2)) / (
                    1 - dy1 * dx2 / (dy2 * dx1)
                )
                t2 = (y1 - y2 + t1 * dy1) / dy2
                x = x1 + t1 * dx1
                y = y1 + t1 * dy1
            except ZeroDivisionError:
                continue
            if low <= x <= high and low <= y <= high and t1 >= 0 and t2 >= 0:
                colliding_count += 1
        return colliding_count

    def colliding_hailstone_pairs_with_sympy(self, low=7, high=27):
        colliding_count = 0
        for (x1, y1, _, dx1, dy1, _), (x2, y2, _, dx2, dy2, _) in combinations(self.hailstones, 2):
            x, y, t1, t2 = symbols("x,y,t1,t2")
            s = solve(
                [
                    Eq(x, x1 + t1 * dx1),
                    Eq(x, x2 + t2 * dx2),
                    Eq(y, y1 + t1 * dy1),
                    Eq(y, y2 + t2 * dy2),
                ]
            )
            if s and low <= s[x] <= high and low <= s[y] <= high and s[t1] >= 0 and s[t2] >= 0:
                colliding_count += 1
        return colliding_count

    def find_the_rock_which_smashes_all_hailstone(self):
        x, y, z, dx, dy, dz = symbols("x,y,z,dx,dy,dz")
        equations = []
        for i, (xi, yi, zi, dxi, dyi, dzi) in enumerate(self.hailstones):
            ti = Symbol(f"t{i}")
            equations.append(Eq(x + ti * dx, xi + ti * dxi))
            equations.append(Eq(y + ti * dy, yi + ti * dyi))
            equations.append(Eq(z + ti * dz, zi + ti * dzi))

            # we have 6+i unknowns and 3*i equations,
            # so in a well-defined system we should be able to solve with 3 hailstones.
            # but if we can't, we can try with more hailstones!
            if i >= 3:
                solution = solve(equations[: i * 3])
                try:
                    return solution[0][x] + solution[0][y] + solution[0][z]
                except KeyError:
                    continue


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = NeverTellMeTheOdds(filename)
    assert answer1 is None or test.colliding_hailstone_pairs() == answer1
    assert answer2 is None or test.find_the_rock_which_smashes_all_hailstone() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 2, 47)
    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day24.txt'
    puzzle = NeverTellMeTheOdds(input_file)
    print(puzzle.colliding_hailstone_pairs(low=200000000000000, high=400000000000000))
    print(puzzle.find_the_rock_which_smashes_all_hailstone())
