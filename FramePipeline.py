import queue

class FramePipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=1)  # Only store and process most recent frame

    def get_frame(self):
        return self.get()

    def add_frame(self, frame):
        if self.full():
            self.get()
        self.put(frame)
