import cv2
import socket
from properties import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

while(True): 
	ret, img = cap.read() 
	if not ret: 
		break 
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame', img) 
	img = img.flatten()
	sock.sendto(bytes(img), (SERVER_IP, UDP_PORT))
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break 
cap.release() 
cv2.destroyAllWindows() 