from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
import numpy as np
import cv2

def drawBoxAndName(frame, coords, label):
    x1, y1, x2, y2 = coords
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 6)
    labelSize = cv2.getTextSize(label,cv2.FONT_HERSHEY_COMPLEX,0.5,2)
    x2 = x1 + labelSize[0][0]
    y2 = y1 - int(labelSize[0][1])
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
    cv2.putText(frame, label, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

identities = {}
identity_file = 'embeddings'
with open(identity_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        try:
            name, embedding = line.split(':')
            identities[name] = np.fromstring(embedding[1:-1], sep=',')
        except:
            pass

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))

mtcnn = MTCNN(keep_all=True, device=device)
resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
cap.set(cv2.CAP_PROP_FRAME_WIDTH,80)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,60)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    boxes, _ = mtcnn.detect(frame)
    if boxes is not None:
        faces = mtcnn(frame)
        if len(boxes) == len(faces) and faces is not None:
            embeddings = resnet(faces)
            for idx, embedding in enumerate(embeddings):
                box = boxes[idx]
                for name, identity in identities.items():
                    if np.linalg.norm(embedding.detach().numpy() - identity) < 1:
                        drawBoxAndName(frame, box.astype('int'), name)
                        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
