import matplotlib.image as mplimp
import matplotlib.pyplot as plt
import os, sys

path = "/home/alexandre/ProjetImage/DecoupageDonnees/Test/"
dirs = os.listdir(path)
for file in dirs:
    if file.endswith(".jpeg"):
        print(file)
        img = mplimp.imread(path + file)
        plt.figure()
        plt.imshow(img)
        plt.show()
    elif file.endswith(".png"):
        print(file)
        img = mplimp.imread(path + file)
        plt.figure()
        plt.imshow(img)
        plt.show()
    elif file.endswith(".jpg"):
        print(file)
        img = mplimp.imread(path + file)
        plt.figure()
        plt.imshow(img)
        plt.show()
