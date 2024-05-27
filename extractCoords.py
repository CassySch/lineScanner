import numpy as np
def find_laser_line_coordinates(thresholded_image, brightness_tolerance=50):
    """
      Find the coordinates of the pixels that form the laser line in the thresholded image.

      Parameters:
      thresholded_image: np.ndarray
          The thresholded image containing the laser line.

      Returns:
      coordinates: list of tuples
          A list of (x, y) coordinates of the pixels that form the laser line.
      """
    height, width = thresholded_image.shape
    coordinates = []

    # Scan each column from the top to find the brightest pixel
    for x in range(width):
        for y in range(height):
            if thresholded_image[y, x] == 255:
                coordinates.append((x, y))
                break

    # Scan each column from the bottom to find the brightest pixel
    for x in range(width):
        for y in range(height - 1, -1, -1):
            if thresholded_image[y, x] == 255:
                coordinates.append((x, y))
                break

    # Ensure only one pixel per column by keeping the brightest pixel in each column
    final_coordinates = []
    coord_dict = {}
    for coord in coordinates:
        x, y = coord
        if x in coord_dict:
            coord_dict[x].append(y)
        else:
            coord_dict[x] = [y]

    for x in coord_dict:
        y_values = coord_dict[x]
        if len(y_values) > 1:
            brightest_y = max(y_values)
            final_coordinates.append((x, brightest_y))
        else:
            final_coordinates.append((x, y_values[0]))

    return final_coordinates

