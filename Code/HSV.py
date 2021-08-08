import cv2
import numpy as np
import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"

frame = cv2.imread('test41.jpg')
frame = cv2.rotate(frame, cv2.ROTATE_180)
frame = cv2.resize(frame, (580, 480), interpolation=cv2.INTER_AREA)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


# lower_blue = np.array([80, 120, 80])
# upper_blue = np.array([150, 255, 255])
# mask = cv2.inRange(hsv, lower_blue, upper_blue)

def empty(a):
    pass


# cv2.namedWindow("HSV")
# cv2.resizeWindow("HSV", 320, 240)
cv2.namedWindow("HSV", cv2.WND_PROP_FULLSCREEN)
cv2.resizeWindow("HSV", 640, 580)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

while True:

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(hsv, hsv, mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([hsv, mask, result])

    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# Print if there is a change in HSV value
print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (
    h_min, s_min, v_min, h_max, s_max, v_max))
