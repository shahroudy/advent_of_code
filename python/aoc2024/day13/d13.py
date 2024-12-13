import re
from pathlib import Path

from myutils.io_handler import get_input_data
from sympy import Symbol
from sympy.solvers import solve


class ClawContraption:
    def __init__(self, filename):
        machines = Path(filename).read_text().split("\n\n")
        self.machines = [list(map(int, re.findall(r"\d+", m))) for m in machines]

    def min_tokens_for_most_win(self, prize_move=0):
        token_count = 0
        for ax, ay, bx, by, px, py in self.machines:
            px, py = px + prize_move, py + prize_move
            ac, bc = Symbol("ac"), Symbol("bc")
            solution = solve([ac * ax + bc * bx - px, ac * ay + bc * by - py], ac, bc)
            acs, bcs = solution[ac], solution[bc]
            if prize_move == 0 and (acs > 100 or bcs > 100):
                continue
            if acs.is_integer and bcs.is_integer and acs >= 0 and bcs >= 0:
                token_count += int(3 * acs + bcs)
        return token_count


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ClawContraption("sample1.txt").min_tokens_for_most_win() == 480

    print("Tests passed, starting with the puzzle")

    puzzle = ClawContraption(data.input_file)

    print(puzzle.min_tokens_for_most_win())
    print(puzzle.min_tokens_for_most_win(10000000000000))
