from InputStream import FrameInputStream
from OutputStream import DetectionOutputStream
from FrameProcessor import frameProcessor
from Pipeline import Pipeline
import concurrent.futures
import cv2

cascadeFile = 'haarcascades/haarcascade_frontalface_default.xml'

if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier()
    if not face_cascade.load(cv2.samples.findFile(cascadeFile)):
        print('Error loading cascades file')
        exit(0)

    framePipeline = Pipeline()
    detectionPipeline = Pipeline()
    inputStream = FrameInputStream()
    outputStream = DetectionOutputStream()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        ex.submit(inputStream.run, framePipeline)
        ex.submit(frameProcessor, framePipeline, detectionPipeline, face_cascade)
        ex.submit(outputStream.run, detectionPipeline)
