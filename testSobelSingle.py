import numpy as np
import cv2
import matplotlib.image as mplimp
import matplotlib.pyplot as plt


kernel = np.ones((5,5), np.uint8)
diameter = 11
circle = np.zeros((diameter, diameter))
center = (circle.shape[0] // 2, circle.shape[1] // 2)
for i in range(circle.shape[0]):
    for j in range(circle.shape[1]):
        if np.sqrt((center[0] - i)**2 + (center[1] - j)**2) <= diameter // 2:
            circle[i, j] = 1

img0 = mplimp.imread("DecoupageDonnees/Traitement/28.jpg")
imgColors = mplimp.imread("DecoupageDonnees/Traitement/28.jpg")
# plt.figure()
# plt.imshow(imgColors)
# plt.show()
imgOpening = cv2.morphologyEx(img0, cv2.MORPH_OPEN, center)

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
# plt.figure()
# plt.imshow(imgN)
# plt.show()

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

imgCarre = np.zeros((imgColors.shape[0]//25, imgColors.shape[1]//25), dtype = np.uint8)
imgCarre[imgCarre.shape[0]//2,imgCarre.shape[1]//2] = 255
imgCarre = imgColors[(moy_x - imgCarre.shape[0]):(moy_x + imgCarre.shape[0]),(moy_y - imgCarre.shape[1]):(moy_y + imgCarre.shape[1])]
plt.figure()
plt.imshow(imgCarre)
plt.show()

# r = imgCarre[moy_x,moy_y,0] * 1.0
# g = imgColors[moy_x,moy_y,1] * 1.0
# b = imgColors[moy_x,moy_y,2] * 1.0
# print(r,"and",g,"and",b)

histRed = [0] * 256
histGreen = [0] * 256
histBlue = [0] * 256

print("ROUGE :")
for i in range(imgCarre.shape[0]):
    for j in range(imgCarre.shape[1]):
        if abs_sobel64f[i,j,0] == 1:
            histRed[imgCarre[i,j,0]] += 1
#print(histRed)
maxRed = 0
iRed = 0
for i in range(253):
    if(histRed[i] + histRed[i+1] + histRed[i+2] + histRed[i+3] > maxRed):
        maxRed = histRed[i] + histRed[i+1] + histRed[i+2] + histRed[i+3]
        iRed = i
    # print(i, ": ", histRed[i])
print(maxRed, iRed)


print("VERT :")
for i in range(imgCarre.shape[0]):
    for j in range(imgCarre.shape[1]):
        if abs_sobel64f[i,j,1] == 1:
            histGreen[imgCarre[i,j,1]] += 1
#print(histGreen)
maxGreen = 0
iGreen = 0
for i in range(253):
    if(histGreen[i] + histGreen[i+1] + histGreen[i+2] + histGreen[i+3] > maxGreen):
        maxGreen = histGreen[i] + histGreen[i+1] + histGreen[i+2] + histGreen[i+3]
        iGreen = i
    # print(i, ": ", histGreen[i])
print(maxGreen, iGreen)


print("BLEU :")
for i in range(imgCarre.shape[0]):
    for j in range(imgCarre.shape[1]):
        if abs_sobel64f[i,j,2] == 1:	
            histBlue[imgCarre[i,j,2]] += 1
maxBlue = 0
iBlue = 0
for i in range(253):
    if(histBlue[i] + histBlue[i+1] + histBlue[i+2] + histBlue[i+3] > maxBlue):
        maxBlue = histBlue[i] + histBlue[i+1] + histBlue[i+2] + histBlue[i+3]
        iBlue = i
    # print(i, ": ", histBlue[i])
print(maxBlue, iBlue)

if(iBlue - 50 < 0):
    print("Jaune : 0,10 0,20 0,50 centimes ou 2 euros")
elif(iGreen - 0 < 0 and iBlue - 50 < 0):
    print("Rouge : 0,01 0,02 0,05 centimes")
elif(iRed - iGreen - iBlue < 0):
    print("Gris : 1 euros")
else:
    print("erreur")

