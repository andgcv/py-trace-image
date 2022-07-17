from preprocessing_smoothing import apply_smoothing
from cv2 import Sobel, CV_64F
from numpy import sqrt, arctan2, pi
from matplotlib.pyplot import subplots, tight_layout, show

# Load image preprocessed with blur and bilateral filtering
img = apply_smoothing()

# Compute gradients along the x and y axis
gradient_x = Sobel(img, CV_64F, 1, 0)
gradient_y = Sobel(img, CV_64F, 0, 1)


def compute_magnitude():
    # Compute gradient magnitude
    magnitude = sqrt((gradient_x ** 2) + (gradient_y ** 2))
    return magnitude


def compute_orientation():
    # Compute gradient orientation
    orientation = arctan2(gradient_y, gradient_x) * (180 / pi) % 180
    return orientation


def visualize_gradient():
    # Initialize a figure to display the input image, gradient magnitude and gradient orientation representations
    (figure, axis) = subplots(nrows=1, ncols=3, figsize=(8, 4))

    axis[0].imshow(img, cmap="gray")
    axis[1].imshow(compute_magnitude(), cmap="jet")
    axis[2].imshow(compute_orientation(), cmap="jet")

    axis[0].set_title("Source")
    axis[1].set_title("Gradient Magnitude")
    axis[2].set_title("Gradient Orientation")

    tight_layout()
    show()


if __name__ == "__main__":
    visualize_gradient()
