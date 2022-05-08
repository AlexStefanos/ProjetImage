import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mplimp 
def main(argv):
    
    default_file = 'DecoupageDonnees/Traitement/0.jpeg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    src1 = cv.cvtColor(src,cv.COLOR_BGR2RGB)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    #imgz = np.zeros(src.shape[0]//25,src.shape[1]//25,dtype = np.uint8)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    
    
    if src.shape[0]*src.shape[1] >= 9000000 :
        print(1)
        gray = cv.medianBlur(gray, 17
                         )
        rows = gray.shape[0]
        circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=100, maxRadius=500                               
                               
                               )
    elif src.shape[0]*src.shape[1] >= 2000000 and src.shape[0]*src.shape[1] < 9000000 :
        print(2)
        gray = cv.medianBlur(gray, 7
                         )
        rows = gray.shape[0]
        circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=90, maxRadius=300                               
                               
                               )
    elif src.shape[0]*src.shape[1] < 2000000 :
        print(3)
        gray = cv.medianBlur(gray, 7
                         )
        rows = gray.shape[0]
        circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=80, maxRadius=180                               
                               
                               )
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        imgz = np.zeros((src.shape[0]//25,src.shape[1]//25),dtype =np.uint8)
        for i in circles[0, :]:
            center = (i[0], i[1])
            print(i[0],i[1])
            for x in range(imgz.shape[0]) :
                for y in range(imgz.shape[1]) :
                    print(src[(i[1]-imgz.shape[0]//2)+x,(i[0]-imgz.shape[1]//2)-y,0])

            print(i[0],i[1],i[2])
            
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            for x in range(imgz.shape[0]//8) :
                for y in range(imgz.shape[1]//16) :
                    print(src[(i[1]-i[2]-x),(i[0]-y)])
            cv.circle(src, center, radius, (255, 0, 255), 3)
    
    
    cv.imshow("detected circles", src)
    cv.waitKey(0)
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])