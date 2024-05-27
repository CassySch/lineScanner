import cv2
def nothing(x):
    pass

def calibrate_laser(cap, window_name='Calibration'):
    """
    Calibrate the laser line by capturing a reference frame and determining the threshold value.

    Parameters:
    cap: cv2.VideoCapture
        The video capture object.
    window_name: str
        The name of the window for calibration.

    Returns:
    reference_frame: np.ndarray or None
        The reference frame captured during calibration, or None if aborted.
    threshold_value: int or None
        The threshold value determined during calibration, or None if aborted.
    """
    # Create a window for the threshold trackbar
    cv2.namedWindow(window_name)
    cv2.namedWindow('Original Image')
    cv2.namedWindow('Blurred Image')
    cv2.namedWindow('Thresholded Image')

    # Create a trackbar to adjust the threshold value
    cv2.createTrackbar('Threshold', window_name, 0, 255, nothing)
    cv2.setTrackbarPos('Threshold', window_name, 10)

    # Set the size of the windows
    cv2.resizeWindow('Original Image', 320, 240)
    cv2.resizeWindow('Blurred Image', 320, 240)
    cv2.resizeWindow('Thresholded Image', 320, 240)

    reference_frame = None
    threshold_value = None

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to the grayscale image
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        # Get the current threshold value from the trackbar
        threshold_value = cv2.getTrackbarPos('Threshold', window_name)

        # Threshold the blurred grayscale image to emphasize the laser line
        _, laser_line_mask = cv2.threshold(blurred_frame, threshold_value, 255, cv2.THRESH_BINARY)

        # Resize images to fit in the smaller windows
        small_frame = cv2.resize(frame, (320, 240))
        small_blurred_frame = cv2.resize(blurred_frame, (320, 240))
        small_laser_line_mask = cv2.resize(laser_line_mask, (320, 240))

        # Display the images
        cv2.imshow('Original Image', small_frame)
        cv2.imshow('Blurred Image', small_blurred_frame)
        cv2.imshow('Thresholded Image', small_laser_line_mask)

        # Wait for the 'c' key to be pressed for capturing the reference frame
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            reference_frame = frame
            break
        elif key == ord('q'):
            break

    # Clean up windows
    cv2.destroyWindow(window_name)
    cv2.destroyWindow('Original Image')
    cv2.destroyWindow('Blurred Image')
    cv2.destroyWindow('Thresholded Image')

    return reference_frame, threshold_value, laser_line_mask
