import cv2
import serial
from calibrate import calibrate_laser
from extractCoords import find_laser_line_coordinates
from plotCoords import plot_coordinates


def scan(cap, ser, threshold_value=212, step_size=0.5):
    all_coordinates = []  # To store coordinates from each scan
    x_pos = 0
    while x_pos < 15:
        # Capture a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            return
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to the grayscale frame
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        # Threshold the blurred grayscale frame to emphasize the laser line
        _, laser_line_mask = cv2.threshold(blurred_frame, threshold_value, 255, cv2.THRESH_BINARY)

        # Find the coordinates of the laser line pixels
        coordinates = find_laser_line_coordinates(laser_line_mask)
        all_coordinates.append(coordinates)
        x_pos+=step_size
        # Advance the machine by step_size
        gcode_command = f'$J=G21G91X{step_size}F100\n'
        ser.write(gcode_command.encode())
        response = ser.readline().decode().strip()
        print("Response:", response)
    plot_coordinates(all_coordinates)