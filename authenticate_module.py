import cv2
from capture_face_module import capture_face

def authenticate():
    captured_face = capture_face()
    if captured_face is not None:
        print("Face captured as NumPy array.")
        cv2.imshow('Captured Face', captured_face)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No face captured or program manually closed.")