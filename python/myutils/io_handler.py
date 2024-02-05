import os
import re
from collections import namedtuple
from pathlib import Path

from aocd import get_data, submit

AoCData = namedtuple("AoCData", ["year", "day", "input_file"])


def get_input_data(filename: str):
    file_parts = filename.split("/")
    day = int(re.search(r"\d+", file_parts[-2]).group(0))
    year = int(re.search(r"\d+", file_parts[-3]).group(0))

    input_file = f'{os.environ.get("aoc_inputs")}/aoc{year}_day{day:02}.txt'
    if not Path(input_file).exists() or len(Path(input_file).read_text()) == 0:
        Path(input_file).write_text(get_data(day=day, year=year))
    return AoCData(year, day, input_file)


def submit_answer(answer, part: str, data: AoCData):
    print(f"Submitting answer for part {part} of AoC ({data.year}/{data.day}): {answer}")
    submit(answer, part=part, day=data.day, year=data.year)
