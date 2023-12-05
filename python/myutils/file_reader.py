from pathlib import Path
import re


def read_str_list(filename):
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.extend(line.strip().split(","))
        return lines


def read_int_list(filename):
    return [int(s) for s in read_str_list(filename)]


def read_float_list(filename):
    return [float(s) for s in read_str_list(filename)]


def read_lines(filename):
    return Path(filename).read_text().strip().split("\n")


def read_int_lines(filename):
    return [int(line) for line in read_lines(filename)]


def read_line_groups(filename):
    return [re.split("\n", g) for g in re.split("\n\n", Path(filename).read_text().strip())]


def read_int_line_groups(filename):
    return [
        [int(n) for n in re.split("\n", g)]
        for g in re.split("\n\n", Path(filename).read_text().strip())
    ]
