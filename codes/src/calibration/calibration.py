import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk

def save_calibration_data(circle_diameter=5.8, rect_length=8.0, rect_width=8.0):
    """Save calibration data for both circle and rectangle measurements"""
    # Save circle calibration
    np.savez('circle_calibration_data.npz', diameter_cm=circle_diameter)
    
    # Save rectangle calibration
    np.savez('rectangle_calibration_data.npz', 
             length_cm=rect_length, 
             width_cm=rect_width) 