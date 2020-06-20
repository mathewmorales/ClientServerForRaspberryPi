import socket
from properties import *
import numpy as np

class DetectionOutputStream:
    def __init__(self):
        self.networkBytes = FRAME_WIDTH * FRAME_HEIGHT
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM)

    def run(self, detectionPipeline):
        while True:
            detection = detectionPipeline.get()
            self.sock.sendto(bytes(list(detection)), (CLIENT_IP, UDP_PORT))

    def stop(self):
        self.sock.shutdown()
