import cv2
import numpy as np

img = cv2.imread("images/pepper_hat.jpg", 0)
kernel = np.ones([5, 5])

i_size = img.shape
k_size = kernel.shape

img2 = np.zeros([i_size[0], i_size[1]])

R = i_size[0] + k_size[0] - 1
C = i_size[1] + k_size[1] - 1
Z = np.zeros([R, C])

for i in range(i_size[0]):
    for j in range(i_size[1]):
        Z[i + np.int((k_size[0] - 1) / 2), j + np.int((k_size[1] - 1) / 2)] = img[i, j]

Q = 1.5

for i in range(i_size[0]):
    for j in range(i_size[1]):
        k = Z[i:i + k_size[0], j:j + k_size[1]]
        k = k.flatten()
        summation1 = 0
        summation2 = 0
        for m in range(len(k)):
            if k[m] == 0:
                pass
            else:
                summation1 = summation1 + k[m] ** (Q + 1)
                summation2 = summation2 + k[m] ** Q

        Con_Har_Mean = summation1 / summation2
        img2[i, j] = Con_Har_Mean

img2 = np.array(img2, dtype=np.uint8)
img2 = cv2.hconcat([img, img2])

print('Displaying Image....')
cv2.imshow('Contra-Harmonic Filter', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
