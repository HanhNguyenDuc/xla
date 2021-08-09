import cv2
import numpy as np

a = [[15,15,15,0,1,2,3],
    [15,14,15,1,15,1,2],
    [15,2,14,2,1,0,1],
    [14,14,15,1,0,2,1],
    [0,1,2,15,15,15,10],
    [1,15,1,10,15,0,15],
    [0,1,0,12,12,15,15]]

a_np = np.array(a, dtype='uint8')

median = cv2.medianBlur(a_np, 3)

print(median)