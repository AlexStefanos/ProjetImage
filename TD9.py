
import matplotlib.image as mplimg
import matplotlib.pyplot as plt
import numpy as np

img = (mplimg.imread("images/Shapes2.png").copy() * 255).astype(np.uint8)
plt.figure()
plt.title("Original")
plt.imshow(img, cmap=plt.cm.gray, vmax=255)

# img Gris
img_gris = functions.conversion_en_gris(img)
plt.figure()
plt.title("Gris")
plt.imshow(img_gris, cmap=plt.cm.gray, vmax=255)

# img Binaire
img_binaire = functions.seuillage(img_gris, 50)
plt.figure()
plt.title("Binaire")
plt.imshow(img_binaire, cmap=plt.cm.gray)

# elem structurant
diameter = 11
circle = np.zeros((diameter, diameter))
center = (circle.shape[0] // 2, circle.shape[1] // 2)
for i in range(circle.shape[0]):
    for j in range(circle.shape[1]):
        if np.sqrt((center[0] - i)**2 + (center[1] - j)**2) <= diameter // 2:
            circle[i, j] = 1
plt.figure()
plt.title("Elem struct")
plt.imshow(circle)


def erosion(image, elem_struct, centre):
    image_out = np.zeros((image.shape[0], image.shape[1]))
    print("Do Erosion")
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image_out[x, y] = erosion_check_pixel2(x, y, image, elem_struct, centre)
    return image_out


def erosion_check_pixel(x, y, image, elem_struct, centre):
    for a in range(elem_struct.shape[0]):
        for b in range(elem_struct.shape[1]):
            if elem_struct[a, b] == 1 and x - a >= 0 and y - b >= 0:
                if image[x - a, y - b] == 0:
                    return 0
    return 1


def erosion_check_pixel2(x, y, image, elem_struct, centre):
    for a in range(-center[0], elem_struct.shape[0] - centre[0] - 1):
        for b in range(-center[1], elem_struct.shape[1] - centre[0] - 1):
            if (center[0] - a < 0 or center[0] - a > im
                and elem_struct[center[0] - a, center[1] - b] == 1
                and x - a >= 0 
                and y - b >= 0 
                and x - a < image.shape[0] 
                and y - b < image.shape[1]):

                    if image[x - a, y - b] == 0:
                        return 0
    return 1


def dilatation(image, elem_struct, centre):
    image_out = np.zeros((image.shape[0], image.shape[1]))
    print("Do Erosion")
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image_out[x, y] = dilatation_check_pixel(x, y, image, elem_struct, centre)
    return image_out


def dilatation_check_pixel(x, y, image, elem_struct, centre):
    for a in range(-center[0], elem_struct.shape[0] - centre[0] - 1):
        for b in range(-center[1], elem_struct.shape[1] - centre[0] - 1):
            if elem_struct[center[0] - a, center[1] - b] == 1 and x - a >= 0 and y - b >= 0 and x - a < image.shape[0] and y - b < image.shape[1]:
                if image[x - a, y - b] == 1:
                    return 1
    return 0


img_erode = erosion(img_binaire, circle, center)
plt.figure()
plt.title("Erosion")
plt.imshow(img_erode, cmap=plt.cm.gray)

img_dilate = dilatation(img_binaire, circle, center)
plt.figure()
plt.title("Dilatation")
plt.imshow(img_dilate, cmap=plt.cm.gray)

print("FIN")
plt.show()