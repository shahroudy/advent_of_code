import re
from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class BalanceBots:
    def __init__(self, filename, search_values={61, 17}):
        self.process_input(filename)
        self.simulate(search_values)

    def process_input(self, filename):
        self.bot_microchips = defaultdict(list)
        self.bot_outputs = {}
        for line in Path(filename).read_text().splitlines():
            if m := re.match(r"value (\d+) goes to (.+)", line):
                self.bot_microchips[m.group(2)].append(int(m.group(1)))
            elif m := re.match(r"(.+) gives low to (.+) and high to (.+)", line):
                self.bot_outputs[m.group(1)] = m.group(2, 3)

    def simulate(self, search_values={61, 17}):
        self.searched_bot = None
        ready_bots = [b for b, chips in self.bot_microchips.items() if len(chips) == 2]
        while ready_bots:
            bot = ready_bots.pop()
            chips = self.bot_microchips[bot]
            if self.searched_bot is None and search_values == set(chips):
                self.searched_bot = int(bot.split()[1])
            for out_bot, microchip in zip(self.bot_outputs[bot], sorted(chips)):
                self.bot_microchips[out_bot].append(microchip)
                if len(self.bot_microchips[out_bot]) == 2:
                    ready_bots.append(out_bot)
            self.bot_microchips[bot].clear()
        self.final_output = 1
        for bin in ["output 0", "output 1", "output 2"]:
            self.final_output *= self.bot_microchips[bin][0]


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert BalanceBots("sample1.txt", {2, 5}).searched_bot == 2
    assert BalanceBots("sample1.txt", {2, 3}).searched_bot == 1
    assert BalanceBots("sample1.txt", {3, 5}).searched_bot == 0

    print("Tests passed, starting with the puzzle")

    puzzle = BalanceBots(data.input_file)

    print(puzzle.searched_bot)
    print(puzzle.final_output)
