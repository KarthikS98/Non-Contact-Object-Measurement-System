import cv2
import numpy as np
import tkinter as tk
import threading
from src.utils.image_processing import get_frame_from_stream
from src.measurement.circle_measurement import process_circle_frame
from src.measurement.rectangle_measurement import process_rectangle_frame

# Global variables
convert_to_meters = False
show_area = False
show_circle = False
show_rectangle = True
running = False

# Load calibration data
try:
    calib_data = np.load('circle_calibration_data.npz')
    circle_ref_diameter_cm = calib_data['diameter_cm']
except FileNotFoundError:
    circle_ref_diameter_cm = 5.8

try:
    calib_data = np.load('rectangle_calibration_data.npz')
    rect_ref_length_cm = calib_data['length_cm']
    rect_ref_width_cm = calib_data['width_cm']
except FileNotFoundError:
    rect_ref_length_cm = 8.0
    rect_ref_width_cm = 8.0

# Rest of your main application code... 