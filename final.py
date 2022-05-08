import numpy as np
import cv2
import matplotlib.image as mplimp
import matplotlib.pyplot as plt
import os

path = "DecoupageDonnees/Traitement/"
dirs = os.listdir(path)
for file in dirs:
    if file.endswith(".jpeg"):
        print(file)
        # Loads an image
        src = cv2.imread(cv2.samples.findFile(path + file), cv2.IMREAD_COLOR)
        src1 = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
        plt.figure()
        plt.imshow(src1)
        plt.show()
        # Check if image is loaded fine
        if src is None:
            print ('Error opening image!')
            print ('Usage: hough_circle.py [image_name -- default ' + (path + file) + '] \n')
            break
        #imgz = np.zeros(src.shape[0]//25,src.shape[1]//25,dtype = np.uint8)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        if src.shape[0]*src.shape[1] >= 12000000 :
            gray = cv2.medianBlur(gray, 17
                            )
            rows = gray.shape[0]
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=100, maxRadius=500                                               
                                )
        elif src.shape[0]*src.shape[1] >= 2000000 and src.shape[0]*src.shape[1] < 12000000 :
            gray = cv2.medianBlur(gray, 7)
            rows = gray.shape[0]
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=90, maxRadius=300)
        elif src.shape[0]*src.shape[1] < 2000000 :
            gray = cv2.medianBlur(gray, 7)
            rows = gray.shape[0]
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=80, maxRadius=180)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            imgz = np.zeros((src.shape[0]//25,src.shape[1]//25),dtype =np.uint8)
            for i in circles[0, :]:
                center = (i[0], i[1])
                print(i[0],i[1])
                for x in range(imgz.shape[0]) :
                    for y in range(imgz.shape[1]) :
                        print(src[(i[1]-imgz.shape[0]//2)+x,(i[0]-imgz.shape[1]//2)-y,0])

                print(i[0],i[1])
                # circle center
                cv2.circle(src, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv2.circle(src, center, radius, (255, 0, 255), 3)
        cv2.imshow("detected circles", src)
        cv2.waitKey(0)
        
        histRed = [0] * 256
        histGreen = [0] * 256
        histBlue = [0] * 256
        print("ROUGE :")
        for i in range(imgz.shape[0]):
            for j in range(imgz.shape[1]):
                if src[i,j,0] == 1:
                    histRed[imgz[i,j,0]] += 1
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
        for i in range(imgz.shape[0]):
            for j in range(imgz.shape[1]):
                if src[i,j,1] == 1:
                    histGreen[imgz[i,j,1]] += 1
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
        for i in range(imgz.shape[0]):
            for j in range(imgz.shape[1]):
                if src[i,j,2] == 1:	
                    histBlue[imgz[i,j,2]] += 1
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
        elif(iGreen - 50 < 0 and iBlue - 50 < 0):
            print("Rouge : 0,01 0,02 0,05 centimes")
        elif(iRed - iGreen - iBlue < 0):
            print("Gris : 1 euros")
        else:
            print("erreur")
    elif file.endswith(".png"):
        print(file)
        # Loads an image
        src = cv2.imread(cv2.samples.findFile(path + file), cv2.IMREAD_COLOR)
        src1 = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
        plt.figure()
        plt.imshow(src1)
        plt.show()
        # Check if image is loaded fine
        if src is None:
            print ('Error opening image!')
            print ('Usage: hough_circle.py [image_name -- default ' + (path + file) + '] \n')
            break
        #imgz = np.zeros(src.shape[0]//25,src.shape[1]//25,dtype = np.uint8)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        if src.shape[0]*src.shape[1] >= 12000000 :
            gray = cv2.medianBlur(gray, 17
                            )
            rows = gray.shape[0]
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=100, maxRadius=500                                               
                                )
        elif src.shape[0]*src.shape[1] >= 2000000 and src.shape[0]*src.shape[1] < 12000000 :
            gray = cv2.medianBlur(gray, 7)
            rows = gray.shape[0]
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=90, maxRadius=300)
        elif src.shape[0]*src.shape[1] < 2000000 :
            gray = cv2.medianBlur(gray, 7)
            rows = gray.shape[0]
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=80, maxRadius=180)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            imgz = np.zeros((src.shape[0]//25,src.shape[1]//25),dtype =np.uint8)
            for i in circles[0, :]:
                center = (i[0], i[1])
                print(i[0],i[1])
                for x in range(imgz.shape[0]) :
                    for y in range(imgz.shape[1]) :
                        print(src[(i[1]-imgz.shape[0]//2)+x,(i[0]-imgz.shape[1]//2)-y,0])

                print(i[0],i[1])
                # circle center
                cv2.circle(src, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv2.circle(src, center, radius, (255, 0, 255), 3)
        cv2.imshow("detected circles", src)
        cv2.waitKey(0)
        
        histRed = [0] * 256
        histGreen = [0] * 256
        histBlue = [0] * 256
        print("ROUGE :")
        for i in range(imgz.shape[0]):
            for j in range(imgz.shape[1]):
                if src[i,j,0] == 1:
                    histRed[imgz[i,j,0]] += 1
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
        for i in range(imgz.shape[0]):
            for j in range(imgz.shape[1]):
                if src[i,j,1] == 1:
                    histGreen[imgz[i,j,1]] += 1
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
        for i in range(imgz.shape[0]):
            for j in range(imgz.shape[1]):
                if src[i,j,2] == 1:	
                    histBlue[imgz[i,j,2]] += 1
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
        elif(iGreen - 50 < 0 and iBlue - 50 < 0):
            print("Rouge : 0,01 0,02 0,05 centimes")
        elif(iRed - iGreen - iBlue < 0):
            print("Gris : 1 euros")
        else:
            print("erreur")
    elif file.endswith(".jpg"):
        print(file)
        # Loads an image
        src = cv2.imread(cv2.samples.findFile(path + file), cv2.IMREAD_COLOR)
        src1 = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
        plt.figure()
        plt.imshow(src1)
        plt.show()
        # Check if image is loaded fine
        if src is None:
            print ('Error opening image!')
            print ('Usage: hough_circle.py [image_name -- default ' + (path + file) + '] \n')
            break
        #imgz = np.zeros(src.shape[0]//25,src.shape[1]//25,dtype = np.uint8)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        if src.shape[0]*src.shape[1] >= 12000000 :
            gray = cv2.medianBlur(gray, 17
                            )
            rows = gray.shape[0]
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=100, maxRadius=500                                               
                                )
        elif src.shape[0]*src.shape[1] >= 2000000 and src.shape[0]*src.shape[1] < 12000000 :
            gray = cv2.medianBlur(gray, 7)
            rows = gray.shape[0]
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=90, maxRadius=300)
        elif src.shape[0]*src.shape[1] < 2000000 :
            gray = cv2.medianBlur(gray, 7)
            rows = gray.shape[0]
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=80, maxRadius=180)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            imgz = np.zeros((src.shape[0]//25,src.shape[1]//25),dtype =np.uint8)
            for i in circles[0, :]:
                center = (i[0], i[1])
                print(i[0],i[1])
                for x in range(imgz.shape[0]) :
                    for y in range(imgz.shape[1]) :
                        print(src[(i[1]-imgz.shape[0]//2)+x,(i[0]-imgz.shape[1]//2)-y,0])

                print(i[0],i[1])
                # circle center
                cv2.circle(src, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv2.circle(src, center, radius, (255, 0, 255), 3)
        cv2.imshow("detected circles", src)
        cv2.waitKey(0)
        
        histRed = [0] * 256
        histGreen = [0] * 256
        histBlue = [0] * 256
        print("ROUGE :")
        for i in range(imgz.shape[0]):
            for j in range(imgz.shape[1]):
                if src[i,j,0] == 1:
                    histRed[imgz[i,j,0]] += 1
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
        for i in range(imgz.shape[0]):
            for j in range(imgz.shape[1]):
                if src[i,j,1] == 1:
                    histGreen[imgz[i,j,1]] += 1
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
        for i in range(imgz.shape[0]):
            for j in range(imgz.shape[1]):
                if src[i,j,2] == 1:	
                    histBlue[imgz[i,j,2]] += 1
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
        elif(iGreen - 50 < 0 and iBlue - 50 < 0):
            print("Rouge : 0,01 0,02 0,05 centimes")
        elif(iRed - iGreen - iBlue < 0):
            print("Gris : 1 euros")
        else:
            print("erreur")
    else:
        print("Erreur")