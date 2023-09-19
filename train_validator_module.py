import cv2
import numpy as np
import cv2.face
import os
from capture_face_module import capture_multiple_faces

def train_recognizer(email):
    # Check if 'validator_models' folder exists; if not, create it
    if not os.path.exists('validator_models'):
        os.mkdir('validator_models')

    images = capture_multiple_faces()
    labels = np.zeros(len(images), dtype=int)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(images, labels)

    recognizer.save(f'validator_models/{email}.yml')
