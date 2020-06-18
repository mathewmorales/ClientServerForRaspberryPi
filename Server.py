import socket
from properties import *
import numpy as np
import cv2

cascadeFile = 'haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier()
if not face_cascade.load(cv2.samples.findFile(cascadeFile)):
    print('Error loading cascades file')
    exit(0)

sock = socket.socket(socket.AF_INET,
                    socket.SOCK_DGRAM)
sock.bind((SERVER_IP, UDP_PORT))
w = 128
h = 96
scale = 5
while True:
    data, addr = sock.recvfrom(w*h)
    img = np.array(list(data)).astype(np.uint8).reshape(h,w)
    faces = face_cascade.detectMultiScale(img.copy())
    if len(faces) > 0:
        cv2.rectangle(img, (faces[0][0],faces[0][1]), (faces[0][0]+faces[0][2], faces[0][1] + faces[0][3]), (255,255,255), 1)
    img = cv2.resize(img, (w * scale, h * scale))
    cv2.imshow('from RaspberryPi', img)
    cv2.waitKey(1)
