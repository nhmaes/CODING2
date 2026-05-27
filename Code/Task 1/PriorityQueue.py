class PriorityQueue:
    def __init__(self, data=None):
        self._queue = []
        self._counter = 0          # tiebreaker: preserves insertion order within same priority

        if data:
            for item in data:
                self.add(item)

    def add(self, data):
        name, priority = data
        # Store as (priority, insertion_order, name) so equal-priority items come out FIFO
        self._queue.append((priority, self._counter, name))
        self._counter += 1
        # Sort ascending: lowest priority number = highest priority (comes out first)
        self._queue.sort(key=lambda x: (x[0], x[1]))

    def is_empty(self):
        return len(self._queue) == 0

    def get(self):
        if not self.is_empty():
            priority, _, name = self._queue.pop(0)   # pop from front = highest priority
            return name                               # return just the name string
        return None

    def __repr__(self):
        return f"PriorityQueue({[(name, p) for p, _, name in self._queue]})"
