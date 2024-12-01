import os
from collections import Counter
from pathlib import Path
from myutils.io_handler import get_input_data


class HighEntropyPassphrases:
    def __init__(self, filename):
        self.inp = [line.split(" ") for line in Path(filename).read_text().strip().split("\n")]

    def is_valid(self, passphrase, rearranged_invalid=False):
        if len(passphrase) != len(set(passphrase)):
            return False
        elif rearranged_invalid:
            history = set()
            for word in passphrase:
                char_counter = [(k, v) for k, v in Counter(word).items()]
                char_counter.sort(key=lambda x: x[0])
                char_counter = tuple(char_counter)
                if char_counter in history:
                    return False
                else:
                    history.add(char_counter)
        return True

    def number_of_simple_valid_passphrases(self):
        return sum(self.is_valid(passphrase, rearranged_invalid=False) for passphrase in self.inp)

    def number_of_valid_passphrases_with_no_rearranging(self):
        return sum(self.is_valid(passphrase, rearranged_invalid=True) for passphrase in self.inp)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert HighEntropyPassphrases("sample1.txt").number_of_simple_valid_passphrases() == 2
    assert (
        HighEntropyPassphrases("sample2.txt").number_of_valid_passphrases_with_no_rearranging() == 3
    )

    print("Tests passed, starting with the puzzle")

    puzzle = HighEntropyPassphrases(data.input_file)
    print(puzzle.number_of_simple_valid_passphrases())
    print(puzzle.number_of_valid_passphrases_with_no_rearranging())
