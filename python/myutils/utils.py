import operator
import re
from collections import defaultdict, namedtuple
from functools import reduce

from myutils.exrange import ExRange
from myutils.geometry import *
from myutils.geometry import Point, Point3D


def multiply(elements):
    return reduce(operator.mul, elements, 1)


def process(text: str):
    lines = text.splitlines()
    inp = []

    # inp = [tuple(map(int, re.split(r"\D", line))) for line in lines]

    # line_re = re.compile(r"(\d+)\s*(\d+):(\d+).*")
    for line in lines:
        # parts = line_re.match(line).groups()
        parts = re.split(r"-, ", line)
        # a = parts[0].strip().split(" ")
        # a = list(map(int, re.findall(r"\d+", parts[0])))
        inp.append(parts)
    return inp


def recursive_split(text, separators, strip=True):
    if strip:
        text = text.strip()
    if not separators:
        return text
    separator, future_separators = separators[0], separators[1:]
    return [recursive_split(x, future_separators, strip) for x in text.split(separator)]


def find_all_re(pattern, text=None):
    pattern = re.compile(pattern)
    return pattern.findall(text)


def find_all_per_line_re(pattern, text=None):
    pattern = re.compile(pattern)
    return [pattern.findall(line) for line in text.splitlines()]


def read_plain_map(text):
    lines = text.splitlines()
    char_map = dict()
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            char_map[Point(col, row)] = ch
    return char_map, row + 1, col + 1


def read_map_of_digits(text):
    char_map, rows, cols = read_plain_map(text)
    int_map = {k: int(v) for k, v in char_map.items()}
    return int_map, rows, cols


def read_map_dict_of_sets_of_points(text):
    lines = text.splitlines()
    sets = defaultdict(set)
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            sets[ch].add(Point(col, row))
    return dict(sets), row + 1, col + 1


def read_map_dict_of_sets_of_3D_points(text):
    sets = defaultdict(set)
    for z, plane in enumerate(text.split("\n\n")):
        for y, line in enumerate(plane.splitlines()):
            for x, ch in enumerate(line):
                sets[ch].add(Point3D(x, y, z))
    return dict(sets), z + 1, y + 1, x + 1


def read_ints(text: str):
    return [int(n) for n in re.findall(r"[+-]?\d+", text)]


def read_line_groups(text: str):
    return [re.split("\n", g) for g in re.split("\n\n", text.strip())]


def read_int_line_groups(text: str):
    return [[int(n) for n in re.split("\n", g)] for g in re.split("\n\n", text.strip())]


def process_int_list(text: str):
    lines = text.splitlines()
    return [list(map(int, re.findall(r"-?\d+", line))) for line in lines]


def process_int_int_dict(text: str):
    lines = text.splitlines()
    inp = {}
    for line in lines:
        parts = list(map(int, re.findall(r"-?\d+", line)))
        inp[parts[0]] = parts[1:]
    return inp


def process_int_list_dict(text: str):
    lines = text.splitlines()
    inp = {}
    for line in lines:
        parts = list(map(int, re.findall(r"-?\d+", line)))
        inp[parts[0]] = parts[1:]
    return inp


def read_ranges(text: str, range_sep="\n", bounds_sep="-", end_inclusive=True):
    ranges = ExRange()
    for line in text.split(range_sep):
        a, b = map(int, line.split(bounds_sep))
        if end_inclusive:
            b += 1
        ranges.add(range(a, b))
    return ranges


def print_with_color(self, text, text_color="#FFFFFF", back_color="#000000", end="\n"):
    from colored import attr, bg, fg

    color = fg(text_color)
    back = bg(back_color)
    reset = attr("reset")
    print(f"{color + back}" + text + f"{reset}", end=end)


def get_sample_number(filename):
    number = re.match(r"sample(\d+).txt", filename)
    if number:
        return int(number.group(1))
    return 0  # actual input file, not a sample test


# Example usage
assert multiply([1, 2, 3, 4, 5]) == 120
