from collections import defaultdict
from functools import reduce
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import recursive_split


class SevenSegmentSearch:
    def __init__(self, filename):
        self.input = recursive_split(Path(filename).read_text(), "\n| ", strip=True)
        self.segments = {
            0: "abcefg",
            1: "cf",
            2: "acdeg",
            3: "acdfg",
            4: "bcdf",
            5: "abdfg",
            6: "abdefg",
            7: "acf",
            8: "abcdefg",
            9: "abcdfg",
        }

    def count_simple_digits(self):
        return sum(len(word) in [2, 3, 4, 7] for line in self.input for word in line[1])

    def sum_of_all_output_values(self):
        sum = 0
        for input, output in self.input:
            match = self.find_matching((input + output))
            sum += self.sum_of_outputs_for_matching(output, match)
        return sum

    def find_matching(self, words):
        segments_of_size = defaultdict(list)
        for word in words:
            segments_of_size[len(word)].append(word)
        chars = {
            length: reduce(set.intersection, map(set, words))
            for length, words in segments_of_size.items()
        }
        match = {
            "a": chars[3] - chars[2],
            "b": chars[6] - chars[5] - chars[2],
            "c": chars[2] - chars[6],
            "d": chars[4] & chars[5],
            "e": chars[7] - chars[6] - chars[5] - chars[2],
            "f": chars[2] & chars[6],
            "g": chars[5] & chars[6] - chars[3],
        }
        assert all(len(value) == 1 for value in match.values())
        return {char: list(matches)[0] for char, matches in match.items()}

    def sum_of_outputs_for_matching(self, words, matching):
        dd = {"".join(sorted([matching[c] for c in v])): k for k, v in self.segments.items()}
        n = 0
        for encoded_word in words:
            word = "".join(sorted(encoded_word))
            n = n * 10 + dd[word]
        return n


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert SevenSegmentSearch("sample2.txt").count_simple_digits() == 26
    assert SevenSegmentSearch("sample1.txt").sum_of_all_output_values() == 5353
    assert SevenSegmentSearch("sample2.txt").sum_of_all_output_values() == 61229

    print("Tests passed, starting with the puzzle")

    puzzle = SevenSegmentSearch(data.input_file)

    print(puzzle.count_simple_digits())
    print(puzzle.sum_of_all_output_values())
