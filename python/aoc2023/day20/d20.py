import os
import re
from collections import defaultdict, deque
from itertools import chain
from math import lcm
from pathlib import Path
from myutils.io_handler import get_input_data


class PulsePropagation:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().splitlines()
        self.process()
        self.simulate()

    def process(self):
        self.outs = {}
        self.types = {}
        self.source = defaultdict(list)
        self.conjunction = defaultdict(dict)
        self.flipflops = {}

        line_re = re.compile(r"([%&]?)(\w+)\s*->\s*(.*)")
        for line in self.lines:
            sign, name, outs = line_re.match(line).groups()
            outs = [out.strip() for out in outs.split(",")]
            self.outs[name] = outs
            self.types[name] = sign
            for out in outs:
                self.source[out].append(name)
                self.conjunction[out][name] = False
            if sign == "%":
                self.flipflops[name] = False
        self.signals = deque()
        self.pulse_count = [0, 0]

    def push_signal(self, name, pulse, sender):
        self.signals.append((name, pulse, sender))
        self.pulse_count[pulse] += 1

    def pop_signal(self):
        return self.signals.popleft()

    def simulate(self):
        # It seems rx is only receiving signals from a conjunction module (layer-1)
        # which also receives signals from a set of other conjunction modules (layer-2)
        # which all in turn receive signals from a set of other conjunction modules (layer-3)
        # Good news is that all the layer-3 conjunction modules are getting activated in a regular
        # pattern, so we can simulate the whole thing and find the activation time for rx.
        # To do so, we need to find the activation time for all the layer-3 conjunction modules and
        # find the least common multiple of those times.
        activators = ["rx"]
        for _ in range(3):
            activators = list(chain(*[self.source[a] for a in activators]))

        periods = {}
        iter = 0
        while True:
            iter += 1
            self.push_signal("broadcaster", False, "button")

            while self.signals:
                signal = self.pop_signal()
                name, pulse, sender = signal
                if name not in self.types:
                    continue
                if self.types[name] == "%":  # flipflop
                    if not pulse:
                        out_pulse = self.flipflops[name] = not self.flipflops[name]
                    else:
                        continue
                elif self.types[name] == "&":  # conjunction
                    self.conjunction[name][sender] = pulse
                    low_pulse = all(self.conjunction[name].values())
                    out_pulse = not low_pulse
                    if low_pulse and name not in periods:
                        periods[name] = iter
                elif self.types[name] == "":  # broadcaster
                    out_pulse = pulse
                for out in self.outs[name]:
                    self.push_signal(out, out_pulse, name)
            if iter == 1000:
                self.lmh = self.pulse_count[False] * self.pulse_count[True]
                if len(activators) == 0:
                    return
            if activators and all(r in periods for r in activators):
                self.rx_activated = lcm(*periods.values())
                return


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = PulsePropagation(filename)
    assert answer1 is None or test.lmh == answer1
    assert answer2 is None or test.rx_activated == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 32000000, None)
    test_samples("sample2.txt", 11687500, None)

    print("Tests passed, starting with the puzzle")

    puzzle = PulsePropagation(data.input_file)

    print(puzzle.lmh)
    print(puzzle.rx_activated)
