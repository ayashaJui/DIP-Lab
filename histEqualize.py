import numpy as np
import cv2

image = cv2.imread("images/histo.jpg")
image = cv2.resize(image, (500, 500))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

a = np.zeros(256, dtype=np.float16)
b = np.zeros(256, dtype=np.float16)

height, width = image.shape
image2 = np.zeros([height, width])

for i in range(height):
    for j in range(width):
        g = image[i, j]
        a[g] = a[g] + 1

tmp = 1.0 / (height * width)

for i in range(256):
    for j in range(i + 1):
        b[i] += a[j] * tmp
    b[i] = round(b[i] * 255)

b = b.astype(np.uint8)

for i in range(height):
    for j in range(width):
        g = image[i, j]
        image2[i, j] = b[g]

image2 = np.array(image2, dtype=np.uint8)
output = cv2.hconcat([image, image2])

cv2.imshow('Histogram Equalization', output)
cv2.waitKey()
cv2.destroyAllWindows()
