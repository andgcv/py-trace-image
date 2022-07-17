from os import path
from cv2 import imread, IMREAD_GRAYSCALE, resize
from tkinter import Tk, filedialog

root = Tk()

# Get screen width and height which will be used to resize the image loaded
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.withdraw()

image_name = ""


def load_image():
    global image_name

    # Open window to specify the src image
    image_path = filedialog.askopenfilename()

    # Save the image name without the extension
    image_name = path.basename(image_path).split('.')[0]

    # Load grayscale src image
    img = imread(image_path, IMREAD_GRAYSCALE)

    # Check if image loaded successfully
    if img is None:
        print('Error opening image!')
        print('Usage: load_src_image.py [image_path -- {}] \n'.format(image_path))
        return -1

    # If the image's height or width exceeds the monitor resolution, resize the image
    if img.shape[0] > screen_height or img.shape[1] > screen_width:
        return resize_image(img)

    return img


# Resize image according to the screen resolution of the user
def resize_image(img):
    # Compute the scales which will be used to resize the image
    scale_width = (screen_width / img.shape[1]) * 0.8
    scale_height = screen_height / img.shape[0] * 0.8
    scale = min(scale_width, scale_height)

    # Define dimensions desired and resize the image
    dimensions = (int(img.shape[1] * scale), int(img.shape[0] * scale))
    img_resized = resize(img, dimensions)

    return img_resized


def get_image_name():
    return image_name
