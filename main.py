import cv2
import numpy as np
from calibrate import calibrate_laser
from extractCoords import find_laser_line_coordinates
from plotCoords import plot_coordinates
from sendCommands import send_gcode_serial



# Main code
def main():
    send_gcode_serial("/dev/cu.usbserial-0001",115200)
    # # Open the webcam (default camera, index 0)
    # cap = cv2.VideoCapture(0)
    #
    # # Check if the camera opened successfully
    # if not cap.isOpened():
    #     print("Error: Could not open webcam.")
    #     return
    #
    # # Calibrate the laser line
    # reference_frame, threshold_value = calibrate_laser(cap)
    #
    # if reference_frame is None or threshold_value is None:
    #     print("Calibration aborted.")
    # else:
    #     # Convert the reference frame to grayscale
    #     gray_reference_frame = cv2.cvtColor(reference_frame, cv2.COLOR_BGR2GRAY)
    #
    #     # Apply Gaussian blur to the grayscale reference frame
    #     blurred_reference_frame = cv2.GaussianBlur(gray_reference_frame, (5, 5), 0)
    #
    #     # Threshold the blurred grayscale reference frame to emphasize the laser line
    #     _, laser_line_mask = cv2.threshold(blurred_reference_frame, threshold_value, 255, cv2.THRESH_BINARY)
    #
    #     # Find the coordinates of the laser line pixels
    #     coordinates = find_laser_line_coordinates(laser_line_mask)

    #     # Print the coordinates
    #     print("Coordinates of the laser line pixels:")
    #     for coord in coordinates:
    #         print(coord)
    #
    #     # Plot the coordinates
    #     plot_coordinates(coordinates)
    #
    # # Release the webcam
    # cap.release()


if __name__ == "__main__":
    main()
