import heapq
from collections import deque
from copy import deepcopy


def shortest_path(start, end, graph, weights=None):
    previous = dict()
    pq = [(0, start)]
    dist = {v: float("inf") for v in graph.keys()}
    dist[start] = 0
    # Looping until the priority queue becomes empty
    while pq:
        # The first element in the tuple is the minimum distance vertex
        # Extract it from the priority queue
        _, u = heapq.heappop(pq)

        # Iterate over all adjacent vertices of a vertex
        for v in graph[u]:
            weight = weights[(u, v)]
            # If there is a shorter path to v through u
            if dist[v] > dist[u] + weight:
                # Update the distance of v
                dist[v] = dist[u] + weight
                previous[v] = u
                heapq.heappush(pq, (dist[v], v))

    cur = end
    path = [end]
    while cur != start:
        cur = previous[cur]
        path.append(cur)
    path.reverse()
    return dist[end], path


def path_counter(start, end, graph, max_counter):
    g = deepcopy(graph)
    counter = 0
    while counter < max_counter:
        path = shortest_path(start, end, g)
        if path is None:
            return counter
        for p, q in zip(path[:-1], path[1:]):
            g[p].remove(q)
            g[q].remove(p)
        counter += 1
    return counter


def simplify_graph(graph, weights=None):
    graph = {k: v.copy() for k, v in graph.items()}  # deep copy and cast to dict (if defaultdict)
    if weights is None:
        weights = {}
        for v, ns in graph.items():
            for n in ns:
                weights[(v, n)] = 1
    while True:
        for p in graph.keys():
            if len(graph[p]) == 2:
                n1, n2 = graph[p]
                if p not in graph[n1] or p not in graph[n2]:
                    continue
                break
        else:
            break
        n1, n2 = graph[p]
        w1, w2 = weights[(p, n1)], weights[(p, n2)]
        del graph[p]
        del weights[(p, n1)]
        del weights[(p, n2)]
        del weights[(n1, p)]
        del weights[(n2, p)]
        graph[n1].remove(p)
        graph[n2].remove(p)
        if n2 not in graph[n1]:
            graph[n1].append(n2)
        if n1 not in graph[n2]:
            graph[n2].append(n1)
        if (n1, n2) in weights:
            weights[(n1, n2)] = min(weights[(n1, n2)], w1 + w2)
        else:
            weights[(n1, n2)] = w1 + w2
        if (n2, n1) in weights:
            weights[(n2, n1)] = min(weights[(n2, n1)], w1 + w2)
        else:
            weights[(n2, n1)] = w1 + w2
    return graph, weights


def longest_path_in_graph(start, end, graph):
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
        extra_path = [end]
        end = pre_end
    else:
        extra_path = []

    # DFS search to find the longest path
    max_dist = 0
    longest_path = []
    state = [start, 0, -1]
    visited = {p: False for p in graph.keys()}
    visited[start] = True
    path = [state]
    while path:
        pos, steps, next_no = path[-1]
        if pos == end:
            if steps > max_dist:
                max_dist = steps
                longest_path = [p[0] for p in path] + extra_path
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
    return max_dist + last_step_dist, longest_path
