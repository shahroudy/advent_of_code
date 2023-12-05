import os
from pathlib import Path


class MonkeyMap:
    def __init__(self, filename):
        lines = Path(filename).read_text().rstrip().split("\n")
        self.map = dict()
        for row, line in enumerate(lines):
            if len(line) == 0:
                break
            for col, ch in enumerate(line):
                if ch in "#.":
                    self.map[(col, row)] = ch

        moves_line = lines[-1]
        self.moves = []
        head = 0
        while head < len(moves_line):
            ch = moves_line[head]
            if ch.isnumeric():
                n = 0
                while head < len(moves_line) and moves_line[head].isnumeric():
                    n = n * 10 + int(moves_line[head])
                    head += 1
                self.moves.append(n)
            else:
                self.moves.append(ch)
                head += 1

        self.directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def reset(self):
        self.xy = (min([p[0] for p, v in self.map.items() if p[1] == 0 and v == "."]), 0)
        self.dir = 0

    def wrap_2d(self, nxy, dir):
        match dir:
            case 0:  # R
                nxy = (min([p[0] for p in self.map if p[1] == nxy[1]]), nxy[1])
            case 1:  # D
                nxy = (nxy[0], min([p[1] for p in self.map if p[0] == nxy[0]]))
            case 2:  # L
                nxy = (max([p[0] for p in self.map if p[1] == nxy[1]]), nxy[1])
            case 3:  # U
                nxy = (nxy[0], max([p[1] for p in self.map if p[0] == nxy[0]]))
        return nxy, dir

    def wrap_3d(self, nxy, dir):
        x, y = nxy
        match dir:
            case 0:  # R
                match x:
                    case 150:
                        return (99, 149 - y), 2
                    case 100:
                        if y < 100:
                            return (50 + y, 49), 3
                        else:
                            return (149, 149 - y), 2
                    case 50:
                        return (y - 100, 149), 3
            case 1:  # D
                match y:
                    case 50:
                        return (99, x - 50), 2
                    case 150:
                        return (49, x + 100), 2
                    case 200:
                        return (x + 100, 0), 1
            case 2:  # L
                match x:
                    case -1:
                        if y < 150:
                            return (50, 149 - y), 0
                        else:
                            return (y - 100, 0), 1
                    case 49:
                        if y < 50:
                            return (0, 149 - y), 0
                        else:
                            return (y - 50, 100), 1
            case 3:  # U
                if x < 50:
                    return (50, 50 + x), 0
                elif x < 100:
                    return (0, 100 + x), 0
                else:
                    return (x - 100, 199), 3

    def move(self, n, simple_wrap):
        if isinstance(n, int):
            xy = self.xy
            dir = self.dir
            for _ in range(n):
                ndir = dir
                nxy = tuple([xy[i] + self.directions[ndir][i] for i in (0, 1)])

                if nxy not in self.map:
                    nxy, ndir = self.wrap_2d(nxy, ndir) if simple_wrap else self.wrap_3d(nxy, ndir)

                if self.map[nxy] == ".":
                    xy = nxy
                    dir = ndir
                else:
                    break
            self.xy, self.dir = xy, dir
        else:
            self.dir = (self.dir + (1 if n == "R" else -1)) % 4

    def final_password(self, simple_wrap=True):
        self.reset()
        for move in self.moves:
            self.move(move, simple_wrap)
        return 1000 * (self.xy[1] + 1) + 4 * (self.xy[0] + 1) + self.dir


def test_samples(filename, answer):
    test = MonkeyMap(filename)
    assert test.final_password() == answer


if __name__ == "__main__":

    test_samples("sample1.txt", 6032)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day22.txt'
    puzzle = MonkeyMap(input_file)
    print(puzzle.final_password())
    print(puzzle.final_password(simple_wrap=False))
