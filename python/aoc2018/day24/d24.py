import re
from collections import namedtuple
from copy import deepcopy
from itertools import count
from pathlib import Path

from myutils.io_handler import get_input_data

Group = namedtuple("Group", ["id", "cnt", "hit", "wkn", "imn", "atk", "dmg", "ini"])


class ImmuneSystemSimulator20XX:
    def __init__(self, filename):
        line_groups = Path(filename).read_text().split("\n\n")
        line_re = re.compile(
            r"(\d+) units each with (\d+) hit points ?(.*?) with an attack "
            r"that does (\d+) (\w+) damage at initiative (\d+)"
        )
        self.inp = []
        for id, line_group in enumerate(line_groups):
            for line in line_group.splitlines()[1:]:
                cnt, hit_point, wkn_imn, atk, dmg, ini = line_re.match(line).groups()
                wkn = []
                imn = []
                for w in wkn_imn[1:-1].split("; "):
                    if w.startswith("weak to "):
                        wkn = w[8:].split(", ")
                    elif w.startswith("immune to "):
                        imn = w[10:].split(", ")
                group = Group(id, int(cnt), int(hit_point), wkn, imn, int(atk), dmg, int(ini))
                self.inp.append(group)

    def fight(self, armies):
        units = [a.cnt for a in armies]
        any_attack_happened = True
        while any_attack_happened:
            any_attack_happened = False
            selection_order = sorted(
                range(len(armies)),
                key=lambda i: (units[i] * armies[i].atk, armies[i].ini),
                reverse=True,
            )
            effective_power = {i: units[i] * a.atk for i, a in enumerate(armies)}

            # target selection
            targets = {}
            picked_targets = set()
            for i in selection_order:
                if units[i] == 0:
                    continue
                army = armies[i]
                damage_factor = []
                for j, defending in enumerate(armies):
                    if j in picked_targets or units[j] == 0:
                        continue
                    if army.id == defending.id or army.dmg in defending.imn:
                        continue
                    factor = 2 if army.dmg in defending.wkn else 1
                    damage_factor.append((factor, effective_power[j], defending.ini, j))
                if damage_factor:
                    factor, _, _, target = max(damage_factor)
                    targets[i] = (target, factor)
                    picked_targets.add(target)

            # attacking
            attacking_order = [i for i in range(len(armies)) if units[i] > 0]
            for i in sorted(attacking_order, key=lambda i: armies[i].ini, reverse=True):
                army = armies[i]
                if i not in targets:
                    continue
                target, factor = targets[i]
                if units_killed := (factor * units[i] * army.atk) // armies[target].hit:
                    any_attack_happened = True
                    units[target] = max(0, units[target] - units_killed)
        return units

    def unit_count_of_winner(self):
        return sum(self.fight(deepcopy(self.inp)))

    def unit_count_with_min_boost(self):
        for boost in count(0):
            armies = []
            for a in self.inp:
                boosted_attack = a.atk + boost if a.id == 0 else a.atk
                armies.append(Group(a.id, a.cnt, a.hit, a.wkn, a.imn, boosted_attack, a.dmg, a.ini))
            units = self.fight(armies)
            alive_groups = [i for i in range(len(armies)) if units[i] > 0]
            if all(armies[j].id == 0 for j in alive_groups):
                return sum(units)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = ImmuneSystemSimulator20XX(filename)
    assert answer1 is None or test.unit_count_of_winner() == answer1
    assert answer2 is None or test.unit_count_with_min_boost() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ImmuneSystemSimulator20XX("sample1.txt").unit_count_of_winner() == 5216
    assert ImmuneSystemSimulator20XX("sample1.txt").unit_count_with_min_boost() == 51

    print("Tests passed, starting with the puzzle")

    puzzle = ImmuneSystemSimulator20XX(data.input_file)

    print(puzzle.unit_count_of_winner())
    print(puzzle.unit_count_with_min_boost())
