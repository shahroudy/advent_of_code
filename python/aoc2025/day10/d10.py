import re
from collections import namedtuple
from pathlib import Path

import numpy as np
from myutils.io_handler import get_input_data
from myutils.optimization import solve_int_ls_min_sum
from myutils.search import Search_BFS


class MySearch(Search_BFS):
    State = namedtuple("state", ["indicator", "pushes"])

    def get_next_states(self, state):
        for button in self.buttons:
            yield self.State([sum(v) % 2 for v in zip(state.indicator, button)], state.pushes + 1)

    def is_goal(self, state):
        return state.indicator == self.goal_state

    def get_result(self, state):
        return state.pushes

    def state_core(self, state):
        return tuple(state.indicator)


class Factory:
    def __init__(self, filename):
        self.machines = []
        line_re = re.compile(
            r"""
            ^\[(?P<indicator_lights>[.#]+)\]
            (?P<buttons>(?:\s+\((?:\d+(?:,\d+)*)\))+)\s+
            \{(?P<joltage_requirements>\d+(?:,\d+)*)\}$
            """,
            re.VERBOSE | re.MULTILINE,
        )
        button_re = re.compile(r"\((\d+(?:,\d+)*)\)")

        for machine in line_re.finditer(Path(filename).read_text()):
            indicator_lights = [1 if ch == "#" else 0 for ch in machine.group("indicator_lights")]
            buttons = [
                [list(map(int, button.split(","))).count(i) for i in range(len(indicator_lights))]
                for button in button_re.findall(machine.group("buttons"))
            ]
            joltage_requirements = list(map(int, machine.group("joltage_requirements").split(",")))
            self.machines.append([indicator_lights, buttons, joltage_requirements])

    def configure_the_indicator_lights(self):
        total_pushes = 0
        for goal_state, buttons, _ in self.machines:
            total_pushes += MySearch(
                buttons=buttons,
                initial_state=MySearch.State([0 for _ in goal_state], 0),
                goal_state=goal_state,
            ).search()
        return total_pushes

    def configure_the_joltage(self):
        total_pushes = 0
        for _, buttons, joltage_requirements in self.machines:
            A = np.asarray(buttons, dtype=float).T
            b = np.asarray(joltage_requirements, dtype=float)
            x = solve_int_ls_min_sum(A, b)
            total_pushes += int(np.sum(x))
        return total_pushes


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Factory("sample1.txt").configure_the_indicator_lights() == 7
    assert Factory("sample1.txt").configure_the_joltage() == 33

    print("Tests passed, starting with the puzzle")

    puzzle = Factory(data.input_file)

    print(puzzle.configure_the_indicator_lights())
    print(puzzle.configure_the_joltage())
