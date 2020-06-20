import socket
from properties import *
import numpy as np

class OutputStream:
    def __init__(self, ip, port):
        self.networkBytes = FRAME_WIDTH * FRAME_HEIGHT
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM)
        self.ip = ip
        self.port = port

    def run(self, pipeline):
        while True:
            data = pipeline.get()
            self.sock.sendto(bytes(list(data)), (self.ip, self.port))

    def stop(self):
        self.sock.shutdown()
