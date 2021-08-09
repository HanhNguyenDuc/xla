import cv2
import numpy as np

# a = [[4, 5, 1, 3, 3, 0], [5, 4, 0, 6, 5, 2], [0, 6, 4, 4, 6, 5], [4, 5, 2, 2, 0, 6], [0, 3, 1, 1, 4, 1], [1, 5, 3, 4, 6, 2]]
# a = [[4, 5, 1, 3, 3, 0], [5, 4, 0, 6, 5, 2], [0, 6, 4, 4, 6, 5], [4, 5, 2, 2, 0, 6], [0, 3, 1, 1, 4, 1], [1, 5, 3, 4, 6, 2]]
a = [[1, 2, 4, 6, 7], [2, 1, 3, 4, 5], [7, 2, 6, 9, 1], [4, 1, 2, 1, 2]]
a = np.array(a, dtype='uint8')
hist = cv2.calcHist([a], [0], None, [10], [0, 10])

print("org_hist: {}".format(hist))
# 2. normalize hist
h, w = a.shape[:2]
hist = hist/(h*w)

# 3. calculate CDF
cdf = np.cumsum(hist)
print(cdf)
s_k = (4 * cdf - 0.5).astype("uint8")


print(s_k)