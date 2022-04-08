import numpy as np
import cv2
import matplotlib.image as mplimp
import matplotlib.pyplot as plt
import argparse
import os, sys

path = "DecoupageDonnees/Traitement/"
dirs = os.listdir(path)
for file in dirs:
	if file.endswith(".jpeg"):
		print(file)
		kernel = np.ones((5,5), np.uint8)
		img0 = cv2.imread(path + file, 0)
		imgColors = mplimp.imread(path + file)
		img = cv2.medianBlur(img0, 65)
		img_dilation = cv2.dilate(img, kernel, iterations = 2)

		sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
		abs_sobel64f = np.absolute(sobelx64f)
		sobel_8u = np.uint8(abs_sobel64f)

		imgN = np.zeros(abs_sobel64f.shape)
		for i in range(abs_sobel64f.shape[0]) :
			for j in range(abs_sobel64f.shape[1]) :
				if abs_sobel64f[i,j] > 120:
					imgN[i,j] = 255

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
		print(moy_x)
		print(moy_y)

		r = imgColors[moy_x,moy_y,0] * 1.0
		g = imgColors[moy_x,moy_y,1] * 1.0
		b = imgColors[moy_x,moy_y,2] * 1.0
		print(r,"and",g,"and",b)
		print("ROUGE :")
		hist = [0] * 256
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				hist[imgColors[i,j,0]] += 1
		for i, val in enumerate(hist):
			print(f"{i}: {val}")

		print("VERT :")
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				hist[imgColors[i,j,1]] += 1
		for i, val in enumerate(hist):
			print(f"{i}: {val}")

		print("BLEU :")
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				hist[imgColors[i,j,1]] += 1
		for i, val in enumerate(hist):
			print(f"{i}: {val}")
		plt.figure()
		plt.imshow(imgColors)
		plt.show()
	elif file.endswith(".png"):
		print(file)
		kernel = np.ones((5,5), np.uint8)
		img0 = cv2.imread(path + file, 0)
		imgColors = mplimp.imread(path + file)
		img = cv2.medianBlur(img0, 65)
		img_dilation = cv2.dilate(img, kernel, iterations = 2)

		sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
		abs_sobel64f = np.absolute(sobelx64f)
		sobel_8u = np.uint8(abs_sobel64f)

		imgN = np.zeros(abs_sobel64f.shape)
		for i in range(abs_sobel64f.shape[0]) :
			for j in range(abs_sobel64f.shape[1]) :
				if abs_sobel64f[i,j] > 120:
					imgN[i,j] = 255

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
		print(moy_x)
		print(moy_y)

		r = imgColors[moy_x,moy_y,0] * 1.0
		g = imgColors[moy_x,moy_y,1] * 1.0
		b = imgColors[moy_x,moy_y,2] * 1.0
		print(r,"and",g,"and",b)

		hist = [0] * 256
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				hist[imgColors[i,j,0]] += 1
		for i, val in enumerate(hist):
			print(f"{i}: {val}")

		print("VERT :")
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				hist[imgColors[i,j,1]] += 1
		for i, val in enumerate(hist):
			print(f"{i}: {val}")

		print("BLEU :")
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				hist[imgColors[i,j,1]] += 1
		for i, val in enumerate(hist):
			print(f"{i}: {val}")
		plt.figure()
		plt.imshow(imgColors)
		plt.show()
	elif file.endswith(".jpg"):
		print(file)
		kernel = np.ones((5,5), np.uint8)
		img0 = cv2.imread(path + file, 0)
		imgColors = mplimp.imread(path + file)
		img = cv2.medianBlur(img0, 65)
		img_dilation = cv2.dilate(img, kernel, iterations = 2)

		sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
		abs_sobel64f = np.absolute(sobelx64f)
		sobel_8u = np.uint8(abs_sobel64f)

		imgN = np.zeros(abs_sobel64f.shape)
		for i in range(abs_sobel64f.shape[0]) :
			for j in range(abs_sobel64f.shape[1]) :
				if abs_sobel64f[i,j] > 120:
					imgN[i,j] = 255

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
		print(moy_x)
		print(moy_y)

		r = imgColors[moy_x,moy_y,0] * 1.0
		g = imgColors[moy_x,moy_y,1] * 1.0
		b = imgColors[moy_x,moy_y,2] * 1.0
		print(r,"and",g,"and",b)
		print("ROUGE :")
		hist = [0] * 256
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				hist[imgColors[i,j,0]] += 1
		for i, val in enumerate(hist):
			print(f"{i}: {val}")

		print("VERT :")
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				hist[imgColors[i,j,1]] += 1
		for i, val in enumerate(hist):
			print(f"{i}: {val}")

		print("BLEU :")
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				hist[imgColors[i,j,1]] += 1
		for i, val in enumerate(hist):
			print(f"{i}: {val}")
		plt.figure()
		plt.imshow(imgColors)
		plt.show()
