import cv2
import queue
from properties import *

class Uniter:
    def run(self, displayImagePipeline, displayDetectionPipeline):
        while True:
            img = displayImagePipeline.get(block=True)
            try:
                detection = displayDetectionPipeline.get(block=False)
                if detection is not None:
                    x = detection[0] * FRAME_SCALE
                    y = detection[1] * FRAME_SCALE
                    w = detection[2] * FRAME_SCALE
                    h = detection[3] * FRAME_SCALE
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)
            except queue.Empty:
                pass
            except:
                print('error in Uniter.py')
            cv2.imshow('frame', img)
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break 
