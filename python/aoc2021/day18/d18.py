import os
from pathlib import Path


class Snailfish:
    def __init__(self, input=None):
        if not input:
            self.sequence = []
        elif isinstance(input, list):
            self.sequence = input.copy()
        else:
            self.snailfishes = Path(input).read_text().strip().split("\n")

    def append(self, sequence):
        self.sequence = sequence if not self.sequence else [self.sequence, sequence]

    def transmit(self, s, value, direction):
        if isinstance(s[direction], int):
            s[direction] += value
        else:
            self.transmit(s[direction], value, direction)

    def explode_recursive(self, s, depth=0):
        if isinstance(s, int):
            return None
        if depth == 4:
            self.exploded = True
            return s
        for i in [0, 1]:
            if self.exploded:
                return None
            if isinstance(s[i], list):
                parts = self.explode_recursive(s[i], depth + 1)
                if parts:
                    if depth == 3:
                        s[i] = 0
                    if isinstance(s[1 - i], int):
                        s[1 - i] += parts[1 - i]
                        parts[1 - i] = 0
                    else:
                        self.transmit(s[1 - i], parts[1 - i], i)
                        parts[1 - i] = 0
                    return parts

    def explode(self, input=None):
        if input:
            self.sequence = input
        self.exploded = False
        self.explode_recursive(self.sequence)
        return self.sequence

    def split_recursive(self, s):
        for i in [0, 1]:
            if self.splitted:
                return
            if isinstance(s[i], int):
                if s[i] > 9:
                    left = s[i] // 2
                    right = s[i] - left
                    self.splitted = True
                    s[i] = [left, right]
                    return
            else:
                self.split_recursive(s[i])

    def split(self):
        self.splitted = False
        self.split_recursive(self.sequence)
        return self.sequence

    def reduce(self):
        while True:
            self.explode()
            if self.exploded:
                continue
            self.split()
            if self.splitted:
                continue
            return self.sequence

    def magnitude_recursive(self, s):
        if isinstance(s, int):
            return s
        else:
            return self.magnitude_recursive(s[0]) * 3 + self.magnitude_recursive(s[1]) * 2

    def magnitude(self):
        return self.magnitude_recursive(self.sequence)

    def reduce_lines(self):
        self.snailsum = Snailfish()
        for snailfish_str in self.snailfishes:
            self.snailsum.append(eval(snailfish_str))
            self.snailsum.reduce()
        return self.snailsum.sequence

    def final_sum_magnitude(self):
        self.reduce_lines()
        return self.snailsum.magnitude()

    def max_pairwise_sum_magnitude(self):
        max_magnitude = 0
        for snailfish1 in self.snailfishes:
            for snailfish2 in self.snailfishes:
                if snailfish1 == snailfish2:
                    continue
                snailsum = Snailfish([eval(snailfish1), eval(snailfish2)])
                snailsum.reduce()
                max_magnitude = max(max_magnitude, snailsum.magnitude())
        return max_magnitude


if __name__ == "__main__":

    # Test Explode Funcion
    assert Snailfish([[[[[9, 8], 1], 2], 3], 4]).explode() == [
        [[[0, 9], 2], 3],
        4,
    ]
    assert Snailfish([7, [6, [5, [4, [3, 2]]]]]).explode() == [
        7,
        [6, [5, [7, 0]]],
    ]
    assert Snailfish([[6, [5, [4, [3, 2]]]], 1]).explode() == [
        [6, [5, [7, 0]]],
        3,
    ]
    assert Snailfish([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]).explode() == [
        [3, [2, [8, 0]]],
        [9, [5, [4, [3, 2]]]],
    ]
    assert Snailfish([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]).explode() == [
        [3, [2, [8, 0]]],
        [9, [5, [7, 0]]],
    ]

    # Test Reduce Function
    assert Snailfish([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]).reduce() == [
        [[[0, 7], 4], [[7, 8], [6, 0]]],
        [8, 1],
    ]

    assert Snailfish("test1.txt").reduce_lines() == [
        [[[1, 1], [2, 2]], [3, 3]],
        [4, 4],
    ]

    assert Snailfish("test2.txt").reduce_lines() == [
        [[[3, 0], [5, 3]], [4, 4]],
        [5, 5],
    ]

    assert Snailfish("test3.txt").reduce_lines() == [
        [[[5, 0], [7, 4]], [5, 5]],
        [6, 6],
    ]

    assert Snailfish("test4.txt").reduce_lines() == [
        [[[8, 7], [7, 7]], [[8, 6], [7, 7]]],
        [[[0, 7], [6, 6]], [8, 7]],
    ]

    # Test Magnitude Function
    assert Snailfish([9, 1]).magnitude() == 29
    assert Snailfish([[9, 1], [1, 9]]).magnitude() == 129
    assert Snailfish([[1, 2], [[3, 4], 5]]).magnitude() == 143
    assert Snailfish([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]).magnitude() == 1384
    assert Snailfish([[[[1, 1], [2, 2]], [3, 3]], [4, 4]]).magnitude() == 445
    assert Snailfish([[[[3, 0], [5, 3]], [4, 4]], [5, 5]]).magnitude() == 791
    assert Snailfish([[[[5, 0], [7, 4]], [5, 5]], [6, 6]]).magnitude() == 1137
    assert (
        Snailfish([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]).magnitude()
        == 3488
    )

    # Test Example Homework
    test5 = Snailfish("test5.txt")
    assert test5.reduce_lines() == [
        [[[6, 6], [7, 6]], [[7, 7], [7, 0]]],
        [[[7, 7], [7, 7]], [[7, 8], [9, 9]]],
    ]
    assert test5.final_sum_magnitude() == 4140
    assert test5.max_pairwise_sum_magnitude() == 3993

    # Solve the Puzzle Input
    input_file = f'{os.environ.get("aoc_inputs")}/aoc2021_day18.txt'
    snailfish = Snailfish(input_file)
    print(snailfish.final_sum_magnitude())
    print(snailfish.max_pairwise_sum_magnitude())
