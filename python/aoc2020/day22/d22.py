from collections import deque
from pathlib import Path

from myutils.io_handler import get_input_data


class CrabCombat:
    def __init__(self, filename):
        hands_txt = Path(filename).read_text().split("\n\n")
        self.hands = [list(map(int, hand.splitlines()[1:])) for hand in hands_txt]

    def hand_score(self, p):
        return sum((i + 1) * c for i, c in enumerate(reversed(p)))

    def result_of_combat(self, recursive=False):
        _, p = self.combat(*self.hands, recursive=recursive)
        return self.hand_score(p)

    def combat(self, player1, player2, recursive=False):
        hand1, hand2 = deque(player1), deque(player2)
        seen = set()
        while hand1 and hand2:
            if recursive:
                if (t := (tuple(hand1), tuple(hand2))) in seen:
                    return 1, hand1
                seen.add(t)
            card1, card2 = hand1.popleft(), hand2.popleft()
            if recursive and len(hand1) >= card1 and len(hand2) >= card2:
                winner, _ = self.combat(list(hand1)[:card1], list(hand2)[:card2], recursive)
            else:
                winner = 1 if card1 > card2 else 2
            if winner == 1:
                hand1.extend([card1, card2])
            else:
                hand2.extend([card2, card1])
        return (1 if hand1 else 2), (hand1 + hand2)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert CrabCombat("sample1.txt").result_of_combat() == 306
    assert CrabCombat("sample1.txt").result_of_combat(recursive=True) == 291

    print("Tests passed, starting with the puzzle")

    puzzle = CrabCombat(data.input_file)

    print(puzzle.result_of_combat())
    print(puzzle.result_of_combat(recursive=True))
