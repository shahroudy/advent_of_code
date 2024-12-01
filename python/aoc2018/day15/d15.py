import os
from itertools import count
from pathlib import Path
from myutils.io_handler import get_input_data


class BeverageBandits:
    def __init__(self, filename):
        self.init_map = dict()
        for row, line in enumerate(Path(filename).read_text().splitlines()):
            for col, ch in enumerate(line):
                self.init_map[row, col] = ch

    def adjacent(self, p):
        return [(p[0] + d[0], p[1] + d[1]) for d in [[-1, 0], [0, -1], [0, 1], [1, 0]]]

    def step_towards_enemy(self, unit, enemies, live_map):
        visited = {unit}
        queue = [unit]
        pre = {unit: None}
        while queue:
            next_queue = []
            for cur in queue:
                for next in self.adjacent(cur):
                    if next in enemies:
                        while cur is not None and pre[cur] != unit:
                            cur = pre[cur]
                        return cur
                    if live_map[next] == "." and next not in visited:
                        visited.add(next)
                        next_queue.append(next)
                        pre[next] = cur
            queue = next_queue

    def find_target(self, unit, enemies):
        if targets := {p for p in self.adjacent(unit) if p in enemies}:
            return sorted(targets, key=lambda p: (enemies[p], p))[0]

    def run_battle(self, attack_power=3, let_elves_die=True):
        elves = {p: 200 for p, code in self.init_map.items() if code == "E"}
        goblins = {p: 200 for p, code in self.init_map.items() if code == "G"}
        live_map = self.init_map.copy()
        for round_counter in count():
            units_to_move = sorted(elves.keys() | goblins.keys(), reverse=True)
            while units_to_move:
                unit = units_to_move.pop()
                unit_side = live_map[unit]
                allies, enemies = (elves, goblins) if unit_side == "E" else (goblins, elves)
                if len(enemies) == 0:  # combat is over
                    return round_counter * sum(allies.values())
                # move (if not in range)
                if (next := self.step_towards_enemy(unit, enemies, live_map)) is not None:
                    live_map[unit], live_map[next] = ".", live_map[unit]
                    allies[next] = allies.pop(unit)
                    unit = next
                # attack (if in range)
                if (target := self.find_target(unit, enemies)) is not None:
                    enemies[target] -= attack_power if unit_side == "E" else 3
                    if enemies[target] <= 0:
                        if unit_side == "G" and not let_elves_die:
                            return
                        live_map[target] = "."
                        enemies.pop(target)
                        if target in units_to_move:
                            units_to_move.remove(target)

    def run_flawless_battle_with_minimum_attack_power(self):
        for attack_power in count(4):
            if (res := self.run_battle(attack_power=attack_power, let_elves_die=False)) is not None:
                return res


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = BeverageBandits(filename)
    assert answer1 is None or test.run_battle() == answer1
    assert answer2 is None or test.run_flawless_battle_with_minimum_attack_power() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 27730, 4988)
    test_samples("sample2.txt", 36334, None)
    test_samples("sample3.txt", 39514, 31284)
    test_samples("sample4.txt", 27755, 3478)
    test_samples("sample5.txt", 28944, 6474)
    test_samples("sample6.txt", 18740, 1140)

    print("Tests passed, starting with the puzzle")

    puzzle = BeverageBandits(data.input_file)
    print(puzzle.run_battle())
    print(puzzle.run_flawless_battle_with_minimum_attack_power())
