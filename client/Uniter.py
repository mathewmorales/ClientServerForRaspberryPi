import cv2

class Uniter:
    def run(self, displayImagePipeline, displayDetectionPipeline):
        while True:
            img = displayImagePipeline.get(block=True)
            detection = displayDetectionPipeline.get(block=False)
            if detection is not None:
                x = detection[0]
                y = detection[1]
                w = detection[2]
                h = detection[3]
                cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 3)
            cv2.imshow('frame', img)