import numpy as np
import cv2
import matplotlib.image as mplimp
import matplotlib.pyplot as plt
import os, sys

path = "/home/alexandre/ProjetImage/img_proj/"
dirs = os.listdir(path)
for file in dirs:
    if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png"):
        print(file)
        img = mplimp.imread(path + file)
        # plt.figure()
        # plt.imshow(img)
        # plt.show()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
        plt.figure()
        plt.imshow(img)
        plt.show()
