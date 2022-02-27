import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img0 = cv2.imread('/users/licence/il09359/Documents/TD_Image/ProjetTI/ProjetTI_traitement/24.jpg', 0) 
img = cv2.medianBlur(img0, 65)


sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()


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

a = x//c
b = y//c
print(a)
print(b)



imgColors = (mpimg.imread('/users/licence/il09359/Documents/TD_Image/ProjetTI/ProjetTI_traitement/24.jpg'))
r = imgColors[a,b,0] * 1.0
g = imgColors[a,b,1] * 1.0
b = imgColors[a,b,2] * 1.0
'''
couleur = ""
if r < 80 and r > 120 and g < 80 and g > 120 and b < 80 and b > 120 :
	couleur = "red"
elif r < 50 and r > 50 and g < 50 and g > 50 and b < 50 and b > 50 :
	couleur = "jaune"
else : 
	couleur = "idk"
Median for black
'''
print(r,"and",g,"and",b)


