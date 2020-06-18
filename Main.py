from FrameInputStream import FrameInputStream
from FrameProcessor import frameProcessor
from FramePipeline import FramePipeline
import concurrent.futures

if __name__ == '__main__':
    pipeline = FramePipeline()
    inputStream = FrameInputStream()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(inputStream.run, pipeline)
        ex.submit(frameProcessor, pipeline)
