import cv2
import numpy as np
import math
from statistics import median

# Initialize variables
loop = True

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # Try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

if rval:
    while loop:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # Exit on ESC
            loop = False
        num = (frame[..., 2] > 236)
        xy_val =  num.nonzero()

        if len(xy_val[0]) > 0 and len(xy_val[1]) > 0:
            y_val = median(xy_val[0])
            x_val = median(xy_val[1])

            dist = abs(x_val - 320)  # Distance of dot from center x-axis only

            # Calculate object distance using a simple geometric formula
            theta = 0.0011450 * dist + 0.0154
            tan_theta = math.tan(theta)

            if tan_theta > 0: # Error checking
                obj_dist = int(5.33 / tan_theta)

            print("(Distance from center pixel: {})".format(dist))
            print("The dot is {} cm away".format(obj_dist))

        else:
            print("No data available for median calculation.")

else:
    print("Failed to open webcam.")

# Release the webcam and close windows
vc.release()
cv2.destroyAllWindows()
