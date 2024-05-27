import cv2
import serial
from calibrate import calibrate_laser
from extractCoords import find_laser_line_coordinates
from plotCoords import plot_coordinates
from scan import scan


def send_gcode_serial(port, baudrate=115200):
    """
    Send G-code commands serially.

    Parameters:
    port: str
        The serial port to which the device is connected (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux).
    baudrate: int, optional
        The baud rate of the serial communication. Default is 9600.

    Returns:
    None
    """
    ser = None  # Initialize ser variable
    try:
        # Open serial connection
        ser = serial.Serial(port, baudrate, timeout=1)

        print("Serial connection established.")

        while True:
            # Get user input
            command = input("Enter G-code command ('quit' to exit): ")
            action = ''
            # Open the webcam (default camera, index 0)
            cap = cv2.VideoCapture(0)

            # Check if the camera opened successfully
            if not cap.isOpened():
                print("Error: Could not open webcam.")
                break

            if command == 'calibrate':
                # Calibrate the laser line
                reference_frame, threshold_value,laser_line_mask = calibrate_laser(cap)
                coordinates = find_laser_line_coordinates(laser_line_mask)
                plot_coordinates(coordinates)
            elif command == 'home':
                action = '$H'
            elif command == 'scan':
                # Set relative positioning mode (G91) once
                ser.write(b'G91\n')
                ser.write(b'M3\n')
                scan(cap, ser)
            # Send the G-code command
            ser.write((action + '\n').encode())
            # Wait for response (if needed)
            response = ser.readline().decode().strip()
            print("Response:", response)

    except serial.SerialException as e:
        print("Error:", e)

    finally:
        # Close serial connection
        if ser is not None and ser.is_open:
            ser.close()
            print("Serial connection closed.")