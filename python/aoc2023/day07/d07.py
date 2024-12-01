import os
from collections import Counter
from functools import cache
from pathlib import Path
from myutils.io_handler import get_input_data


class CamelCards:
    def __init__(self, filename):
        self.hands_and_bids = []
        for line in Path(filename).read_text().strip().split("\n"):
            hand, bid = line.split()
            self.hands_and_bids.append([hand, int(bid)])

    def hand_rank(self, hand, joker):
        counts = Counter(hand)
        if joker and "J" in counts:
            joker_count = counts["J"]
            counts.pop("J")
        else:
            joker_count = 0
        counts = sorted(counts.values(), reverse=True)
        if joker_count == 5:
            return 6  # five of a kind
        first = counts[0]
        if first + joker_count == 5:
            return 6  # five of a kind
        if first + joker_count == 4:
            return 5  # four of a kind
        second = counts[1]
        if first + joker_count == 3:
            if second == 2:
                return 4  # full house
            return 3  # three of a kind
        if first == 2:
            if second == 2:
                return 2  # two pairs
            return 1  # one pair
        if joker_count:
            return 1  # one pair
        return 0  # high card

    @cache
    def card_rank(self, card, joker):
        return {c: i for i, c in enumerate("J23456789TQKA" if joker else "23456789TJQKA")}[card]

    def hand_value(self, hand, joker):
        return 13**6 * self.hand_rank(hand, joker) + sum(
            [self.card_rank(c, joker) * 13**i for i, c in enumerate(hand[::-1])]
        )

    def total_winnings(self, joker=False):
        bid_values = [(bid, self.hand_value(hand, joker)) for hand, bid in self.hands_and_bids]
        bid_values = sorted(bid_values, key=lambda x: x[-1])
        return sum([(i + 1) * bid_value[0] for i, bid_value in enumerate(bid_values)])


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = CamelCards(filename)
    assert answer1 is None or test.total_winnings() == answer1
    assert answer2 is None or test.total_winnings(joker=True) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 6440, 5905)

    print("Tests passed, starting with the puzzle")

    puzzle = CamelCards(data.input_file)
    print(puzzle.total_winnings())
    print(puzzle.total_winnings(joker=True))
