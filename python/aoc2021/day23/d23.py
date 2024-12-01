from functools import reduce
from collections import *
from itertools import *
from pathlib import Path
import heapq as hq


# This script is in draft shape and not refined yet :D


class Amphipod:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.mask4 = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.process_num_map()

    def process_num_map(self):
        self.map = dict()
        row = 0
        for line in self.lines:
            col = 0
            for ch in line:
                if ch in "ABCD.":
                    self.map[(row, col)] = ch
                col += 1
            if row == 0:
                self.cols = col
            col = 0
            row += 1
        self.rows = row - 1

    def available_moves(self, map):
        unitcost = {"A": 1, "B": 10, "C": 100, "D": 1000}
        dmap = []
        for row in range(self.rows):
            ddmap = ""
            for col in range(13):
                if (row, col) in map:
                    ddmap += map[(row, col)]
                else:
                    ddmap += "#"
            dmap.append(ddmap)
        moves = []
        for k, v in map.items():
            if v.isalpha():
                if v == "A" and k[1] == 3:
                    for row in range(k[0], self.rows):
                        if map[(row, 3)] != "A":
                            break
                    else:
                        continue  # it's all As skip
                if v == "B" and k[1] == 5:
                    for row in range(k[0], self.rows):
                        if map[(row, 5)] != "B":
                            break
                    else:
                        continue  # it's all Bs skip
                if v == "C" and k[1] == 7:
                    for row in range(k[0], self.rows):
                        if map[(row, 7)] != "C":
                            break
                    else:
                        continue  # it's all Cs skip
                if v == "D" and k[1] == 9:
                    for row in range(k[0], self.rows):
                        if map[(row, 9)] != "D":
                            break
                    else:
                        continue  # it's all Ds skip
                dists = {k: 0}
                q = deque()
                q.append(k)
                while q:
                    p = q.popleft()
                    steps = dists[p]
                    for n in self.mask4:
                        dest = (p[0] + n[0], p[1] + n[1])
                        if dest not in dists and dest in map and map[dest] == ".":
                            if n[0] == 1:  # moving down one step
                                if dest[1] == 3:
                                    if v != "A":
                                        continue
                                    flag = True
                                    for row in range(2, self.rows):
                                        if map[(row, 3)] not in "A.":
                                            flag = False
                                            break
                                    if not flag:
                                        continue

                                if dest[1] == 5:
                                    if v != "B":
                                        continue
                                    flag = True
                                    for row in range(2, self.rows):
                                        if map[(row, 5)] not in "B.":
                                            flag = False
                                            break
                                    if not flag:
                                        continue

                                if dest[1] == 7:
                                    if v != "C":
                                        continue
                                    flag = True
                                    for row in range(2, self.rows):
                                        if map[(row, 7)] not in "C.":
                                            flag = False
                                            break
                                    if not flag:
                                        continue

                                if dest[1] == 9:
                                    if v != "D":
                                        continue
                                    flag = True
                                    for row in range(2, self.rows):
                                        if map[(row, 9)] not in "D.":
                                            flag = False
                                            break
                                    if not flag:
                                        continue
                            dists[dest] = steps + 1
                            q.append(dest)
                for dest, steps in dists.items():
                    if dest[0] == k[0] == 1:
                        continue
                    if dest[1] == k[1]:
                        continue
                    if dest[1] in (3, 5, 7, 9) and dest[0] == 1:
                        continue
                    if map.get((dest[0] + 1, dest[1]), "#") == ".":
                        continue
                    if dest[0] > 1:
                        flag = True
                        for row in range(dest[0] + 1, self.rows):
                            if map[(row, dest[1])] == ".":
                                flag = False
                                break
                        if not flag:
                            continue
                    newmap = map.copy()
                    newmap[dest] = newmap[k]
                    newmap[k] = "."
                    cost = steps * unitcost[v]
                    desc = ""
                    # desc = v + str(k) + str(dest) + str(cost) + " "
                    moves.append([cost, newmap, desc])
        # moves.sort(key=lambda k: k[0], reverse=True)
        return moves

    def is_solution(self, map):
        for row in range(2, self.rows):
            if (
                map[(row, 3)] != "A"
                or map[(row, 5)] != "B"
                or map[(row, 7)] != "C"
                or map[(row, 9)] != "D"
            ):
                return False
        return True

    def estimated_remaining_cost(self, map):
        dmap = []
        for row in range(self.rows):
            ddmap = ""
            for col in range(13):
                if (row, col) in map:
                    ddmap += map[(row, col)]
                else:
                    ddmap += "#"
            dmap.append(ddmap)

        unitcost = {"A": 1, "B": 10, "C": 100, "D": 1000}
        goal = {"A": 3, "B": 5, "C": 7, "D": 9}
        cost = 0
        for ch, ucost in unitcost.items():
            chsteps = 0
            start = (self.rows - 1, goal[ch])
            q = deque()
            q.append(start)
            dest = {start: 0}
            remain_count = self.rows - 2
            if map[start] == ch:
                remain_count -= 1
            while remain_count:
                p = q.popleft()
                steps = dest[p] + 1
                for n in self.mask4:
                    pn = (p[0] + n[0], p[1] + n[1])
                    if pn not in dest:
                        m = map.get(pn, "#")
                        if m == ch:
                            remain_count -= 1
                            chsteps += steps
                        if m != "#":
                            q.append(pn)
                            dest[pn] = steps
            chsteps -= 6
            cost += chsteps * ucost
        return cost

    def estimated_remaining_cost0(self, map):
        unitcost = {"A": 1, "B": 10, "C": 100, "D": 1000}
        cost = 0
        for k, v in map.items():
            if v.isalpha():
                step = 0
                if k[0] == 1:
                    step = 1
                else:
                    if v == "A" and k[1] != 3:
                        step += k[0]
                    if v == "B" and k[1] != 5:
                        step += k[0]
                    if v == "A" and k[1] != 7:
                        step += k[0]
                    if v == "A" and k[1] != 9:
                        step += k[0]
                if v == "A":
                    step += abs(3 - k[1])
                if v == "B":
                    step += abs(5 - k[1])
                if v == "C":
                    step += abs(7 - k[1])
                if v == "D":
                    step += abs(9 - k[1])
                cost += step * unitcost[v]
        return cost

    def calc_min_energy(self):
        buf = defaultdict(list)

        val = self.estimated_remaining_cost(self.map)
        vals = [val]
        buf[val].append([0, self.map, ""])
        hq.heapify(vals)

        while True:
            val = hq.heappop(vals)
            p = buf[val].pop()

            cost, map, desc = p
            moves = self.available_moves(map)
            for mc, mmap, mdesc in moves:
                fdesc = desc + mdesc
                fc = mc + cost
                if self.is_solution(mmap):
                    print(fdesc)
                    return fc
                else:
                    est = self.estimated_remaining_cost(mmap)
                    newval = est + fc
                    hq.heappush(vals, newval)
                    buf[newval].append([fc, mmap, fdesc])


if __name__ == "__main__":

    test1 = Amphipod("test1.txt")
    assert test1.calc_min_energy() == 12521

    test2 = Amphipod("test2.txt")
    assert test2.calc_min_energy() == 44169

    amphipod1 = Amphipod("input1.txt")
    print(amphipod1.calc_min_energy())

    amphipod2 = Amphipod("input2.txt")
    print(amphipod2.calc_min_energy())
