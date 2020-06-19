def frameProcessor(framePipeline, detectionPipeline, detector):
    while True:
        frame = framePipeline.get()
        if frame is not None:
            faces = detector.detectMultiScale(frame)
            for face in faces:
                detectionPipeline.insert(face)
