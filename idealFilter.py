import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


img = Image.open(r'images/pic.jpg')
img2 = img.resize((100, 100))
plt.imshow(img2, cmap='gray')
plt.show()

h, w = img2.size
img2 = np.asarray(img2)

pre_dfd = np.zeros((h, w), dtype=np.float64)
dft = np.zeros((h, w), dtype=np.float64)

# centralize
for x in range(h):
    for y in range(w):
        pre_dfd[x, y] = img2[x, y] * ((-1) ^ (x + y))

# fourier transform
for k in range(h):
    for l in range(w):
        summation = 0.0
        for m in range(h):
            for n in range(w):
                theta1 = (((2*m)+1)*k*np.pi) / (2*h)
                theta2 = (((2*n)+1)*l*np.pi) / (2*w)
                val = np.cos(theta1) * np.cos(theta2)
                summation += pre_dfd[m, n] * val
            dft[k, l] = summation

dist = np.zeros((h, w), dtype=np.float64)
filt = np.zeros((h, w), dtype=np.float64)

for u in range(h):
    for v in range(w):
        dist[u, v] = np.sqrt((np.power((u - (h / 2)), 2)) + (np.power((v - (w / 2)), 2)))


# low pass filter
radius_val = 50

for u in range(h):
    for v in range(w):
        if dist[u, v] > radius_val:
            dft[u, v] = 0

# inverse Fourier
inv_dft = np.zeros((h, w), dtype=np.float64)

for k in range(h):
    for l in range(w):
        summation = 0.0
        for m in range(h):
            for n in range(w):
                theta1 = (((2 * m) + 1) * k * np.pi) / (2 * h)
                theta2 = (((2 * n) + 1) * l * np.pi) / (2 * w)
                val = np.cos(theta1) * np.cos(theta2)
                summation += dft[m, n] * val
        inv_dft[k, l] = 2 * summation / h

output_img = np.zeros((h, w), dtype=np.float64)

# Decentralize
for u in range(h):
    for v in range(w):
        output_img[u, v] = inv_dft[u, v] * ((-1) ^ (u + v))


plt.imshow(output_img.real, cmap='gray')
plt.show()
