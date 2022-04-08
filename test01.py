import numpy as np
import cv2
import matplotlib.image as mplimp
import matplotlib.pyplot as plt

img = mplimp.imread("DecoupageDonnees/Traitement/24.jpg")

print("ROUGE :")
hist = [0] * 256
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		hist[img[i,j,0]] += 1
for i, val in enumerate(hist):
	print(f"{i}: {val}")

print("VERT :")
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		hist[img[i,j,1]] += 1
for i, val in enumerate(hist):
	print(f"{i}: {val}")

print("BLEU :")
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		hist[img[i,j,1]] += 1
for i, val in enumerate(hist):
	print(f"{i}: {val}")