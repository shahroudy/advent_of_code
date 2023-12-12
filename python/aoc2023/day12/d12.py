import os
from functools import cache
from pathlib import Path


class HotSprings:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().splitlines()
        self.inp = []
        for line in self.lines:
            parts = line.split()
            ns = list(map(int, parts[1].strip().split(",")))
            self.inp.append([parts[0], ns])

    @cache
    def how_many_ways(self, numbers, groups):
        if len(numbers) == 0:
            for g in groups:
                if "#" in g:
                    break
            else:
                return 1
            return 0
        if len(groups) == 0:
            return 0

        if "#" not in groups[0]:  # all ?s
            ways = self.how_many_ways(numbers, groups[1:])  # consider it as all dots
            if len(groups[0]) < numbers[0]:
                return ways
            elif len(groups[0]) == numbers[0]:  # match it
                ways += self.how_many_ways(
                    numbers[1:],
                    groups[1:],
                )
                return ways
            else:
                ways += self.how_many_ways(numbers[1:], groups[1:]) * 2
                for i in range(len(groups[0]) - numbers[0] - 1, 0, -1):
                    rem_group_0 = groups[0][-i:]
                    ways += self.how_many_ways(numbers[1:], (rem_group_0,) + groups[1:])
            return ways

        ways = 0
        if groups[0][0] == "?":
            if len(groups[0]) == 1:
                ways += self.how_many_ways(numbers, groups[1:])
            else:
                ways += self.how_many_ways(numbers, (groups[0][1:],) + groups[1:])

        first_question_mark_index = groups[0].find("?")

        if first_question_mark_index < 0:  # not question marks in this group
            if numbers[0] == len(groups[0]):
                ways += self.how_many_ways(numbers[1:], groups[1:])
            return ways

        if first_question_mark_index > numbers[0]:  # we cannot match anymore
            return ways

        if first_question_mark_index == numbers[0]:
            rem_group_0 = groups[0][first_question_mark_index + 1 :]
            if len(rem_group_0) > 0:
                ways += self.how_many_ways(numbers[1:], (rem_group_0,) + groups[1:])
            else:
                ways += self.how_many_ways(numbers[1:], groups[1:])
            return ways

        if first_question_mark_index < numbers[0]:
            if len(groups[0]) == numbers[0]:
                ways += self.how_many_ways(numbers[1:], groups[1:])
                return ways
            if len(groups[0]) > numbers[0]:
                if groups[0][numbers[0]] == "#":
                    return ways
                # it's ?
                rem_group_0 = groups[0][numbers[0] + 1 :]
                if len(rem_group_0) > 0:
                    ways += self.how_many_ways(numbers[1:], (rem_group_0,) + groups[1:])
                else:
                    ways += self.how_many_ways(numbers[1:], groups[1:])
        return ways

    def sum_of_different_arrangements(self, rep=1):
        result = 0
        for code, numbers in self.inp:
            if rep > 1:
                ccc = list(code)
                ccc.append("?")
                ccc = ccc * (rep - 1)
                ccc.extend(code)
                code = "".join(ccc)
                numbers = numbers * rep

            groups = []
            history = ""
            for ch in code:
                if ch == ".":
                    if len(history) > 0:
                        groups.append(history)
                        history = ""
                else:
                    history += ch
            else:
                if len(history) > 0:
                    groups.append(history)

            result += self.how_many_ways(tuple(numbers), tuple(groups))
        return result


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = HotSprings(filename)
    assert answer1 is None or test.sum_of_different_arrangements() == answer1
    assert answer2 is None or test.sum_of_different_arrangements(rep=5) == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 1, 1)
    test_samples("sample2.txt", 4, 16384)
    test_samples("sample3.txt", 1, 1)
    test_samples("sample4.txt", 1, 16)
    test_samples("sample5.txt", 4, 2500)
    test_samples("sample6.txt", 10, 506250)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day12.txt'
    puzzle = HotSprings(input_file)
    print(puzzle.sum_of_different_arrangements())
    print(puzzle.sum_of_different_arrangements(rep=5))
