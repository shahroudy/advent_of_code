import os
from collections import defaultdict
from pathlib import Path
from myutils.io_handler import get_input_data


class ALongWalk:
    def __init__(self, filename):
        self.map = dict()
        lines = Path(filename).read_text().strip().splitlines()
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                self.map[(col, row)] = ch
                if row == 0 and ch == ".":
                    self.start = (col, row)
                if row == len(lines) - 1 and ch == ".":
                    self.end = (col, row)

        self.directions = {"e": (1, 0), "w": (-1, 0), "n": (0, -1), "s": (0, 1)}
        self.slope_dir = {"v": "s", "^": "n", ">": "e", "<": "w"}

    def simplify_graph(self, graph):
        while True:
            for p in graph.keys():
                if len(graph[p]) == 2:
                    n1, n2 = graph[p]
                    if p not in {n[0] for n in graph[n1[0]]} & {n[0] for n in graph[n2[0]]}:
                        continue
                    break
            else:
                break
            n1, n2 = graph[p]
            del graph[p]
            graph[n1[0]].remove((p, n1[1]))
            graph[n2[0]].remove((p, n2[1]))
            graph[n1[0]].append((n2[0], n1[1] + n2[1]))
            graph[n2[0]].append((n1[0], n1[1] + n2[1]))

    def longest_path_in_graph(self, start, end, graph):
        # one improvement is to check if there is only one path to the end and use it instead as end
        pre_end_counter = 0
        last_step_dist = 0
        for p in graph.keys():
            for n, dist in graph[p]:
                if n == end:
                    pre_end_counter += 1
                    pre_end = p
                    last_step_dist = dist
        if pre_end_counter == 1:
            end = pre_end

        # DFS search to find the longest path
        max_dist = 0
        state = [start, 0, -1]
        visited = {p: False for p in graph.keys()}
        visited[start] = True
        path = [state]
        while path:
            pos, steps, next_no = path[-1]
            if pos == end:
                max_dist = max(max_dist, steps)
                path.pop()
                visited[pos] = False
                continue
            while next_no < len(graph[pos]) - 1:
                next_no += 1
                nei, dist = graph[pos][next_no]
                if visited[nei]:
                    continue
                path[-1][2] = next_no
                path.append([nei, steps + dist, -1])
                visited[nei] = True
                break
            else:
                path.pop()
                visited[pos] = False
        return max_dist + last_step_dist

    def longest_hike(self, slopes=True):
        graph = defaultdict(list)
        for pos, ch in self.map.items():
            if ch == "#":
                continue
            for _, dir in self.directions.items():
                if slopes and ch in self.slope_dir and dir != self.directions[self.slope_dir[ch]]:
                    continue
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if new_pos in self.map and self.map[new_pos] != "#":
                    graph[pos].append((new_pos, 1))
        self.simplify_graph(graph)
        return self.longest_path_in_graph(self.start, self.end, graph)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = ALongWalk(filename)
    assert answer1 is None or test.longest_hike() == answer1
    assert answer2 is None or test.longest_hike(slopes=False) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 94, 154)

    print("Tests passed, starting with the puzzle")

    puzzle = ALongWalk(data.input_file)
    print(puzzle.longest_hike())
    print(puzzle.longest_hike(slopes=False))
