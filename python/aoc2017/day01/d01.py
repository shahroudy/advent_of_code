import os
from pathlib import Path
from myutils.io_handler import get_input_data


class InverseCaptcha:
    def __init__(self, filename):
        txt = Path(filename).read_text().strip()
        self.inp = list(map(int, list(txt)))

    def captcha_solution(self, shift=1):
        sum = 0
        for i in range(len(self.inp)):
            if self.inp[i] == self.inp[(i + shift) % len(self.inp)]:
                sum += self.inp[i]
        return sum

    def solve_with_next_item(self):
        return self.captcha_solution(1)

    def solve_with_halfway_around(self):
        return self.captcha_solution(len(self.inp) // 2)


def test_samples(filename, answer1, answer2):
    test = InverseCaptcha(filename)
    assert answer1 is None or test.solve_with_next_item() == answer1
    assert answer2 is None or test.solve_with_halfway_around() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 3, None)
    test_samples("sample2.txt", 4, None)
    test_samples("sample3.txt", None, 0)
    test_samples("sample4.txt", None, 4)
    test_samples("sample5.txt", None, 12)
    test_samples("sample6.txt", None, 4)

    print("Tests passed, starting with the puzzle")

    puzzle = InverseCaptcha(data.input_file)
    print(puzzle.solve_with_next_item())
    print(puzzle.solve_with_halfway_around())
