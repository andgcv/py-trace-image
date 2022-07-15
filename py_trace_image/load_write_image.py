from os.path import dirname, join
import cv2

project_root = dirname(dirname(__file__))
output_path = join(project_root, 'py_trace_image')
image_name = ""
image_extension = ""

def load_image():
    path = "{}\\{}.{}".format(output_path, image_name, image_extension)
    img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    return img

def write_image():
    cv2.imwrite("{}\\{}_edit.jpg".format(output_path, image_name), load_image())

if __name__ == "__main__":
    image_name = input('What is the image name?: ')
    image_extension = input('What is the image extension?: ')
    load_or_plot = input('Would you like to load or plot the image? Please answer with "load" or "write": ')

    if load_or_plot == "load":
        load_image()
    elif load_or_plot == "write":
        write_image()
    else:
        print('Invalid input, please answer with "load" or "write"')