from os.path import dirname, join
from cv2 import imread, IMREAD_GRAYSCALE, resize

# Define project root folder and image input path
project_root = dirname(dirname(__file__))
input_path = join(project_root, 'py_trace_image\\images')


def load_image():
    image_name = input('What is the image name?: ')
    image_extension = input('What is the image extension?: ')
    image_orientation = input('What is the image orientation, landscape(l) or portrait(p)?: ')

    path = "{}\\{}.{}".format(input_path, image_name, image_extension)

    # Load and resize grayscale src image
    img = resize(imread(path, IMREAD_GRAYSCALE), ((1080, 720) if image_orientation == 'l' else (720, 1080)))

    # Check if image loaded successfully
    if img is None:
        print('Error opening image!')
        print('Usage: load_src_image.py [image_name -- {}.{}] \n'.format(image_name, image_extension))
        return -1

    return img
