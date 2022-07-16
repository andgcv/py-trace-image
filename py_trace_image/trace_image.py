from load_write_image import load_image
import cv2
import numpy

# Load and resize the image
img = load_image()
img_small = cv2.resize(img, (1080, 720))
# img_small = cv2.resize(img, (720, 1080))

def preprocess_blur():
    # Preprocess image with blur to improve edge map output
    img_median_blur = cv2.medianBlur(img_small, 3)
    img_bilateral_filter = cv2.bilateralFilter(img_median_blur, 11, 21, 7)

    return img_bilateral_filter

def trace_image():
    # Trace image using the Canny algorithm
    canny_edges = cv2.Canny(preprocess_blur(), 725, 1200, None, 5)

    # Find line segments using the probabilistic Hough transform
    trace_output_probabilistic = cv2.cvtColor(canny_edges, cv2.COLOR_GRAY2BGR)
    edge_map_probabilistic = cv2.HoughLinesP(canny_edges, 2, numpy.pi / 180, 8, None, 1, 3)

    # Draw lines through the line segments found
    if edge_map_probabilistic is not None:
        for i in range(0, len(edge_map_probabilistic)):
            line = edge_map_probabilistic[i][0]
            cv2.line(trace_output_probabilistic, (line[0], line[1]), (line[2], line[3]), (245,100,245), 1, cv2.LINE_AA)

    # Show the source and output
    cv2.imshow("Source", img_small)
    cv2.imshow("Edge Map", canny_edges)
    cv2.imshow("Trace Output - Probabilistic", trace_output_probabilistic)

    cv2.waitKey()
    return 0

if __name__ == "__main__":
    trace_image()
