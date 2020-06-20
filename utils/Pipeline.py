import queue

class Pipeline(queue.Queue):
    def __init__(self):
        # Only store and process the single most up to date item
        super().__init__(maxsize=1)

    def insert(self, item):
        if self.full():
            self.get(block=False)
        self.put(item)
