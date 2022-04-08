import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mplimp

diameter = 11
circle = np.zeros((diameter, diameter))
center = ((circle.shape[0]//2,circle.shape[1]//2))
for i in range(circle.shape[0]):
	for j in range (circle.shape[1]):
		if np.sqrt((center[0] - i) ** 2 + (center[1] - j) ** 2) <= diameter//2:
			circle[i,j] = 1


plt.figure()
plt.imshow(circle)
plt.show()

imgEro = mplimp.imread('DecoupageDonnees/Traitement/24.jpg')
img_bin = np.zeros((imgEro.shape[0], imgEro.shape[1]), dtype=bool)
for i in range(imgEro.shape[0]):
	for j in range(imgEro.shape[1]):
		if (int((imgEro[i, j, 0] * 1.0 + imgEro[i, j, 1] * 1.0 + imgEro[i, j, 2] * 1.0)/3)) > 2:
			img_bin[i, j] = 1

					

plt.figure()
plt.imshow(img_bin)
plt.show()


def erode (image_bin, structuring_element, center):
	erosion_output = np.ones((image_bin.shape[0], image_bin.shape[1]), dtype=bool)

	for i in range(image_bin.shape[0]):
		for j in range(image_bin.shape[1]):
			for i2 in range(-center[0], structuring_element.shape[0] - center[0] - 1):
				if (i + i2 < 0) or (i + i2 > image_bin.shape[0] - 1):
					continue

				for j2 in range(-center[1], structuring_element[1] - center[1] - 1):
					if (j + j2 < 0) or (j + j2 > image_bin.shape[1] - 1) or structuring_element.shape[center[0] + i2, center[1] + j2] == 0:
						continue

					if image_bin[i + i2, j + j2] == 0:
						erosion_output[i, j] = 0
						break
				if erosion_output[i, j] == 0:
					break
	return erosion_output

erode(img_bin, circle, center)

def dilate (image_bin, structuring_element, center):
	dilation_output = np.zeros((image_bin.shape[0], image_bin.shape[1]), dtype=bool)

	for i in range(image_bin.shape[0]):
		for j in range(image_bin.shape[1]):
			for i2 in range(-center[0], structuring_element.shape[0] - center - 1):
				if (i + i2 < 0) or (i + i2 > image_bin.shape[0] - 1):
					continue

				for j2 in range(-center[1], structuring_element.shape[1] - center - 1):
					if (j + j2 < 0) or (j + j2 > image_bin.shape[1] - 1) or structuring_element.shape[center[0] + i2, center[1] + j2] == 0:
						continue

					if image_bin[i + i2, j + j2] == 1:
						dilation_output[i, j] = 1
						break
				if dilation_output[i, j] == 1:
					break
	return dilation_output

dilate(img_bin, circle, center)

def opening (image_bin, structuring_element, center):
	dilate(erode(image_bin, structuring_element, center), structuring_element, center)

def closing (image_bin, structuring_element, center):
	erode(dilate(image_bin, structuring_element, center), structuring_element, center)

opening(img_bin, circle, center)
closing(img_bin, circle, center)