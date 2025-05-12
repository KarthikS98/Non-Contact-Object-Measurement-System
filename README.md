
# Non-Contact Object Measurement System using ESP32-CAM

A computer vision-based measurement system that accurately measures object dimensions without physical contact. The system uses ESP32-CAM for image capture and Python with OpenCV for processing and measurements.

## Features

- Real-time object measurement using ESP32-CAM
- Multiple measurement capabilities:
  - Rectangle/Square measurements (length, width)
  - Circle measurements (diameter, radius)
  - Area calculation for both shapes
  - Unit conversion (cm to m)
- Interactive GUI with measurement controls
- Calibration system with visual feedback
- Support for both rectangular and circular objects
- Real-time visual feedback with measurements overlay


## Hardware Requirements

- ESP32-CAM module
- USB to TTL converter
- Power supply (5V)
- Proper lighting setup
- Reference objects for calibration

## Software Requirements

- Python 3.x
- OpenCV
- NumPy
- SciPy
- imutils
- Tkinter (for GUI)
- urllib

## Installation

1. Clone the repository

2. Install required packages:
pip install -r requirements.txt

3. Configure ESP32-CAM:
   - Upload the camera streaming code to ESP32-CAM
   - Connect to your WiFi network
   - Note down the IP address

## Usage

### 1. Calibration Mode

Run the calibration script first:
python src/calibration/calibration.py

- Place a reference object of known dimensions
- Use sliders to adjust measurements
- Press 'S' to save calibration
- Press 'Q' to quit calibration

### 2. Measurement Mode

Run the main measurement application:
python main.py

The GUI provides several controls:
- Start/Stop Measurement
- Toggle between CM and M
- Calculate Area
- Switch between Circle/Rectangle detection

## Key Components

### 1. Calibration System
- Interactive calibration with visual feedback
- Separate calibration for rectangles and circles
- Saves calibration data for future use

### 2. Measurement System
- Real-time object detection
- Accurate dimension calculation
- Support for multiple measurement units
- Area calculation capability

### 3. GUI Interface
- User-friendly controls
- Real-time measurement display
- Easy mode switching
- Visual feedback

## Code Description

1. `calibration.py`:
   - Handles system calibration
   - Uses trackbars for dimension adjustment
   - Saves calibration data to NPZ file

2. `main.py`:
   - Main measurement interface
   - Processes ESP32-CAM stream
   - Implements GUI controls
   - Handles measurement calculations

3. `image_processing.py`:
   - Contains common image processing functions
   - Edge detection
   - Contour processing
   - Shape detection

## Troubleshooting

1. ESP32-CAM Connection:
   - Verify IP address in code
   - Check WiFi connection
   - Ensure proper power supply

2. Calibration Issues:
   - Use well-lit environment
   - Place reference object on contrasting background
   - Ensure stable camera position

3. Measurement Accuracy:
   - Recalibrate if lighting changes
   - Keep camera stable
   - Use proper reference objects

## Future Improvements

- Add support for more complex shapes
- Implement 3D measurements
- Add data logging capabilities
- Develop mobile app integration
- Add automatic calibration
- Implement machine learning for object recognition

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Karthik S

## Acknowledgments

- OpenCV community
- ESP32-CAM developers
- Python community
- RV College of Engineering, Bangalore
