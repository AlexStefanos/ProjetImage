import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as matimg

img = matimg.imread("DecoupageDonnees/Traitement/24.jpg")
plt.figure()
plt.imshow(img)
plt.show()

# imgGris = np.zeros((img.shape[0], img.shape[1]), dtype = np.uint8)
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         imgGris[i, j] = (img[i, j, 0] * 1.0 + img[i, j, 1] * 1.0 + img[i, j, 2] * 1.0) / 3
# plt.figure()
# plt.imshow(imgGris, cmap = plt.cm.gray, vmin = 0, vmax = 255)
# plt.show()

imgTest = np.zeros(img.shape, dtype = np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i, j, 0] > 230 and (img[i, j, 1] > 130) and (img[i, j, 2] > 80):
            imgTest[i, j, 0] = img[i, j, 0]
            imgTest[i, j, 1] = img[i, j, 1]
            imgTest[i, j, 2] = img[i, j, 2]
        else:
            imgTest[i, j, 0] = 0
            imgTest[i, j, 1] = 0
            imgTest[i, j, 2] = 0

plt.figure()
plt.imshow(imgTest)
plt.show()