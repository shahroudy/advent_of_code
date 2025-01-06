import re
from pathlib import Path

from myutils.io_handler import get_input_data


class MonsterMessages:
    def __init__(self, filename):
        rules_txt, inputs_txt = Path(filename).read_text().split("\n\n")
        self.inp = inputs_txt.splitlines()

        self.expressions = {}
        line_re = re.compile(r"(\d+): (.*)")
        for line in rules_txt.splitlines():
            rule_id, rule = line_re.match(line).groups()
            rule_id = int(rule_id)
            if rule.startswith('"'):
                self.expressions[rule_id] = rule.replace('"', "")
                continue
            self.expressions[rule_id] = [list(map(int, term.split())) for term in rule.split(" | ")]

        remaining_ids = set(self.expressions.keys())
        self.re_rules = {}
        for id, rule in self.expressions.items():
            if isinstance(rule, str):
                self.re_rules[id] = rule
                remaining_ids.remove(id)
        while 0 in remaining_ids:
            for id in remaining_ids:
                rule = self.expressions[id]
                if all(all(n in self.re_rules for n in ns) for ns in rule):
                    this_one_rule = []
                    for rule_option in rule:
                        term = "".join(self.re_rules[n] for n in rule_option)
                        this_one_rule.append(f"({term})")
                    self.re_rules[id] = "(" + "|".join(this_one_rule) + ")"
                    break
            remaining_ids.remove(id)

    def count_matching_simple(self):
        root_rule = re.compile(f"^{self.re_rules[0]}$")
        return sum(bool(root_rule.match(t)) for t in self.inp)

    def count_matching_looped(self):
        re_rule_8 = f"({self.re_rules[42]})+"
        r11 = []
        for i in range(1, 5):
            r11.append(f"({self.re_rules[42]}){{{i}}}({self.re_rules[31]}){{{i}}}")
        re_rule_11 = "(" + "|".join(r11) + ")"
        re_rule_0 = f"({re_rule_8})({re_rule_11})"
        root_rule = re.compile(f"^{re_rule_0}$")
        return sum(bool(root_rule.match(t)) for t in self.inp)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert MonsterMessages("sample1.txt").count_matching_simple() == 2
    assert MonsterMessages("sample2.txt").count_matching_simple() == 3
    assert MonsterMessages("sample2.txt").count_matching_looped() == 12

    print("Tests passed, starting with the puzzle")

    puzzle = MonsterMessages(data.input_file)

    print(puzzle.count_matching_simple())
    print(puzzle.count_matching_looped())
