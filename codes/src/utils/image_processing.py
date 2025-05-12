import cv2
import numpy as np
import urllib.request
from scipy.spatial.distance import euclidean
from imutils import perspective

def get_frame_from_stream(url):
    """Capture frame from ESP32-CAM stream"""
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgnp, -1)
    return frame

def preprocess_frame(frame):
    """Common image preprocessing steps"""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blur, 50, 150)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    return edged 