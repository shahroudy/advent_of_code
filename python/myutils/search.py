import heapq as hq
from abc import abstractmethod


class Search:
    def __init__(self, initial_state, **kwargs):
        self.initial_state = initial_state
        self.args = kwargs

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def get_next_states(self, state):
        pass

    @abstractmethod
    def is_goal(self, state):
        pass

    @abstractmethod
    def get_result(self, state):
        pass


class Search_MinHeap(Search):
    def __init__(self, initial_state, **kwargs):
        super().__init__(initial_state, **kwargs)
        self.min_heap = []
        hq.heapify(self.min_heap)
        self.min_heap.append(initial_state)

    def search(self):
        while self.min_heap:
            state = hq.heappop(self.min_heap)
            if self.is_goal(state):
                return self.get_result(state)
            for next_state in self.get_next_states(state):
                hq.heappush(self.min_heap, next_state)
