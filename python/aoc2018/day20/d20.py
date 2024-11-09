from pathlib import Path

from myutils.io_handler import get_input_data


class ARegularMap:
    def __init__(self, filename):
        self.directions = {"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1)}
        self.path = Path(filename).read_text().strip()
        self.pass_through_doors()

    def pass_through_doors(self):
        cur = (0, 0)
        stack = []
        dist = {(0, 0): 0}
        for ch in self.path:
            if ch in self.directions:
                dx, dy = self.directions[ch]
                next = (cur[0] + dx, cur[1] + dy)
                dist[next] = min(dist[next], dist[cur] + 1) if next in dist else dist[cur] + 1
                cur = next
            elif ch == "(":
                stack.append(cur)
            elif ch == "|":
                cur = stack[-1]
            elif ch == ")":
                cur = stack.pop()

        self.calc1 = max(dist.values())
        self.calc2 = sum(d >= 1000 for d in dist.values())


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ARegularMap("sample1.txt").calc1 == 3
    assert ARegularMap("sample2.txt").calc1 == 10
    assert ARegularMap("sample3.txt").calc1 == 18
    assert ARegularMap("sample4.txt").calc1 == 23
    assert ARegularMap("sample5.txt").calc1 == 31

    print("Tests passed, starting with the puzzle")

    puzzle = ARegularMap(data.input_file)

    print(puzzle.calc1)
    print(puzzle.calc2)
