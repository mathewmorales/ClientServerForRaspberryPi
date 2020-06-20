from properties import *
import numpy as np

def frameProcessor(framePipeline, detectionPipeline, detector):
    while True:
        data = framePipeline.get()
        if data is not None:
            try:
                data = np.array(list(data))
                data = data.astype(np.uint8)
                data = data.reshape(FRAME_HEIGHT, FRAME_WIDTH)
                faces = detector.detectMultiScale(data)
                for face in faces:
                    print(face)
                    detectionPipeline.insert(face)
            except:
                print('error in frameProcessor')
