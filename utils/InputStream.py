import socket
from properties import *
import numpy as np

class InputStream():
    def __init__(self, ip, port, numNetworkBytes):
        self.numNetworkBytes = numNetworkBytes
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM)
        self.sock.bind((ip, port))

    def run(self, pipeline):
        while True:
            data, addr = self.sock.recvfrom(self.numNetworkBytes)
            pipeline.insert(data)

    def stop(self):
        self.sock.shutdown()
