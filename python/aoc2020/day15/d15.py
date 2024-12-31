import re
from pathlib import Path

from myutils.io_handler import get_input_data


class RambunctiousRecitation:
    def __init__(self, filename):
        self.inp = [int(n) for n in re.findall(r"[+-]?\d+", Path(filename).read_text())]

    def whats_nth_spoken_number(self, n=2020):
        history = [-1] * n
        for index, number in enumerate(self.inp[:-1]):
            history[number] = index
        last_number = self.inp[-1]
        last_index = history[last_number]
        history[last_number] = len(self.inp) - 1

        iteration = len(self.inp)
        while iteration < n:
            last_number = 0 if last_index < 0 else iteration - last_index - 1
            last_index = history[last_number]
            history[last_number] = iteration
            iteration += 1
        return last_number


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert RambunctiousRecitation("sample1.txt").whats_nth_spoken_number(2020) == 436
    assert RambunctiousRecitation("sample2.txt").whats_nth_spoken_number(2020) == 1
    assert RambunctiousRecitation("sample3.txt").whats_nth_spoken_number(2020) == 10
    assert RambunctiousRecitation("sample4.txt").whats_nth_spoken_number(2020) == 27
    assert RambunctiousRecitation("sample5.txt").whats_nth_spoken_number(2020) == 78
    assert RambunctiousRecitation("sample6.txt").whats_nth_spoken_number(2020) == 438
    assert RambunctiousRecitation("sample7.txt").whats_nth_spoken_number(2020) == 1836

    assert RambunctiousRecitation("sample1.txt").whats_nth_spoken_number(30000000) == 175594
    assert RambunctiousRecitation("sample2.txt").whats_nth_spoken_number(30000000) == 2578
    assert RambunctiousRecitation("sample3.txt").whats_nth_spoken_number(30000000) == 3544142
    assert RambunctiousRecitation("sample4.txt").whats_nth_spoken_number(30000000) == 261214
    assert RambunctiousRecitation("sample5.txt").whats_nth_spoken_number(30000000) == 6895259
    assert RambunctiousRecitation("sample6.txt").whats_nth_spoken_number(30000000) == 18
    assert RambunctiousRecitation("sample7.txt").whats_nth_spoken_number(30000000) == 362

    print("Tests passed, starting with the puzzle")

    puzzle = RambunctiousRecitation(data.input_file)

    print(puzzle.whats_nth_spoken_number(2020))
    print(puzzle.whats_nth_spoken_number(30000000))
