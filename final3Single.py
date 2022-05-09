import numpy as np
import cv2
import matplotlib.image as mplimp
import matplotlib.pyplot as plt

src1 = cv2.imread(cv2.samples.findFile("DecoupageDonnees/Traitement/28.jpg"), cv2.IMREAD_COLOR)
src = cv2.cvtColor(src1,cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)
plt.figure()
plt.imshow(src)
plt.show()
histColor = [0] * 180
histSaturation = [0] * 100
histBrightness = [0] * 100

boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
    ]
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(hsv, hsv, mask = mask)
    # show the images
    cv2.imshow("images", np.hstack([hsv, output]))
    cv2.waitKey(0)