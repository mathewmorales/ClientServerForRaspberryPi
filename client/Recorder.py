import cv2
from utils.Pipeline import Pipeline
from properties import *

class Recorder:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    def run(self, outputPipeline, displayPipeline):
        while(True):
        	ret, img = cap.read()
        	if not ret:
        		break
            bwImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            displayPipeline.insert(bwImg.flatten())
            outputPipeline.insert(img)
        	if cv2.waitKey(1) & 0xFF == ord('q'):
        		break
        self.shutdown()

    def shutdown(self):
        cap.release()
        cv2.destroyAllWindows()
