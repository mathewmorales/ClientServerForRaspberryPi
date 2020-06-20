import cv2
from utils.Pipeline import Pipeline
from properties import *

class Recorder:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH * FRAME_SCALE)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT * FRAME_SCALE)

    def run(self, outputPipeline, displayPipeline):
        while(True):
            ret, img = self.cap.read()
            if not ret:
                break
            bwImg = cv2.cvtColor(cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT)), cv2.COLOR_BGR2GRAY)
            outputPipeline.insert(bwImg.flatten())
            displayPipeline.insert(img)
        self.shutdown()

    def shutdown(self):
        cap.release()
        cv2.destroyAllWindows()
