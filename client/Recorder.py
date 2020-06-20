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
            ret, img = self.cap.read()
            if not ret:
                break
            bwImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            outputPipeline.insert(bwImg.flatten())
            displayPipeline.insert(img)
        self.shutdown()

    def shutdown(self):
        cap.release()
        cv2.destroyAllWindows()
