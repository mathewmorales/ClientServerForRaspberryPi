import socket
from properties import *
import numpy as np

class FrameInputStream():
    def __init__(self):
        self.networkBytes = FRAME_WIDTH * FRAME_HEIGHT
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM)
        self.sock.bind((SERVER_IP, UDP_PORT))

    def run(self, framePipeline):
        while True:
            data, addr = self.sock.recvfrom(self.networkBytes)
            data = np.array(list(data))
            data = data.astype(np.uint8)
            data = data.reshape(FRAME_HEIGHT, FRAME_WIDTH)
            framePipeline.insert(data)

    def stop(self):
        self.sock.shutdown()
