import cv2
import numpy as np

def process_circle_frame(frame, circle_ref_diameter_cm, convert_to_meters=False, show_area=False):
    """Process frame for circle measurements"""
    # Implementation from your existing process_circle_frame function
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blur, 50, 150)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = [cnt for cnt in cnts if cv2.contourArea(cnt) > 100]

    # Rest of your circle measurement code...
    return frame 