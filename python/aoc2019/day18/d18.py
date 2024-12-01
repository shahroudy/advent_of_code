import os
from collections import defaultdict, deque
from myutils.file_reader import read_lines


class ManyWorldsInterpretation:
    def __init__(self, filename):
        self.lines = read_lines(filename)
        self.process()

    def process(self):
        self.map = defaultdict(lambda: "#")
        self.keys = {}
        row = self.vault_counter = 0
        for line in self.lines:
            col = 0
            for ch in line:
                if ch == "@":
                    ch = str(self.vault_counter)
                    self.vault_counter += 1
                if ch.islower() or ch.isnumeric():
                    self.keys[ch] = (col, row)
                self.map[(col, row)] = ch
                col += 1
            col = 0
            row += 1
        return

    def min_distance_and_obstacles(self, src_key, dest_key):
        # start a breadth first search to find the minimum distance
        if src_key == dest_key:
            return 0, set(), set()

        mask = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque()
        dist = {}
        locks_between = {}
        keys_between = {}

        start_point = self.keys[src_key]
        queue.append(start_point)
        dist[start_point] = 0
        locks_between[start_point] = set()
        keys_between[start_point] = set()

        while queue:
            current_point = queue.popleft()
            current_dist = dist[current_point]
            current_locks = locks_between[current_point]
            current_keys = keys_between[current_point]
            xp, yp = current_point
            for d in mask:
                n = (d[0] + xp, d[1] + yp)
                map_n = self.map[n]
                if n == self.keys[dest_key]:
                    return current_dist + 1, current_locks, current_keys
                if map_n != "#" and n not in dist:
                    dist[n] = 1 + current_dist
                    queue.append(n)
                    if map_n.isupper():
                        locks_between[n] = current_locks | {map_n.lower()}
                    else:
                        locks_between[n] = current_locks
                    if map_n.islower() and map_n != src_key:
                        keys_between[n] = current_keys | {map_n}
                    else:
                        keys_between[n] = current_locks
        else:
            return -1, {"#"}, {"#"}

    def calc_dist_matrix(self):
        self.key_dist = dict()
        self.locks_between = dict()
        self.keys_between = dict()
        keys = list(self.keys.keys())
        for k1 in keys:
            for k2 in keys:
                if k1 == k2:
                    self.key_dist[(k1, k2)] = 0
                    self.locks_between[(k1, k2)] = set()
                    self.keys_between[(k1, k2)] = set()
                elif (k2, k1) in self.key_dist:
                    self.key_dist[(k1, k2)] = self.key_dist[(k2, k1)]
                    self.locks_between[(k1, k2)] = self.locks_between[(k2, k1)]
                    self.keys_between[(k1, k2)] = self.keys_between[(k2, k1)]
                    continue
                else:
                    (
                        self.key_dist[(k1, k2)],
                        self.locks_between[(k1, k2)],
                        self.keys_between[(k1, k2)],
                    ) = self.min_distance_and_obstacles(k1, k2)

    def accessible_keys(self, from_key, current_keys: list):
        accessible = set()
        current = set(current_keys)
        for k in set(self.keys) - current:
            if (self.locks_between[(from_key, k)] | self.keys_between[(from_key, k)]) <= current:
                accessible.add(k)
        return accessible

    def update_vaults(self, four_vaults):
        if four_vaults and self.vault_counter == 1:
            x, y = self.keys["0"]
            self.vault_counter = 0
            for xn in range(x - 1, x + 2):
                for yn in range(y - 1, y + 2):
                    n = (xn, yn)
                    if xn == x or yn == y:
                        self.map[n] = "#"
                    else:
                        ch = str(self.vault_counter)
                        self.vault_counter += 1
                        self.map[n] = ch
                        self.keys[ch] = n

    def shortest_path_to_collect_keys(self, four_vaults=False):
        self.update_vaults(four_vaults)
        self.calc_dist_matrix()

        steps = dict()
        queue = deque()
        start = tuple(str(i) for i in range(self.vault_counter))
        start = start + ("".join(start),)
        queue.append(start)
        steps[start] = 0
        min_dist = -1
        while queue:
            p = queue.popleft()
            if 0 < min_dist < steps[p]:
                continue
            new_solutions = []
            current_keys = p[-1]
            for i in range(len(p) - 1):
                last_key = p[i]
                found_keys = self.accessible_keys(last_key, current_keys)
                for fk in found_keys:
                    new_solution = list(p)
                    new_solution[i] = fk
                    new_solution[-1] = "".join(sorted(p[-1] + fk))
                    new_solution = tuple(new_solution)
                    new_steps = self.key_dist[(last_key, fk)] + steps[p]
                    if 0 < min_dist < new_steps:
                        continue
                    if new_solution in steps:
                        steps[new_solution] = min(new_steps, steps[new_solution])
                    else:
                        steps[new_solution] = new_steps
                        if len(new_solution) <= len(self.keys):
                            new_solutions.append(new_solution)
                    if len(new_solution[-1]) == len(self.keys):
                        if min_dist < 0:
                            min_dist = new_steps
                        else:
                            min_dist = min(min_dist, new_steps)
            for n in sorted(new_solutions, key=lambda x: steps[x], reverse=False):
                queue.append(n)

        return min_dist


if __name__ == "__main__":
    test1 = ManyWorldsInterpretation("test1.txt")
    assert test1.shortest_path_to_collect_keys() == 8

    test2 = ManyWorldsInterpretation("test2.txt")
    assert test2.shortest_path_to_collect_keys() == 86

    test3 = ManyWorldsInterpretation("test3.txt")
    assert test3.shortest_path_to_collect_keys() == 132

    test4 = ManyWorldsInterpretation("test4.txt")
    assert test4.shortest_path_to_collect_keys() == 136

    test5 = ManyWorldsInterpretation("test5.txt")
    assert test5.shortest_path_to_collect_keys() == 81

    test6 = ManyWorldsInterpretation("test6.txt")
    assert test6.shortest_path_to_collect_keys(True) == 8

    test7 = ManyWorldsInterpretation("test7.txt")
    assert test7.shortest_path_to_collect_keys(True) == 24

    test8 = ManyWorldsInterpretation("test8.txt")
    assert test8.shortest_path_to_collect_keys(True) == 32

    test9 = ManyWorldsInterpretation("test9.txt")
    assert test9.shortest_path_to_collect_keys(True) == 72

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2019_day18.txt'
    many_worlds_interpretation = ManyWorldsInterpretation(input_file)
    print(many_worlds_interpretation.shortest_path_to_collect_keys(False))
    print(many_worlds_interpretation.shortest_path_to_collect_keys(True))
