import os
from collections import deque
from functools import cmp_to_key, reduce

from myutils.file_reader import read_line_groups


class DistressSignal:
    def __init__(self, filename):
        self.signals = [[eval(pair[0]), eval(pair[1])] for pair in read_line_groups(filename)]

    def compare(self, left, right):
        if isinstance(left, int) and isinstance(right, int):
            return left - right
        leftQ = deque([left]) if isinstance(left, int) else deque(left)
        rightQ = deque([right]) if isinstance(right, int) else deque(right)
        while rightQ:
            if not leftQ:
                return -1
            left_item = leftQ.popleft()
            right_item = rightQ.popleft()
            comparison = self.compare(left_item, right_item)
            if comparison:
                return comparison
        if leftQ:
            return 1
        return 0

    def sum_of_right_ordered_signals(self):
        return sum([i + 1 for i, signals in enumerate(self.signals) if self.compare(*signals) < 0])

    def decoder_key(self):
        dividers = [[[2]], [[6]]]
        q = [signal for signals in self.signals for signal in signals]
        q.extend(dividers)
        q.sort(key=cmp_to_key(self.compare))
        return reduce(lambda a, b: a * b, [1 + q.index(d) for d in dividers])


def test_samples(filename, answer1, answer2):
    test = DistressSignal(filename)
    assert test.sum_of_right_ordered_signals() == answer1
    assert test.decoder_key() == answer2


if __name__ == "__main__":

    test_samples("sample1.txt", 13, 140)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day13.txt'
    puzzle = DistressSignal(input_file)
    print(puzzle.sum_of_right_ordered_signals())
    print(puzzle.decoder_key())
