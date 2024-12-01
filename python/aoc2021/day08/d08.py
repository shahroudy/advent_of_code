import os
from collections import defaultdict
from myutils.file_reader import read_lines


class SevenSegmentSearch:
    def __init__(self, filename):
        self.lines = read_lines(filename)
        self.process()

    def process(self):
        self.inp = []
        self.out = []
        for line in self.lines:
            parts = line.split("|")
            self.inp.append(parts[0].split())
            self.out.append(parts[1].split())

        self.seven_seg_digit = {
            "abcefg": 0,
            "cf": 1,
            "acdeg": 2,
            "acdfg": 3,
            "bcdf": 4,
            "abdfg": 5,
            "abdefg": 6,
            "acf": 7,
            "abcdefg": 8,
            "abcdfg": 9,
        }

    def count_simple_digits(self):
        count = 0
        for output_line in self.out:
            for word in output_line:
                if len(word) in [2, 3, 4, 7]:
                    count += 1
        return count

    def find_segment_matching(self, words):
        codes = defaultdict(list)
        chars = defaultdict(set)
        match = dict()

        for w in words:
            codes[len(w)].append(w)
            chars[len(w)].update(set(w))

        match["a"] = chars[3] & chars[7] & chars[6] & chars[5] - chars[2] - chars[4]
        match["g"] = chars[5] & chars[6] & chars[7] - chars[2] - chars[3] - chars[4]
        match["e"] = chars[7] - chars[4]
        match["b"] = chars[4] & chars[6] - chars[2] - chars[3]
        match["d"] = chars[5] & chars[4] - chars[2] - chars[3]
        f = chars[2]
        for w in codes[6]:
            f = f & set(w)
        match["f"] = f
        match["c"] = chars[2] - match["f"]

        for w in codes[5]:
            for fm in match["f"]:
                if fm in w:
                    match["e"] -= set(w)

        for w in codes[5]:
            for am in match["c"]:
                if am in w:
                    match["b"] -= set(w)

        for ch in list("abcef"):
            match["g"] -= match[ch]
            match["d"] -= match[ch]

        reverse_match = dict()
        for key, value in match.items():
            assert len(value) == 1
            reverse_match[value.pop()] = key
        return reverse_match

    def calc_full_matching_result(self):
        result = 0
        for index in range(len(self.inp)):
            words = self.inp[index] + self.out[index]
            seg_matching = self.find_segment_matching(words)

            number = 0
            for word in self.out[index]:
                mapped_word_list = [seg_matching[ch] for ch in word]
                mapped_word = "".join(sorted(mapped_word_list))
                digit = self.seven_seg_digit[mapped_word]
                number = number * 10 + int(digit)
            result += number

        return result


if __name__ == "__main__":
    test2 = SevenSegmentSearch("test2.txt")
    assert test2.count_simple_digits() == 26
    assert test2.calc_full_matching_result() == 61229

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2021_day08.txt'
    seven_segment_search = SevenSegmentSearch(input_file)
    print(seven_segment_search.count_simple_digits())
    print(seven_segment_search.calc_full_matching_result())
