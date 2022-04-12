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
		diameter = 11
		circle = np.zeros((diameter, diameter))
		center = (circle.shape[0] // 2, circle.shape[1] // 2)
		for i in range(circle.shape[0]):
			for j in range(circle.shape[1]):
				if np.sqrt((center[0] - i)**2 + (center[1] - j)**2) <= diameter // 2:
					circle[i, j] = 1
		# plt.figure()
		# plt.title("Elem struct")
		# plt.imshow(circle)
		img0 = mplimp.imread(path + file)
		imgColors = mplimp.imread(path + file)
		imgOpening = cv2.morphologyEx(img0, cv2.MORPH_OPEN, circle)
		plt.figure()
		plt.imshow(imgOpening)
		plt.show()

		sobelx64f = cv2.Sobel(imgOpening,cv2.CV_64F,1,0,ksize=5)
		abs_sobel64f = np.absolute(sobelx64f)
		sobel_8u = np.uint8(abs_sobel64f)

		imgN = np.zeros(abs_sobel64f.shape)
		for i in range(abs_sobel64f.shape[0]) :
			for j in range(abs_sobel64f.shape[1]) :
				if abs_sobel64f[i,j,0] > 120:
					imgN[i,j,0] = 255
				if abs_sobel64f[i,j,1] > 120:
					imgN[i,j,1] = 255
				if abs_sobel64f[i,j,2] > 120:
					imgN[i,j,2] = 255

		x = 0
		y = 0
		c = 0
		for i in range(imgN.shape[0]) :
			for j in range(imgN.shape[1]) :
				if imgN[i,j,0] == 255:
					x = x + i
					y = y + j
					c = c + 1
				if imgN[i,j,1] == 255:
					x = x + i
					y = y + j
					c = c +1
				if imgN[i,j,2] == 255:
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
		
		histRed = [0] * 256
		histGreen = [0] * 256
		histBlue = [0] * 256
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				histRed[imgColors[i,j,0]] += 1
		for i, val in enumerate(histRed):
			print(f"{i}: {val}")

		print("VERT :")
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				histGreen[imgColors[i,j,1]] += 1
		for i, val in enumerate(histGreen):
			print(f"{i}: {val}")

		print("BLEU :")
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				histBlue[imgColors[i,j,2]] += 1
		for i, val in enumerate(histBlue):
			print(f"{i}: {val}")
		plt.figure()
		plt.imshow(imgColors)
		plt.show()
	elif file.endswith(".png"):
		print(file)
		kernel = np.ones((5,5), np.uint8)
		diameter = 11
		circle = np.zeros((diameter, diameter))
		center = (circle.shape[0] // 2, circle.shape[1] // 2)
		for i in range(circle.shape[0]):
			for j in range(circle.shape[1]):
				if np.sqrt((center[0] - i)**2 + (center[1] - j)**2) <= diameter // 2:
					circle[i, j] = 1
		# plt.figure()
		# plt.title("Elem struct")
		# plt.imshow(circle)
		img0 = mplimp.imread(path + file)
		imgColors = mplimp.imread(path + file)
		imgOpening = cv2.morphologyEx(img0, cv2.MORPH_OPEN, circle)
		plt.figure()
		plt.imshow(imgOpening)
		plt.show()

		sobelx64f = cv2.Sobel(imgOpening,cv2.CV_64F,1,0,ksize=5)
		abs_sobel64f = np.absolute(sobelx64f)
		sobel_8u = np.uint8(abs_sobel64f)

		imgN = np.zeros(abs_sobel64f.shape)
		for i in range(abs_sobel64f.shape[0]) :
			for j in range(abs_sobel64f.shape[1]) :
				if abs_sobel64f[i,j,0] > 120:
					imgN[i,j,0] = 255
				if abs_sobel64f[i,j,1] > 120:
					imgN[i,j,1] = 255
				if abs_sobel64f[i,j,2] > 120:
					imgN[i,j,2] = 255

		x = 0
		y = 0
		c = 0
		for i in range(imgN.shape[0]) :
			for j in range(imgN.shape[1]) :
				if imgN[i,j,0] == 255:
					x = x + i
					y = y + j
					c = c + 1
				if imgN[i,j,1] == 255:
					x = x + i
					y = y + j
					c = c +1
				if imgN[i,j,2] == 255:
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

		somme = 0
		histRed = [0] * 256
		histGreen = [0] * 256
		histBlue = [0] * 256
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				histRed[imgColors[i,j,0]] += 1
		for i, val in enumerate(histRed):
			print(f"{i}: {val}")

		print("VERT :")
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				histGreen[imgColors[i,j,1]] += 1
		for i, val in enumerate(histGreen):
			print(f"{i}: {val}")

		print("BLEU :")
		for i in range(imgColors.shape[0]):
			for j in range(imgColors.shape[1]):
				histBlue[imgColors[i,j,2]] += 1
		for i, val in enumerate(histBlue):
			print(f"{i}: {val}")
		plt.figure()
		plt.imshow(imgColors)
		plt.show()
	elif file.endswith(".jpg"):
		print(file)
		kernel = np.ones((5,5), np.uint8)
		diameter = 11
		circle = np.zeros((diameter, diameter))
		center = (circle.shape[0] // 2, circle.shape[1] // 2)
		for i in range(circle.shape[0]):
			for j in range(circle.shape[1]):
				if np.sqrt((center[0] - i)**2 + (center[1] - j)**2) <= diameter // 2:
					circle[i, j] = 1
		# plt.figure()
		# plt.title("Elem struct")
		# plt.imshow(circle)
		img0 = mplimp.imread(path + file)
		imgColors = mplimp.imread(path + file)
		imgOpening = cv2.morphologyEx(img0, cv2.MORPH_OPEN, center)
		# plt.figure()
		# plt.imshow(imgOpening)
		# plt.show()

		sobelx64f = cv2.Sobel(imgOpening,cv2.CV_64F,1,0,ksize=5)
		abs_sobel64f = np.absolute(sobelx64f)

		imgN = np.zeros(abs_sobel64f.shape)
		for i in range(abs_sobel64f.shape[0]) :
			for j in range(abs_sobel64f.shape[1]) :
				if abs_sobel64f[i,j,0] > 120:
					imgN[i,j,0] = 255
				if abs_sobel64f[i,j,1] > 120:
					imgN[i,j,1] = 255
				if abs_sobel64f[i,j,2] > 120:
					imgN[i,j,2] = 255
		plt.figure()
		plt.imshow(imgN)
		plt.show()

		x = 0
		y = 0
		c = 0
		for i in range(imgN.shape[0]) :
			for j in range(imgN.shape[1]) :
				if imgN[i,j,0] == 255:
					x = x + i
					y = y + j
					c = c + 1
				if imgN[i,j,1] == 255:
					x = x + i
					y = y + j
					c = c +1
				if imgN[i,j,2] == 255:
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

		xResolution = 0
		yResolution = 0
		xFond = 0
		yFond = 0
		redXMoyFond = 0
		greenXMoyFond = 0
		blueXMoyFond = 0
		redYMoyFond = 0
		greenYMoyFond = 0
		blueYMoyFond = 0
		for i in range(imgColors.shape[0]):
			xResolution += 1
		for i in range(imgColors.shape[1]):
			yResolution += 1
		xFond = xResolution // 100
		yFond = yResolution // 100
		for i in range(xFond, (imgColors.shape[0] - xFond)):
			redXMoyFond += imgColors[i, yFond, 0]
			greenXMoyFond += imgColors[i, yFond, 1]
			blueXMoyFond += imgColors[i, yFond, 2]
		for j in range(yFond, (imgColors.shape[1] - yFond)):
			redYMoyFond += imgColors[xFond, j, 0]
			greenYMoyFond += imgColors[xFond, j, 1]
			blueYMoyFond += imgColors[xFond, j, 2]
		redXMoyFond = redXMoyFond // xResolution
		greenXMoyFond = greenXMoyFond // xResolution
		blueXMoyFond = blueXMoyFond // xResolution
		redYMoyFond = redYMoyFond // yResolution
		greenYMoyFond = greenYMoyFond // yResolution
		blueYMoyFond = blueYMoyFond // yResolution
		print("redXMoyFond : ", redXMoyFond)
		print("greenXMoyFond : ", greenXMoyFond)
		print("blueXMoyFond : ", blueXMoyFond)
		print("redYMoyFond : ", redYMoyFond)
		print("greenYMoyFond : ", greenYMoyFond)
		print("blueYMoyFond : ", blueYMoyFond)

		histRed = [0] * 256
		histGreen = [0] * 256
		histBlue = [0] * 256

		for i in range(imgN.shape[0]):
			for j in range(imgN.shape[1]):
				if imgColors[i, j, 0] >= (redXMoyFond - 10) and imgColors[i, j, 0] <= (redXMoyFond + 10):
					abs_sobel64f[i, j, 0] = 0
				if imgColors[i, j, 0] >= (greenXMoyFond - 10) and imgColors[i, j, 0] <= (greenXMoyFond + 10):
					abs_sobel64f[i, j, 0] = 0
				if imgColors[i, j, 0] >= (blueXMoyFond - 10) and imgColors[i, j, 0] <= (blueXMoyFond + 10):
					abs_sobel64f[i, j, 0] = 0
				if imgColors[i, j, 0] >= (redYMoyFond - 10) and imgColors[i, j, 0] <= (redYMoyFond + 10):
					abs_sobel64f[i, j, 0] = 0
				if imgColors[i, j, 0] >= (greenYMoyFond - 10) and imgColors[i, j, 0] <= (greenYMoyFond + 10):
					abs_sobel64f[i, j, 0] = 0
				if imgColors[i, j, 0] >= (blueYMoyFond - 10) and imgColors[i, j, 0] <= (blueYMoyFond + 10):
					abs_sobel64f[i, j, 0] = 0
		plt.figure()
		plt.imshow(imgN)
		plt.show()
		print("ROUGE :")
		for i in range(imgN.shape[0]):
			for j in range(imgN.shape[1]):
				if abs_sobel64f[i,j,0] == 1:
					histRed[imgColors[i,j,0]] += 1
		for i, val in enumerate(histRed):
			print(f"{i}: {val}")

		print("VERT :")
		for i in range(imgN.shape[0]):
			for j in range(imgN.shape[1]):
				if abs_sobel64f[i,j,1] == 1:
					histGreen[imgColors[i,j,1]] += 1
		for i, val in enumerate(histGreen):
			print(f"{i}: {val}")

		print("BLEU :")
		for i in range(imgN.shape[0]):
			for j in range(imgN.shape[1]):
				if abs_sobel64f[i,j,2] == 1:	
					histBlue[imgColors[i,j,2]] += 1
		for i, val in enumerate(histBlue):
			print(f"{i}: {val}")
		plt.figure()
		plt.imshow(imgColors)
		plt.show()
