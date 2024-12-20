import re
from collections import defaultdict
from functools import cache
from itertools import permutations, product
from pathlib import Path

from myutils.geometry import DIR_CHARS, Point
from myutils.io_handler import get_input_data


class KeypadConundrum:
    def __init__(self, filename):
        self.door_codes = Path(filename).read_text().splitlines()

        ph_kb = ["789", "456", "123", " 0A"]
        d_kb = [" ^A", "<v>"]
        self.ph_kp = {c: Point(x, y) for y, row in enumerate(ph_kb) for x, c in enumerate(row)}
        self.dir_kp = {c: Point(x, y) for y, line in enumerate(d_kb) for x, c in enumerate(line)}

    @cache
    def move_ph(self, current_1, new_1):
        current = self.ph_kp[current_1] + (0, 0)
        new = self.ph_kp[new_1] + (0, 0)
        moves = []
        while new.x > current.x:
            moves.append(">")
            current.x += 1
        while new.x < current.x:
            moves.append("<")
            current.x -= 1
        while new.y > current.y:
            moves.append("v")
            current.y += 1
        while new.y < current.y:
            moves.append("^")
            current.y -= 1

        per = set(permutations(moves))
        moves = []
        for p in per:
            current = self.ph_kp[current_1] + (0, 0)
            valid = True
            for ch in p:
                current = current + DIR_CHARS[ch]
                if current == Point(0, 3):
                    valid = False
                    break
            if valid:
                moves.append("".join(p) + "A")
        return moves

    @cache
    def moves_in_dir_kb(self, current_1, new_1):
        current = self.dir_kp[current_1] + (0, 0)
        new = self.dir_kp[new_1] + (0, 0)
        return current.manhattan_dist(new)

    @cache
    def move_dir(self, current_1, new_1):
        current = self.dir_kp[current_1] + (0, 0)
        new = self.dir_kp[new_1] + (0, 0)
        moves = []
        while new.x > current.x:
            moves.append(">")
            current.x += 1
        while new.x < current.x:
            moves.append("<")
            current.x -= 1
        while new.y > current.y:
            moves.append("v")
            current.y += 1
        while new.y < current.y:
            moves.append("^")
            current.y -= 1

        per = set(permutations(moves))
        moves = []
        for p in per:
            current = self.dir_kp[current_1] + (0, 0)
            valid = True
            for ch in p:
                current = current + DIR_CHARS[ch]
                if current == Point(0, 0):
                    valid = False
                    break
            if valid:
                moves.append("".join(p) + "A")

        proper = defaultdict(set)
        min_possible = float("inf")
        for m in moves:
            length = sum(self.moves_in_dir_kb(a, b) for a, b in zip(m[:-1], m[1:]))
            proper[length].add(m)
            min_possible = min(min_possible, length)
        return proper[min_possible]

    def key_in_dir_keyboard(self, text):
        if isinstance(text, str):
            atext = "A" + text
            s = [a + b for a, b in zip(atext[:-1], atext[1:])]
            d = defaultdict(int)
            for p in s:
                d[p] += 1
        else:
            d = text

        result1 = defaultdict(int)
        result2 = defaultdict(int)
        for k, v in d.items():
            moves = list(self.move_dir(k[0], k[1]).copy())

            atext = "A" + moves[0]
            s = [a + b for a, b in zip(atext[:-1], atext[1:])]
            for p in s:
                result1[p] += v

            atext = ("A" + moves[1]) if len(moves) > 1 else ("A" + moves[0])
            s = [a + b for a, b in zip(atext[:-1], atext[1:])]
            for p in s:
                result2[p] += v
        return result1, result2

    def sum_of_complexities(self, iterations=2):
        res = 0
        for text in self.door_codes:
            c1 = "A"
            m1 = {""}
            for ch in text:
                possible = set()
                for m, mm in product(m1, self.move_ph(c1, ch)):
                    possible.add(m + mm)
                c1 = ch
                m1 = possible
            for _ in range(iterations):
                ds = [dict(d) for m in m1 for d in self.key_in_dir_keyboard(m)]
                min_size = min(sum(d.values()) for d in ds)
                m1 = [d for d in ds if sum(d.values()) == min_size]
            res += min_size * int(re.findall(r"(\d+)", text)[0])

        return res


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert KeypadConundrum("sample1.txt").sum_of_complexities(2) == 68 * 29
    assert KeypadConundrum("sample2.txt").sum_of_complexities(2) == 60 * 980
    assert KeypadConundrum("sample3.txt").sum_of_complexities(2) == 68 * 179
    assert KeypadConundrum("sample4.txt").sum_of_complexities(2) == 64 * 456
    assert KeypadConundrum("sample5.txt").sum_of_complexities(2) == 64 * 379
    assert KeypadConundrum("sample6.txt").sum_of_complexities(2) == 126384

    print("Tests passed, starting with the puzzle")

    puzzle = KeypadConundrum(data.input_file)

    assert puzzle.sum_of_complexities(2) == 222670
    assert puzzle.sum_of_complexities(25) == 271397390297138

    print(puzzle.sum_of_complexities(2))
    print(puzzle.sum_of_complexities(25))
