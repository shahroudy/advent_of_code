import re
from pathlib import Path

from myutils.io_handler import get_input_data


class PassportProcessing:
    def __init__(self, filename):
        self.passports = [g for g in re.split("\n\n", Path(filename).read_text().strip())]

    def passports_with_required_fields(self):
        needed = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        return sum(needed <= set(re.findall(r"(\w+):\S+", group)) for group in self.passports)

    def fully_valid_passports(self):
        valid_count = 0
        for passport in self.passports:
            passport_dict = {k: v for k, v in re.findall(r"(\w+):(\S+)", passport)}
            try:
                if not (1920 <= int(passport_dict["byr"]) <= 2002):
                    continue
                if not (2010 <= int(passport_dict["iyr"]) <= 2020):
                    continue
                if not (2020 <= int(passport_dict["eyr"]) <= 2030):
                    continue
                height = passport_dict["hgt"]
                if height.endswith("cm"):
                    if not (150 <= int(height[:-2]) <= 193):
                        continue
                elif height.endswith("in"):
                    if not (59 <= int(height[:-2]) <= 76):
                        continue
                else:
                    continue
                if not re.match(r"^#[0-9a-f]{6}$", passport_dict["hcl"]):
                    continue
                if not passport_dict["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                    continue
                if not re.match(r"^\d{9}$", passport_dict["pid"]):
                    continue
                valid_count += 1
            except Exception:
                continue
        return valid_count


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert PassportProcessing("sample1.txt").passports_with_required_fields() == 2
    assert PassportProcessing("sample2.txt").fully_valid_passports() == 0
    assert PassportProcessing("sample3.txt").fully_valid_passports() == 4

    print("Tests passed, starting with the puzzle")

    puzzle = PassportProcessing(data.input_file)

    print(puzzle.passports_with_required_fields())
    print(puzzle.fully_valid_passports())
