import time

import cv2
import numpy as np


def nothing(x):
    # any operation
    pass


cap = cv2.VideoCapture(0)
time.sleep(0.01)

while (True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    output = frame.copy()

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.0, 50, minRadius=25, maxRadius=75)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Output", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
