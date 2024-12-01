import os
from myutils.file_reader import read_line_groups
from myutils.io_handler import get_input_data


class SubterraneanSustainability:
    def __init__(self, filename):
        self.line_groups = read_line_groups(filename)
        self.process()

    def process(self):
        self.state = {n for n, c in enumerate(self.line_groups[0][0].split()[-1]) if c == "#"}
        self.rules = {line.split()[0] for line in self.line_groups[1] if line[-1] == "#"}

    def sum_of_planted_pots(self, generations=20):
        state = self.state
        delta_sum = 0
        for gen in range(generations):
            new_state = set()
            for i in range(min(state) - 4, max(state) + 5):
                w = "".join(["#" if (i + j) in state else "." for j in range(-2, 3)])
                if w in self.rules:
                    new_state.add(i)
            new_delta_sum = sum(new_state) - sum(state)
            if new_delta_sum == delta_sum:
                # after few iterations the sum grows linerly!
                return (generations - gen) * delta_sum + sum(state)
            else:
                state, delta_sum = new_state, new_delta_sum
        return sum(state)


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = SubterraneanSustainability("test1.txt")
    assert test1.sum_of_planted_pots() == 325

    ss = SubterraneanSustainability(data.input_file)
    print(ss.sum_of_planted_pots())
    print(ss.sum_of_planted_pots(50000000000))
