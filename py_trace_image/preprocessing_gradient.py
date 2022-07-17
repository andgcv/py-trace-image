from preprocessing_smoothing import apply_smoothing
from cv2 import Sobel, CV_32F, convertScaleAbs, addWeighted, imshow

# Load image preprocessed with blur and bilateral filtering
img = apply_smoothing()
# Define kernel diameter for Sobel gradient
kernel_size = 3


def apply_gradient():
    # Compute the gradients along the x and y axis
    gradient_x = Sobel(img, ddepth = CV_32F, dx = 1, dy = 0, ksize = kernel_size)
    gradient_y = Sobel(img, ddepth = CV_32F, dx = 0, dy = 1, ksize = kernel_size)

    # Convert gradient magnitude images to unsigned 8-bit integer representation
    gradient_x = convertScaleAbs(gradient_x)
    gradient_y = convertScaleAbs(gradient_y)

    # Combine gradient representations into a single image
    combined_gradient = addWeighted(gradient_x, 0.5, gradient_y, 0.5, 0)

    imshow("Sobel X", gradient_x)
    imshow("Sobel Y", gradient_y)
    imshow("Sobel Combined", combined_gradient)

    return combined_gradient
