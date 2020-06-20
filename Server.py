import socket
from properties import *
import numpy as np
import cv2

sock = socket.socket(socket.AF_INET,
                    socket.SOCK_DGRAM)
sock.bind((SERVER_IP, UDP_PORT))
w = FRAME_WIDTH
h = FRAME_HEIGHT
network_len = w * h
scale = 5
while True:
    data, addr = sock.recvfrom(network_len)
    img = np.array(list(data)).astype(np.uint8).reshape(h,w)
    img = cv2.resize(img, (w * scale, h * scale))
    cv2.imshow('from RaspberryPi', img)
    cv2.waitKey(1)
