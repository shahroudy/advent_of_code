import heapq as hq
from abc import abstractmethod
from collections import defaultdict, deque
from multiprocessing import Pool

# from queue import Queue


class Search:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @abstractmethod
    def search(self, initial_state=None):
        raise NotImplementedError

    @abstractmethod
    def search_mp(self, initial_state=None, workers=24):
        raise NotImplementedError

    @abstractmethod
    def get_next_states(self, state):
        raise NotImplementedError

    @abstractmethod
    def is_goal(self, state):
        raise NotImplementedError

    @abstractmethod
    def cost(self, state):
        raise NotImplementedError

    @abstractmethod
    def heuristic(self, state):
        raise NotImplementedError

    @abstractmethod
    def get_result(self, state):
        raise NotImplementedError

    @abstractmethod
    def state_core(self, state):
        """
        Core presentation of the state, in an immutable form.
        Used to avoid repetition of the same state in the search.

        Args:
            state: The state to be processed.

        Returns:
            The immutable core state.
        """
        raise NotImplementedError


class Search_BFS(Search):
    def search(self, initial_state=None):
        initial_state = initial_state if initial_state else self.initial_state
        self.queue = deque()
        self.queue.append(initial_state)
        history = {
            self.state_core(initial_state),
        }
        while self.queue:
            state = self.queue.popleft()
            for next_state in self.get_next_states(state):
                if (core_state := self.state_core(next_state)) in history:
                    continue
                if self.is_goal(next_state):
                    return self.get_result(next_state)
                self.queue.append(next_state)
                history.add(core_state)

    def search_mp(self, initial_state=None, workers=24):

        initial_state = initial_state if initial_state else self.initial_state
        states = [initial_state]
        history = {
            self.state_core(initial_state),
        }

        with Pool(workers) as p:
            while states:
                all_next_states = p.map(self.get_next_states, states)
                states = []
                for next_states in all_next_states:
                    for next_state in next_states:
                        if (core_state := self.state_core(next_state)) in history:
                            continue
                        if self.is_goal(next_state):
                            return self.get_result(next_state)
                        states.append(next_state)
                        history.add(core_state)


class Search_DFS(Search):
    def search(self, initial_state=None):
        initial_state = initial_state if initial_state else self.initial_state
        self.stack = []
        self.history = set()
        self.history.add(self.state_core(initial_state))
        self.stack.append(initial_state)
        while self.stack:
            state = self.stack.pop()
            if self.is_goal(state):
                return self.get_result(state)
            for next_state in self.get_next_states(state):
                core_state = self.state_core(next_state)
                if core_state in self.history:
                    continue
                self.stack.append(next_state)
                self.history.add(core_state)


class Search_DFS_MaxCost(Search):
    def search(self, initial_state=None):
        initial_state = initial_state if initial_state else self.initial_state
        self.stack = []
        self.stack.append(initial_state)
        max_cost = None
        while self.stack:
            state = self.stack.pop()
            max_cost = max(max_cost, self.cost(state)) if max_cost is not None else self.cost(state)
            for next_state in self.get_next_states(state):
                self.stack.append(next_state)
        return max_cost


class Search_MinHeap(Search):
    def search(self, initial_state=None):
        initial_state = initial_state if initial_state else self.initial_state
        min_heap = []
        hq.heapify(min_heap)
        min_heap.append(initial_state)
        while min_heap:
            state = hq.heappop(min_heap)
            if self.is_goal(state):
                return self.get_result(state)
            for next_state in self.get_next_states(state):
                hq.heappush(min_heap, next_state)


class Search_AStar(Search):
    def search(self, initial_state=None):
        initial_state = initial_state if initial_state else self.initial_state
        min_heap = []
        hq.heapify(min_heap)
        init_score = self.heuristic(initial_state) + self.cost(initial_state)
        min_heap.append(init_score)
        history = {self.state_core(initial_state): self.cost(initial_state)}
        states = defaultdict(list)
        states[init_score].append(initial_state)
        while min_heap:
            score = hq.heappop(min_heap)
            state = states[score].pop()
            if self.is_goal(state):
                return self.get_result(state)
            for next_state in self.get_next_states(state):
                core_state = self.state_core(next_state)
                cost = self.cost(next_state)
                if core_state in history:
                    if history[core_state] <= cost:
                        continue
                history[core_state] = self.cost(next_state)
                next_score = self.heuristic(next_state) + self.cost(next_state)
                states[next_score].append(next_state)
                hq.heappush(min_heap, next_score)


class Search_Dijkstra(Search):
    def search(self, initial_state=None):
        initial_state = initial_state if initial_state else self.initial_state
        min_heap = []
        hq.heapify(min_heap)
        init_score = self.cost(initial_state)
        min_heap.append(init_score)
        shortest_distance = {self.state_core(initial_state): init_score}
        backtrace = defaultdict(set)
        states = defaultdict(list)
        states[init_score].append(initial_state)
        while min_heap:
            score = hq.heappop(min_heap)
            state = states[score].pop()
            if shortest_distance[self.state_core(state)] < score:
                continue
            for next_state in self.get_next_states(state):
                core_state = self.state_core(next_state)
                next_score = self.cost(next_state)
                if shortest_distance.get(core_state, float("inf")) < next_score:
                    continue
                elif shortest_distance.get(core_state, float("inf")) == next_score:
                    backtrace[core_state].add(self.state_core(state))
                    continue
                shortest_distance[core_state] = next_score
                states[next_score].append(next_state)
                backtrace[core_state] = {self.state_core(state)}
                hq.heappush(min_heap, next_score)
        return shortest_distance, backtrace
