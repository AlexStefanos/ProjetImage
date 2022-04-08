import numpy as np
import cv2
import matplotlib.image as mplimp
import matplotlib.pyplot as plt
import argparse

kernel = np.ones((5,5), np.uint8)
img0 = cv2.imread('DecoupageDonnees/Traitement/24.jpg', 0) 
img = cv2.medianBlur(img0, 65)
img_dilation = cv2.dilate(img, kernel, iterations = 2)
# plt.figure()
# plt.imshow(img)
# plt.show()

sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

# plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
# plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

imgN = np.zeros(abs_sobel64f.shape)
for i in range(abs_sobel64f.shape[0]) :
	for j in range(abs_sobel64f.shape[1]) :
		if abs_sobel64f[i,j] > 120:
			imgN[i,j] = 255

plt.figure()
plt.imshow(imgN,cmap = plt.cm.gray)
plt.show()

x = 0
y = 0
c = 0
for i in range(imgN.shape[0]) :
	for j in range(imgN.shape[1]) :
		if imgN[i,j] == 255:
			x = x + i
			y = y + j
			c = c +1

moy_x = x//c
moy_y = y//c
# print(moy_x)
# print(moy_y)

