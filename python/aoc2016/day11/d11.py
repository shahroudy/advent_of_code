import re
from collections import namedtuple
from itertools import combinations
from pathlib import Path
from typing import override

from myutils.io_handler import get_input_data
from myutils.search import Search_BFS

State = namedtuple("State", ["floors", "elevator", "steps"])


class RadioisotopeThermoelectricGenerators(Search_BFS):
    def __init__(self, filename):
        input_text = Path(filename).read_text()
        self.floors = []
        mc_re = re.compile(r"a (\w+)-compatible microchip")
        gen_re = re.compile(r"a (\w+) generator")
        names = ["zero"] + re.findall(mc_re, input_text)
        self.floors = [
            {names.index(gen) for gen in gen_re.findall(line)}
            | {-names.index(mc) for mc in mc_re.findall(line)}
            for line in input_text.splitlines()
        ]
        self.chip_count = len(names) - 1

    def fry(self, floor):
        gens = {item for item in floor if item > 0}
        chips = {-item for item in floor if item < 0}
        return bool(chips - gens and gens)

    @override
    def get_next_states(self, state):
        next_states = []
        elevator_from = state.elevator
        for elevator_move in (-1, 1):
            elevator_to = elevator_from + elevator_move
            if not 0 <= elevator_to < len(state.floors):
                continue
            for moving_items_count in (1, 2):
                for items in combinations(list(state.floors[elevator_from]), moving_items_count):
                    floor_from = state.floors[elevator_to] | set(items)
                    floor_to = state.floors[elevator_from] - set(items)
                    if not (self.fry(floor_from) or self.fry(floor_to)):
                        new_floors = state.floors.copy()
                        new_floors[elevator_from] = floor_to
                        new_floors[elevator_to] = floor_from
                        next_states.append(
                            State(
                                floors=new_floors,
                                elevator=elevator_to,
                                steps=state.steps + 1,
                            )
                        )
        return next_states

    @override
    def is_goal(self, state: State):
        return len(state.floors[-1]) == (self.chip_count * 2)

    @override
    def get_result(self, state):
        return state.steps

    @override
    def state_core(self, state):
        s = []
        for _ in range(self.chip_count):
            s.append([0, 0])
        for i, floor in enumerate(state.floors):
            for item in floor:
                s[abs(item) - 1][0 if item < 0 else 1] = i
        s.sort()
        f = tuple(tuple(ss) for ss in s) + (state.elevator,)
        return f

    @override
    def cost(self, state):
        return state.steps

    def min_number_of_steps(self):
        return self.search(State(floors=self.floors, elevator=0, steps=0))

    def min_number_of_steps_with_extra_parts(self):
        count = self.chip_count
        self.floors[0] |= {count + 1, -count - 1, count + 2, -count - 2}
        self.chip_count += 2
        return self.search(State(floors=self.floors, elevator=0, steps=0))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert RadioisotopeThermoelectricGenerators("sample1.txt").min_number_of_steps() == 11

    print("Tests passed, starting with the puzzle")

    puzzle = RadioisotopeThermoelectricGenerators(data.input_file)

    print(puzzle.min_number_of_steps())
    print(puzzle.min_number_of_steps_with_extra_parts())
