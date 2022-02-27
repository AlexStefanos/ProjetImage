import numpy as np
import cv2
import matplotlib.image as mplimp
import matplotlib.pyplot as plt

img = cv2.imread('Piece1.jpeg', cv2.IMREAD_GRAYSCALE)
#img = (mplimp.imread('/users/licence/il06110/landscape.png') * 255 ). astype(np.uint8)
# plt.figure()
# plt.imshow(img, cmap=plt.cm.gray, vmin=0, vmax=255)
# plt.show()

hist = [0] * 256
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		hist[img[i,j]] += 1
for i, val in enumerate(hist):
	print(f"{i}: {val}")

img_tree = np.zeros((img.shape[0], img.shape[1], 3), dtype = np.uint8)

for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		if img[i,j] > 200 and img[i, j] < 256:
			img_tree[i,j] = [34, 139, 34]
		else: 
			img_tree[i,j] = img[i,j]

plt.figure()
plt.imshow(img_tree, cmap=plt.cm.gray, vmin=0, vmax=255)
plt.show()

# img_mountain = np.zeros((img.shape[0], img.shape[1], 3), dtype = np.uint8)

# for i in range(img.shape[0]):
# 	for j in range(img.shape[1]):
# 		if img[i,j] > 85 and img[i,j] < 115 :
# 			img_mountain[i,j] = [139, 69, 19]
# 		else: 
# 			img_mountain[i,j] = img[i,j]

# plt.figure()
# plt.imshow(img_mountain, cmap=plt.cm.gray, vmin=0, vmax=255)
# plt.show()


# img_full = np.zeros((img.shape[0], img.shape[1], 3), dtype = np.uint8)
# for i in range(img.shape[0]):
# 	for j in range(img.shape[1]):
# 		if img[i,j] > 85 and img[i,j] < 115 :
# 			img_full[i,j] = [139, 69, 19]
# 		elif img[i,j] < 80 : 
# 			img_full[i,j] = [34, 139, 34]
# 		elif img[i,j] > 115 :
# 			img_full[i,j] = [135, 206, 235]

# plt.figure()
# plt.imshow(img_full, cmap=plt.cm.gray, vmin=0, vmax=255)
# plt.show()
