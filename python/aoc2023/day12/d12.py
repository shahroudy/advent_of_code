import os
import re
from functools import cache
from pathlib import Path
from myutils.io_handler import get_input_data


class HotSprings:
    def __init__(self, filename):
        self.condition_records = []
        for line in Path(filename).read_text().strip().splitlines():
            parts = line.split()
            self.condition_records.append([parts[0], list(map(int, parts[1].strip().split(",")))])

    @cache
    def how_many_ways(self, numbers, records):
        if len(numbers) == 0:  # the only way to match is to have no #s and set all ?s as dots
            if any(["#" in record for record in records]):
                return 0
            else:
                return 1
        if len(records) == 0:  # no more records to match, but we still have numbers
            return 0

        record, rest_records = records[0], records[1:]
        number, rest_numbers = numbers[0], numbers[1:]

        if "#" not in record:  # all ?s
            ways = self.how_many_ways(numbers, rest_records)  # consider it as all dots
            if len(record) == number:  # match it
                ways += self.how_many_ways(rest_numbers, rest_records)
            elif len(record) > number:
                ways += self.how_many_ways(rest_numbers, rest_records) * 2
                for i in range(len(record) - number - 1, 0, -1):
                    rem_group_0 = record[-i:]
                    ways += self.how_many_ways(rest_numbers, (rem_group_0,) + rest_records)
            return ways

        ways = 0
        if record[0] == "?":
            if len(record) == 1:
                ways += self.how_many_ways(numbers, rest_records)
            else:
                ways += self.how_many_ways(numbers, (record[1:],) + rest_records)

        first_question_mark_index = record.find("?")

        if first_question_mark_index < 0:  # not question marks in this group
            if number == len(record):
                ways += self.how_many_ways(rest_numbers, rest_records)
            return ways

        if first_question_mark_index > number:  # we cannot match anymore
            return ways

        if first_question_mark_index == number:
            rem_group_0 = record[first_question_mark_index + 1 :]
            if len(rem_group_0) > 0:
                ways += self.how_many_ways(rest_numbers, (rem_group_0,) + rest_records)
            else:
                ways += self.how_many_ways(rest_numbers, rest_records)
            return ways

        if first_question_mark_index < number:
            if len(record) == number:
                ways += self.how_many_ways(rest_numbers, rest_records)
                return ways
            if len(record) > number:
                if record[number] == "#":
                    return ways
                # it's ?
                rem_group_0 = record[number + 1 :]
                if len(rem_group_0) > 0:
                    ways += self.how_many_ways(rest_numbers, (rem_group_0,) + rest_records)
                else:
                    ways += self.how_many_ways(rest_numbers, rest_records)
        return ways

    def sum_of_different_arrangements(self, rep=1):
        return sum(
            [
                self.how_many_ways(
                    tuple(numbers * rep),
                    tuple(re.findall(r"[#,?]+", (code + "?") * (rep - 1) + code)),
                )
                for code, numbers in self.condition_records
            ]
        )


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = HotSprings(filename)
    assert answer1 is None or test.sum_of_different_arrangements() == answer1
    assert answer2 is None or test.sum_of_different_arrangements(rep=5) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 1, 1)
    test_samples("sample2.txt", 4, 16384)
    test_samples("sample3.txt", 1, 1)
    test_samples("sample4.txt", 1, 16)
    test_samples("sample5.txt", 4, 2500)
    test_samples("sample6.txt", 10, 506250)

    print("Tests passed, starting with the puzzle")

    puzzle = HotSprings(data.input_file)
    print(puzzle.sum_of_different_arrangements())
    print(puzzle.sum_of_different_arrangements(rep=5))
