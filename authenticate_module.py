import cv2
import cv2.face
import os
from capture_face_module import capture_face

def authenticate(email):
    model_path = f'validator_models/{email}.yml'
    
    # Check if model file exists; if not, print error and return None
    if not os.path.exists(model_path):
        print("Error: Model file does not exist.")
        return None

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(model_path)
    
    captured_face = capture_face()
    
    if captured_face is not None:
        # Perform face recognition
        label, confidence = recognizer.predict(captured_face)

        if label == 0 and confidence < 100:  # Adjust confidence threshold as needed
            print(f"It's the user!: {confidence}% confidence.")
            return True
        else:
            print(f"It's not the user!: {confidence}% confidence.")
            return False
    else:
        print("No face captured or program manually closed.")
        return None
