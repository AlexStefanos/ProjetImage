import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def stackImages(scale, imgArray):
    """
    Press multiple images into the same window to display
    :param scale:float type , Output image display percentage , Controls the scale ,0.5= The image resolution is reduced by half
    :param imgArray: Tuple nested list , The image matrix to be arranged
    :return: Output image
    """
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),None, scale, scale)
        if len(imgArray[x][y].shape) == 2: 
            imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
            imageBlank = np.zeros((height, width, 3), np.uint8)
            hor = [imageBlank] * rows
            hor_con = [imageBlank] * rows
            for x in range(0, rows):
                hor[x] = np.hstack(imgArray[x])
                ver = np.vstack(hor)
        else:
            for x in range(0, rows):
                if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                    imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
    else:
        imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
        if len(imgArray[x].shape) == 2: 
            imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
            hor = np.hstack(imgArray)
            ver = hor
    return ver

src = cv2.imread('DecoupageDonnees/Traitement/58.jpeg')
img = src.copy()

img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img_1)
plt.show()
ret, img_2 = cv2.threshold(img_1, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

plt.figure()
plt.imshow(img_2)
plt.show()

kernel = np.ones((25, 25), int)
img_3 = cv2.erode(img_2, kernel, iterations=1)

plt.figure()
plt.imshow(img_3)
plt.show()

kernel = np.ones((10, 10), int)
img_4 = cv2.dilate(img_3, kernel, iterations=1)

plt.figure()
plt.imshow(img_4)
plt.show()

#contours, hierarchy = cv2.findContours(img_4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]
#print(contours)

contours, hierarchy= cv2.findContours(img_4.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


cv2.drawContours(img, contours, -1, (0, 0, 255), 5)


print(len(contours))

"""
cv2.putText(img, "count:{}".format(len(contours)), (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)
cv2.putText(src, "src", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)
cv2.putText(img_1, "gray", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)
cv2.putText(img_2, "thresh", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)
cv2.putText(img_3, "erode", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)
cv2.putText(img_4, "dilate", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)
#imgStack = stackImages(1, ([img]))
#cv2.imshow("imgStack", imgStack)
cv2.waitKey(0)
"""

plt.figure()
plt.imshow(img)
plt.show()

