import matplotlib.pyplot as plt

def plot_coordinates(coordinates):
    """
    Plot the coordinates of the laser line pixels using matplotlib.

    Parameters:
    coordinates: list of tuples
        A list of (x, y) coordinates of the pixels that form the laser line.
    """
    if not coordinates:
        print("No coordinates found.")
        return

    x_coords, y_coords = zip(*coordinates)

    # Plot the coordinates
    plt.figure()
    plt.scatter(x_coords, y_coords, c='red', s=1)
    plt.title('Laser Line Coordinates')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().invert_yaxis()  # Invert the y-axis to match image coordinates
    plt.show()