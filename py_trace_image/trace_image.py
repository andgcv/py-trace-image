from load_write_image import load_image
import math
import cv2
import numpy

img = load_image()
img_small = cv2.resize(img, (960, 540))


def trace_image():
    canny_trace = cv2.Canny(img_small, 50, 200, None, 3)

    # Copy edges to separate images
    trace_output = cv2.cvtColor(canny_trace, cv2.COLOR_GRAY2BGR)
    trace_output_probabilistic = numpy.copy(trace_output)

    edges = cv2.HoughLines(canny_trace, 1, numpy.pi / 180, 150, None, 0, 0)

    if edges is not None:
        for i in range(0, len(edges)):
            rho = edges[i][0][0]
            theta = edges[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))

            cv2.line(trace_output, pt1, pt2, (0,0,255), 1, cv2.LINE_AA)

    edges_probabilistic = cv2.HoughLinesP(canny_trace, 1, numpy.pi / 180, 12, None, 1, 3)

    if edges_probabilistic is not None:
        for i in range(0, len(edges_probabilistic)):
            line = edges_probabilistic[i][0]
            cv2.line(trace_output_probabilistic, (line[0], line[1]), (line[2], line[3]), (0,0,255), 1, cv2.LINE_AA)

    cv2.imshow("Source", img_small)
    cv2.imshow("Trace Output", trace_output)
    cv2.imshow("Trace Output - Probabilistic", trace_output_probabilistic)

    cv2.waitKey()
    return 0

if __name__ == "__main__":
    trace_image()
