import os
import re
from copy import deepcopy
from math import lcm
from pathlib import Path
from myutils.io_handler import get_input_data


class MonkeyInTheMiddle:
    def __init__(self, filename):
        self.init_state = []
        self.monkeys = []

        for lines in [
            re.split("\n", g) for g in re.split("\n\n", Path(filename).read_text().strip())
        ]:
            items = [int(i) for i in re.split(r", ", lines[1][18:])]
            operation = lines[2].split("=")[-1]
            divisor = int(lines[3].split()[-1])
            if_monkey = int(lines[4].split()[-1])
            else_monkey = int(lines[5].split()[-1])
            self.init_state.append(items)
            self.monkeys.append([operation, divisor, if_monkey, else_monkey])

    def reset_state(self):
        self.state = deepcopy(self.init_state)
        self.inspect = [0 for _ in range(len(self.monkeys))]

    def throw_items(self, worry_update):
        for monkey, (operation, divisor, if_monkey, else_monkey) in enumerate(self.monkeys):
            while self.state[monkey]:
                worry_level = self.state[monkey].pop()
                worry_level = worry_update(eval(operation, {"old": worry_level}))
                to_monkey = if_monkey if (worry_level % divisor == 0) else else_monkey
                self.state[to_monkey].append(worry_level)
                self.inspect[monkey] += 1

    def level_of_monkey_business(self, iterations, worry_update_fun):
        self.reset_state()
        for _ in range(iterations):
            self.throw_items(worry_update_fun)
        self.inspect.sort(reverse=True)
        return self.inspect[0] * self.inspect[1]

    def monkey_business(self, relief=True):
        if relief:
            return self.level_of_monkey_business(20, lambda w: w // 3)
        else:
            least_common_multiple = lcm(*[m[1] for m in self.monkeys])
            return self.level_of_monkey_business(10000, lambda w: w % least_common_multiple)


def test_samples(filename, answer1, answer2):
    test = MonkeyInTheMiddle(filename)
    assert test.monkey_business() == answer1
    assert test.monkey_business(relief=False) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 10605, 2713310158)

    monkey_in_the_middle = MonkeyInTheMiddle(data.input_file)
    print(monkey_in_the_middle.monkey_business())
    print(monkey_in_the_middle.monkey_business(relief=False))
