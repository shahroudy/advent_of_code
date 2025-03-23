import os
import re
from pathlib import Path


class MojibakePuzzleDictionary:
    def __init__(self, filename):
        self.words, patterns = Path(filename).read_text().split("\n\n")
        self.regex = re.compile("|".join("^" + p.strip() + "$" for p in patterns.splitlines()))

    def sum_of_line_numbers_of_fitting_words(self):
        s = 0
        for n_zero, word in enumerate(self.words.splitlines()):
            n = n_zero + 1
            for order in (3, 5):
                if n % order == 0:
                    word = word.encode("latin-1").decode("utf-8")
            s += n if self.regex.match(word) else 0
        return s


if __name__ == "__main__":
    assert MojibakePuzzleDictionary("test-input.txt").sum_of_line_numbers_of_fitting_words() == 50
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(
        MojibakePuzzleDictionary(
            f"{input_folder}/i18n2025_day06.txt"
        ).sum_of_line_numbers_of_fitting_words()
    )
