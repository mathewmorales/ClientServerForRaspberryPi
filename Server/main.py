from FrameProcessor import frameProcessor
from utils.InputStream import InputStream
from utils.OutputStream import OutputStream
from utils.Pipeline import Pipeline
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
    inputStream = InputStream(ip=SERVER_IP,
                            port=UDP_PORT,
                            numNetworkBytes=FRAME_WIDTH * FRAME_HEIGHT)
    outputStream = OutputStream(ip=CLIENT_IP,
                            port=UDP_PORT)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        ex.submit(inputStream.run, framePipeline)
        ex.submit(frameProcessor, framePipeline, detectionPipeline, face_cascade)
        ex.submit(outputStream.run, detectionPipeline)
