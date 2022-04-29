import cv2
import numpy as np

img = cv2.imread("images/panda.jpg", 0)

img = cv2.resize(img, (500, 500))

kernel = np.ones([5, 5]) / 25

i_size = img.shape
k_size = kernel.shape

img2 = np.zeros([i_size[0], i_size[1]])

R = i_size[0] + k_size[0] - 1
C = i_size[1] + k_size[1] - 1
Z = np.zeros([R, C])

for i in range(i_size[0]):
    for j in range(i_size[1]):
        Z[i+np.int((k_size[0]-1)/2), j+np.int((k_size[1]-1)/2)] = img[i, j]

for i in range(i_size[0]):
    for j in range(i_size[1]):
        k = Z[i:i+k_size[0], j:j+k_size[1]]
        img2[i, j] = np.sum(k * kernel)


img2 = np.array(img2, dtype=np.uint8)

factor = int(input("Enter Factor: "))
mask = cv2.subtract(img, img2)
mask_factor = cv2.multiply(mask, factor)
img2 = cv2.add(img, mask_factor)

img2 = cv2.hconcat([img, img2])

cv2.imshow('High Boost', img2)
cv2.waitKey()
cv2.destroyAllWindows()
