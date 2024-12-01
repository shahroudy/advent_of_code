import os
import numpy as np
from myutils.file_reader import read_line_groups
from myutils.io_handler import get_input_data


class GiantSquidNP:
    def __init__(self, filename):
        line_groups = read_line_groups(filename)
        self.numbers = list(map(int, line_groups[0][0].split(",")))

        cards = []
        for card_input in line_groups[1:]:
            card = []
            for line in card_input:
                card.append(list(map(int, line.split())))
            cards.append(card)
        self.cards = np.array(cards)
        self.n_cards, self.n_rows, self.n_cols = self.cards.shape

    def reset_marks(self):
        self.marks = np.zeros_like(self.cards, dtype=bool)

    def mark_card(self, card_idx, number):
        self.marks[card_idx, self.cards[card_idx, :] == number] = True

    def card_score(self, card_idx):
        return np.sum(self.cards[card_idx, self.marks[card_idx, :] == False])

    def card_bingo(self, card_idx):
        card = self.marks[card_idx]
        return np.any(np.all(card, axis=0)) or np.any(np.all(card, axis=1))

    def bingo_system(self):
        self.reset_marks()
        for number in self.numbers:
            for card_idx in range(self.n_cards):
                self.mark_card(card_idx, number)
                if self.card_bingo(card_idx):
                    return number * self.card_score(card_idx)

    def last_to_bingo(self):
        self.reset_marks()
        no_bingo_cards = set(range(self.n_cards))

        for number in self.numbers:
            for card_idx in no_bingo_cards.copy():
                self.mark_card(card_idx, number)
                if self.card_bingo(card_idx):
                    no_bingo_cards.remove(card_idx)
                    if not no_bingo_cards:
                        return number * self.card_score(card_idx)


if __name__ == "__main__":
    data = get_input_data(__file__)
    test1 = GiantSquidNP("test1.txt")
    assert test1.bingo_system() == 4512
    assert test1.last_to_bingo() == 1924

    giant_squid = GiantSquidNP(data.input_file)
    print(giant_squid.bingo_system())
    print(giant_squid.last_to_bingo())
