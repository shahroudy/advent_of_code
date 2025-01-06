import re
from pathlib import Path

from myutils.grammar import count_matching_inputs
from myutils.io_handler import get_input_data


class MonsterMessages:
    def __init__(self, filename):
        rules_txt, inputs_txt = Path(filename).read_text().split("\n\n")
        self.inp = inputs_txt.splitlines()
        self.grammar = re.sub(r"(\d+)", r"t\1", rules_txt)

    def count_matching_simple(self):
        return count_matching_inputs(self.grammar, "t0", self.inp)

    def count_matching_looped(self):
        rules = [r for r in self.grammar.splitlines() if "t8:" not in r and "t11:" not in r]
        rules.extend(["t8: t42 | t42 t8", "t11: t42 t31 | t42 t11 t31"])
        rules = "\n".join(rules)
        return count_matching_inputs(rules, "t0", self.inp)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert MonsterMessages("sample1.txt").count_matching_simple() == 2
    assert MonsterMessages("sample2.txt").count_matching_simple() == 3
    assert MonsterMessages("sample2.txt").count_matching_looped() == 12

    print("Tests passed, starting with the puzzle")

    puzzle = MonsterMessages(data.input_file)

    print(puzzle.count_matching_simple())
    print(puzzle.count_matching_looped())
