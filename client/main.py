from Recorder import Recorder
from utils.InputStream import InputStream
from utils.OutputStream import OutputStream
from utils.Pipeline import Pipeline
from Uniter import Uniter
from properties import *
import concurrent.futures
import cv2


if __name__ == '__main__':
    outputPipeline = Pipeline()
    displayImagePipeline = Pipeline()
    displayDetectionPipeline = Pipeline()
    recorder = Recorder()
    inputStream = InputStream(ip=CLIENT_IP,
                            port=UDP_PORT,
                            numNetworkBytes=1024)
    outputStream = OutputStream(ip=SERVER_IP,
                            port=UDP_PORT)
    uniter = Uniter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        ex.submit(recorder.run, outputPipeline, displayImagePipeline)
        ex.submit(outputStream.run, outputPipeline)
        ex.submit(inputStream.run, displayDetectionPipeline)
        ex.submit(uniter.run, displayImagePipeline, displayDetectionPipeline)
