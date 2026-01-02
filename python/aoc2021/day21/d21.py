from collections import Counter, deque
from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import find_all_re


class DiracDice:
    def __init__(self, filename):
        self.init = list(map(int, find_all_re(r": (\d+)", Path(filename).read_text())))

    def deterministic_dice(self):
        positions = [i - 1 for i in self.init]
        scores = [0, 0]
        die = 0
        while True:
            for turn in range(2):
                positions[turn] = (positions[turn] + sum(range(die + 1, die + 4))) % 10
                scores[turn] += positions[turn] + 1
                die += 3
                if scores[turn] >= 1000:
                    return scores[1 - turn] * die

    def quantum_dice(self):
        dice_sums = Counter([sum(ds) for ds in product([1, 2, 3], repeat=3)])
        state = (self.init[0] - 1, self.init[1] - 1, 0, 0, 0)  # pos1, pos2, score1, score2, turn
        counts = {state: 1}
        queue = deque([state])
        wins = [0, 0]
        while queue:
            state = queue.popleft()
            count = counts.pop(state)
            pos1, pos2, score1, score2, turn = state
            for move, ways in dice_sums.items():
                np = ((pos1 if turn == 0 else pos2) + move) % 10
                ns = (score1 if turn == 0 else score2) + np + 1
                if ns >= 21:
                    wins[turn] += count * ways
                else:
                    next = (np, pos2, ns, score2, 1) if turn == 0 else (pos1, np, score1, ns, 0)
                    if next not in counts:
                        queue.append(next)
                        counts[next] = count * ways
                    else:
                        counts[next] += count * ways
        return max(wins)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert DiracDice("sample1.txt").deterministic_dice() == 739785
    assert DiracDice("sample1.txt").quantum_dice() == 444356092776315

    print("Tests passed, starting with the puzzle")

    puzzle = DiracDice(data.input_file)

    print(puzzle.deterministic_dice())
    print(puzzle.quantum_dice())
