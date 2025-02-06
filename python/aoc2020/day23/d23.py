from pathlib import Path

from myutils.io_handler import get_input_data


class CrabCups:
    def __init__(self, filename):
        self.cups = list(map(int, Path(filename).read_text().strip()))

    def move(self, next, start, iterations):
        max_val = max(next.keys())
        current = start
        for _ in range(iterations):
            first = next[current]
            second = next[first]
            third = next[second]
            fourth = next[third]
            dest = current - 1 if current > 1 else max_val
            removed = {first, second, third}
            while dest in removed:
                dest = dest - 1 if dest > 1 else max_val
            next[current], next[dest], next[third] = fourth, first, next[dest]
            current = next[current]

    def crab_mix_simple(self, iterations=100):
        next = {i: j for i, j in zip(self.cups, self.cups[1:] + self.cups[:1])}
        self.move(next, self.cups[0], iterations)
        res, cur = 0, next[1]
        while cur != 1:
            res = res * 10 + cur
            cur = next[cur]
        return res

    def crab_mix_many(self):
        next = {i: j for i, j in zip(self.cups[:-1], self.cups[1:])}
        m = max(self.cups) + 1
        next.update({i: i + 1 for i in range(m, 1000000)})
        next.update({self.cups[-1]: m, 1000000: self.cups[0]})
        self.move(next, self.cups[0], 10000000)
        return next[1] * next[next[1]]


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert CrabCups("sample1.txt").crab_mix_simple(10) == 92658374
    assert CrabCups("sample1.txt").crab_mix_simple() == 67384529
    assert CrabCups("sample1.txt").crab_mix_many() == 149245887792

    puzzle = CrabCups(data.input_file)

    print(puzzle.crab_mix_simple())
    print(puzzle.crab_mix_many())
