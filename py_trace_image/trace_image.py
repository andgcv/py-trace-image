from preprocessing_gradient import apply_gradient
from cv2 import Canny, cvtColor, COLOR_GRAY2BGR, HoughLinesP, line, LINE_AA, imshow, waitKey
from numpy import pi

# Load preprocessed image
img = apply_gradient()

canny_edges = None
trace_output_probabilistic = None
edge_map_probabilistic = None


def find_edge():
    global canny_edges
    global trace_output_probabilistic
    global edge_map_probabilistic

    # Trace image using the Canny algorithm
    canny_edges = Canny(img, 725, 1200, None, 5)

    # Find line segments using the probabilistic Hough transform
    trace_output_probabilistic = cvtColor(canny_edges, COLOR_GRAY2BGR)
    edge_map_probabilistic = HoughLinesP(canny_edges, 2, pi / 180, 8, None, 1, 3)


def draw_lines():
    # Define the edge map and find line segments
    find_edge()

    # Draw lines through the line segments found
    if edge_map_probabilistic is not None:
        for i in range(0, len(edge_map_probabilistic)):
            line_arr = edge_map_probabilistic[i][0]
            line(trace_output_probabilistic, (line_arr[0], line_arr[1]), (line_arr[2], line_arr[3]), (245, 100, 245), 1, LINE_AA)

    imshow("Edge Map", canny_edges)
    imshow("Trace Output - Probabilistic", trace_output_probabilistic)

    waitKey()


if __name__ == "__main__":
    draw_lines()
