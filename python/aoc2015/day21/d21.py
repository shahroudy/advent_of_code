import re
from itertools import combinations, product
from pathlib import Path

from myutils.io_handler import get_input_data


class RPGSimulator20XX:
    def __init__(self, filename=None):
        input = """Weapons:    Cost  Damage  Armor
                   Dagger        8     4       0
                   Shortsword   10     5       0
                   Warhammer    25     6       0
                   Longsword    40     7       0
                   Greataxe     74     8       0

                   Armor:      Cost  Damage  Armor
                   Leather      13     0       1
                   Chainmail    31     0       2
                   Splintmail   53     0       3
                   Bandedmail   75     0       4
                   Platemail   102     0       5

                   Rings:      Cost  Damage  Armor
                   Damage +1    25     1       0
                   Damage +2    50     2       0
                   Damage +3   100     3       0
                   Defense +1   20     0       1
                   Defense +2   40     0       2
                   Defense +3   80     0       3"""
        items = [
            [list(map(int, re.findall(r"\d+", line)))[-3:] for line in group.splitlines()[1:]]
            for group in input.split("\n\n")
        ]
        if filename:
            self.boss = list(map(int, re.findall(r"\d+", Path(filename).read_text())))
            self.process(items)

    def process(self, items):
        weapons, armors, rings = items
        possible_weapons = weapons
        possible_armors = armors + [[0, 0, 0]]
        possible_rings = [[0, 0, 0]] + [
            [sum(rings[j][i] for j in ring_comb) for i in range(3)]
            for ring_count in range(1, 3)
            for ring_comb in combinations(range(len(rings)), ring_count)
        ]
        self.min_winning_cost, self.max_losing_cost = float("inf"), 0
        for cur in product(possible_weapons, possible_armors, possible_rings):
            cost, damage, armor = [sum(cur[j][i] for j in range(3)) for i in range(3)]
            if self.min_winning_cost <= cost <= self.max_losing_cost:
                continue
            if self.fight(100, damage, armor, *self.boss):
                self.min_winning_cost = min(self.min_winning_cost, cost)
            else:
                self.max_losing_cost = max(self.max_losing_cost, cost)

    def fight(self, player_hit, player_damage, player_armor, boss_hit, boss_damage, boss_armor):
        boss_lives = boss_hit // max(1, player_damage - boss_armor)
        player_lives = player_hit // max(1, boss_damage - player_armor)
        return player_lives >= boss_lives


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert RPGSimulator20XX().fight(8, 5, 5, 12, 7, 2)

    print("Tests passed, starting with the puzzle")

    puzzle = RPGSimulator20XX(data.input_file)

    print(puzzle.min_winning_cost)
    print(puzzle.max_losing_cost)
