from collections import deque
from copy import deepcopy


def shortest_path(start, end, graph):
    q = deque([(start,)])
    visited = set(start)
    while q:
        path = q.popleft()
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(path + (neighbor,))
                visited.add(neighbor)
    return None


def path_counter(start, end, graph, max_counter):
    g = deepcopy(graph)
    counter = 0
    while counter < max_counter:
        path = shortest_path(start, end, g)
        if path is None:
            return counter
        for i in range(len(path) - 1):
            g[path[i]].remove(path[i + 1])
            g[path[i + 1]].remove(path[i])
        counter += 1
    return counter
