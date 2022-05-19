# Import opencv
import cv2

# Import uuid
import uuid

# Import Operating System
import os

# Import time
import time


labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
# Če boš slikal samo en image, če ne spodnjo vrstico zakomentiraj !!!!!
labels = ['thumbsup']
number_imgs = 6

wd = os.getcwd()
IMAGES_PATH = os.path.join(
    wd, 'Tensorflow', 'workspace', 'images', 'collectedimages')

if not os.path.exists(IMAGES_PATH):
    if os.name == 'posix':
        os.makedirs(IMAGES_PATH)
    if os.name == 'nt':
        print("OperationSystem je NT")
        os.makedirs(IMAGES_PATH)
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.makedirs(path)

for label in labels:
    cap = cv2.VideoCapture(1)
    print('Collecting images for {}'.format(label))
    time.sleep(4)
    for imgnum in range(number_imgs):

        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label +
                               '.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imshow('frame', frame)
        cv2.imshow('frame', frame)
        if imgnum != 0:  # Prva slika bo pokvarjena
            cv2.imwrite(imgname, frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
