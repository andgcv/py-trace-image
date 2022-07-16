from os.path import dirname, join
import cv2

project_root = dirname(dirname(__file__))
output_path = join(project_root, 'py_trace_image\\images')
image_name = ""
image_extension = ""

def load_image():
    image_name = input('What is the image name?: ')
    image_extension = input('What is the image extension?: ')

    path = "{}\\{}.{}".format(output_path, image_name, image_extension)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Check if image is loaded fine
    if img is None:
        print('Error opening image!')
        print('Usage: load_write_image.py [image_name -- {}.{}] \n'.format(image_name, image_extension))
        return -1

    return img

def write_image():
    cv2.imwrite("{}\\{}_edit.jpg".format(output_path, image_name), load_image())

if __name__ == "__main__":
    load_or_plot = input('Would you like to load or plot the image? Please answer with "load" or "write": ')

    if load_or_plot == "load":
        load_image()
    elif load_or_plot == "write":
        write_image()
    else:
        print('Invalid input, please answer with "load" or "write"')