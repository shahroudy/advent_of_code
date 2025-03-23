import os
from functools import cache
from pathlib import Path


class HomersCipher:
    def __init__(self, filename):
        self.input_text = Path(filename).read_text()
        self.capitals = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
        self.index = {ch: i for i, ch in enumerate(self.capitals)}
        self.names = list(map(str.upper, ["Οδυσσευς", "Οδυσσεως", "Οδυσσει", "Οδυσσεα", "Οδυσσευ"]))
        self.min_name_length = min({len(name) for name in self.names})

    @cache
    def char_shift(self, char: str, shift: int):
        if char not in self.capitals:
            return char
        return self.capitals[(self.index[char] + shift) % len(self.capitals)]

    @cache
    def shift(self, word: str):
        if len(word) < self.min_name_length:
            return 0
        for i in range(len(self.capitals)):
            shifted = "".join([self.char_shift(c, i) for c in word])
            if any(name in shifted for name in self.names):
                return i
        return 0

    def sum_of_all_shifts(self):
        return sum(self.shift(word) for word in self.input_text.upper().split())


if __name__ == "__main__":
    assert HomersCipher("test-input.txt").sum_of_all_shifts() == 19
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(HomersCipher(f"{input_folder}/i18n2025_day11.txt").sum_of_all_shifts())
