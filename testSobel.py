import numpy as np
import cv2
import matplotlib.image as mplimp
import matplotlib.pyplot as plt

img = mplimp.imread("DecoupageDonnees/Traitement/24.jpg")
# plt.figure()
# plt.imshow(img)
# plt.show()

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

# cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize = 3)

# cv2.imshow('a', img)
# cv2.waitKey(0)