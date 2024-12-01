import os

from myutils.file_reader import read_lines
from myutils.io_handler import get_input_data


class FFT:
    def __init__(self, filename, repeat_code=1, apply_offset=False):
        self.init_code = list(map(int, list(read_lines(filename)[0]))) * repeat_code
        self.code_size = len(self.init_code)
        self.ignore_size = int("".join(map(str, self.init_code[:7]))) if apply_offset else 0

    def calculate_digit(self, digit_no):
        head = digit_no
        total = 0
        factor = 1
        while head < len(self.code):
            tail = min(head + digit_no + 1, self.code_size)
            total += factor * sum(self.code[head:tail])
            head = tail + digit_no + 1
            factor *= -1
        mod = total % 10
        if total < 0 and mod != 0:
            mod = 10 - mod
        return mod

    def fft_step(self):
        new_code = [0] * self.code_size
        digit = self.ignore_size
        while digit < self.code_size:
            new_code[digit] = self.calculate_digit(digit)
            digit += 1
        self.code = new_code

    def fft_step_heuristic(self):
        new_code = [0] * self.code_size
        digit = self.ignore_size
        total = sum(self.code[digit:])
        while digit < self.code_size:
            new_code[digit] = total % 10
            total -= self.code[digit]
            digit += 1
        self.code = new_code

    def process(self, steps=100):
        self.code = self.init_code.copy()
        for _ in range(steps):
            if not self.ignore_size:
                self.fft_step()
            else:
                self.fft_step_heuristic()
        return "".join(map(str, self.code[self.ignore_size : 8 + self.ignore_size]))


class FFT_Efficient:
    def __init__(self, filename, repeat_code=10000):
        code = list(map(int, list(read_lines(filename)[0])))
        codelen = len(code)
        ignore_size = int("".join(map(str, code[:7])))
        full_size = len(code) * repeat_code - ignore_size
        self.code = code[codelen - (full_size % codelen) :] + code * (full_size // codelen)

    def process(self, steps=100):
        for _ in range(steps):
            total = 0
            for index in reversed(range(len(self.code))):
                total += self.code[index]
                self.code[index] = total % 10
        return "".join(map(str, self.code[:8]))


if __name__ == "__main__":
    data = get_input_data(__file__)
    fft1 = FFT("test1.txt")
    assert fft1.process(4) == "01029498"
    fft2 = FFT("test2.txt")
    assert fft2.process() == "24176176"
    fft3 = FFT("test3.txt")
    assert fft3.process() == "73745418"
    fft4 = FFT("test4.txt")
    assert fft4.process() == "52432133"

    fft5 = FFT("test5.txt", 10000, True)
    assert fft5.process() == "84462026"
    fft6 = FFT("test6.txt", 10000, True)
    assert fft6.process() == "78725270"
    fft7 = FFT("test7.txt", 10000, True)
    assert fft7.process() == "53553731"

    fft = FFT(data.input_file)
    print(fft.process())
    fft = FFT(input_file, 10000, True)
    print(fft.process())
    fft = FFT_Efficient(data.input_file)
    print(fft.process())
