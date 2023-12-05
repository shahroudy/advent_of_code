import os
# import re
from itertools import combinations
from pathlib import Path

# This code is the brute force solution for day16 and is in draft mode
# Some improvements/refatorings are on the way :)


class Puzzle:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.process()

    def process(self):

        self.rate = {}
        self.tuns = {}
        self.valves = set()

        # line_re = re.compile(r"Valve (.+) has flow rate=(.+); [\w+] [\w+] to [\w+] (.+)")
        for line in self.lines:
            # parts = line_re.match(line).groups()
            parts = line.split(";")
            p0 = parts[0].split()
            p1 = parts[1].split()
            name = p0[1]
            fr = int(p0[4].split("=")[1])
            tun = p1[4:]
            tun = [t.replace(",", "") for t in tun]
            self.rate[name] = fr
            self.tuns[name] = tun
            self.valves.add(name)

        self.dist = {}
        for s in self.valves:
            q = [s]
            d = {s: 0}
            rem = self.valves - {s}
            while rem and q:
                new_q = []
                for c in q:
                    for n in self.tuns[c]:
                        if n not in d:
                            new_q.append(n)
                            d[n] = d[c] + 1
                            rem.remove(n)
                q = new_q
            for k, v in d.items():
                if k != s:
                    self.dist[s, k] = v

    def calc1(self):
        rate = self.rate
        dist = self.dist
        vv = {v for v in self.valves if rate[v] > 0}
        cur = "AA"
        stack = []
        best_val = 0
        for v in vv:
            remtime = 30 - dist[cur, v] - 1
            if remtime > 0:
                stack.append([[v], remtime, remtime * rate[v]])

        while stack:
            state = stack.pop()
            path, remtime, sumpres = state
            cur = path[-1]
            for v in vv - set(path):
                new_remtime = remtime - dist[cur, v] - 1
                if remtime > 0:
                    new_path = path + [v]
                    new_sumpres = sumpres + new_remtime * rate[v]
                    new_state = [new_path, new_remtime, new_sumpres]
                    if new_sumpres > best_val:
                        best_val = new_sumpres
                    stack.append(new_state)
        return best_val

    def calc2(self):
        rate = self.rate
        dist = self.dist
        valid_valves = {v for v in self.valves if rate[v] > 0}
        current_valve = "AA"
        stack = []
        best_val = 0
        for c in combinations(valid_valves, 2):
            v1, v2 = c
            remtime1 = 26 - dist[current_valve, v1] - 1
            remtime2 = 26 - dist[current_valve, v2] - 1
            sumpres1 = remtime1 * rate[v1]
            sumpres2 = remtime2 * rate[v2]
            state = [[v1], [v2], remtime1, remtime2, sumpres1, sumpres2]
            if remtime1 > 0 and remtime2 > 0:
                stack.append(state)

        stack.sort(key=lambda v: v[-1] + v[-2])
        iter = 1
        while stack:
            state = stack.pop()
            new_states = []
            visited = state[0] + state[1]
            for v in valid_valves - set(visited):
                path1, path2, remtime1, remtime2, sumpres1, sumpres2 = state.copy()
                current_valve1 = path1[-1]
                current_valve2 = path2[-1]
                new_remtime1 = remtime1 - dist[current_valve1, v] - 1
                new_remtime2 = remtime2 - dist[current_valve2, v] - 1
                if new_remtime1 > 0:
                    new_sumpres1 = sumpres1 + new_remtime1 * rate[v]
                    new_state = [
                        path1 + [v],
                        path2.copy(),
                        new_remtime1,
                        remtime2,
                        new_sumpres1,
                        sumpres2,
                    ]
                    val = sum(new_state[-2:])
                    if val > best_val:
                        best_val = val
                        best_sol = new_state
                    new_states.append(new_state)
                if new_remtime2 > 0:
                    new_sumpres2 = sumpres2 + new_remtime2 * rate[v]
                    new_state = [
                        path1.copy(),
                        path2 + [v],
                        remtime1,
                        new_remtime2,
                        sumpres1,
                        new_sumpres2,
                    ]
                    val = sum(new_state[-2:])
                    if val > best_val:
                        best_val = val
                        best_sol = new_state
                    new_states.append(new_state)
            new_states.sort(key=lambda v: v[-1] + v[-2])
            stack.extend(new_states)
            iter += 1
            if iter % 1000000 == 0:
                print(f"so far: {best_val}")

            # stack.sort(key=lambda v: v[-1] + v[-2])
        print(best_sol)
        return best_val

    def calc02(self):
        rate = self.rate
        dist = self.dist
        valid_valves = {v for v in self.valves if rate[v] > 0}
        current_valve = "AA"
        stack = []
        best_val = 0
        for c in combinations(valid_valves, 2):
            v1, v2 = c
            if dist[current_valve, v1] > dist[current_valve, v2]:
                v1, v2 = v2, v1
            path = [v1, v2]
            remtime1 = 26 - dist[current_valve, v1] - 1
            remtime2 = 26 - dist[current_valve, v2] - 1
            sumpres1 = remtime1 * rate[v1]
            sumpres2 = remtime2 * rate[v2]
            state = [path, remtime1, remtime2, sumpres1, sumpres2]
            stack.append(state)

        # stack.sort(key=lambda v: v[-1] + v[-2])
        iter = 1
        while stack:

            state = stack.pop()
            new_states = []
            path1 = state[0]
            for v in valid_valves - set(path1):
                path, remtime1, remtime2, sumpres1, sumpres2 = state.copy()
                current_valve = path[-2]
                v1 = path[-1]
                v2 = v
                new_remtime = remtime1 - dist[current_valve, v2] - 1
                if new_remtime <= 0:
                    current_valve = path[-1]
                    v2 = v
                    new_remtime = remtime2 - dist[current_valve, v2] - 1
                    if new_remtime <= 0:
                        continue
                    sumpres2 = sumpres2 + new_remtime * rate[v2]
                    new_state = [path + [v2], remtime2, new_remtime, sumpres1, sumpres2]
                    # print("koskesh")
                else:
                    remtime1, remtime2 = remtime2, new_remtime
                    sumpres1, sumpres2 = sumpres2, sumpres1 + remtime2 * rate[v2]
                    if remtime1 < remtime2:
                        remtime1, remtime2 = remtime2, remtime1
                        v1, v2 = v2, v1
                        sumpres1, sumpres2 = sumpres2, sumpres1
                    new_state = [path[:-1] + [v1, v2], remtime1, remtime2, sumpres1, sumpres2]
                    if sumpres1 + sumpres2 > best_val:
                        best_val = sumpres1 + sumpres2
                        best_sol = new_state
                    new_states.append(new_state)
            # new_states.sort(key=lambda v: v[-1] + v[-2])
            stack.extend(new_states)
            iter += 1
            if iter % 1000000 == 0:
                print(f"so far: {best_val}")

            # stack.sort(key=lambda v: v[-1] + v[-2])
        print(best_sol)
        return best_val


if __name__ == "__main__":

    test1 = Puzzle("test1.txt")
    assert test1.calc1() == 1651
    assert test1.calc2() == 1707

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day16.txt'
    puzzle = Puzzle(input_file)
    print(puzzle.calc1())
    print(puzzle.calc2())

# [['XC', 'HH', 'FL', 'DW', 'UK', 'OL', 'WV'], ['RP', 'SU', 'XD', 'TE', 'YP', 'FQ'], 2, 7, 1262, 1513]
