import numpy as np
import cv2
import matplotlib.image as mplimp
import matplotlib.pyplot as plt
import os
import json

path = "DecoupageDonnees/Traitement/"
dirs = os.listdir(path)
countI = 0
countP = 0
finalP = 0
finalI = 0
for file in dirs:
    if file.endswith(".jpeg"):
        countI = countI + 1
        s = file.split(".")[0]
        with open("DecoupageDonnees/JSON/"+s+".json") as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
    
        data = jsonObject['shapes']
        
        print(file)
        src1 = cv2.imread(cv2.samples.findFile(path + file), cv2.IMREAD_COLOR)
        src = cv2.cvtColor(src1,cv2.COLOR_BGR2RGB)
        plt.figure()
        plt.imshow(src)
        plt.show()
        histRed = [0] * 256
        histGreen = [0] * 256
        histBlue = [0] * 256
        histRed2 = [0] * 256
        histGreen2 = [0] * 256
        histBlue2 = [0] * 256
        couleur = ""
        piece = ""
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
            imgz = np.zeros((src.shape[0]//25, src.shape[1]//25), dtype = np.uint8)
            tabcoin = []
            for c in circles[0, :]:
                piece = ""
                radius = c[2]
                center = (c[0], c[1])
                for x in range(imgz.shape[0]):
                    for y in range(imgz.shape[1]):
                        histRed[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,0]] += 1
                        histGreen[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,1]] += 1
                        histBlue[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,2]] += 1
                print("ROUGE :")
                maxRed = 0
                iRed = 0
                for i in range(253):
                    if(histRed[i] + histRed[i+1] + histRed[i+2] + histRed[i+3] > maxRed):
                        maxRed = histRed[i] + histRed[i+1] + histRed[i+2] + histRed[i+3]
                        iRed = i
                print(maxRed, iRed)
                print("VERT :")
                maxGreen = 0
                iGreen = 0
                for i in range(253):
                    if(histGreen[i] + histGreen[i+1] + histGreen[i+2] + histGreen[i+3] > maxGreen):
                        maxGreen = histGreen[i] + histGreen[i+1] + histGreen[i+2] + histGreen[i+3]
                        iGreen = i
                print(maxGreen, iGreen)
                print("BLEU :")
                maxBlue = 0
                iBlue = 0
                for i in range(253):
                    if(histBlue[i] + histBlue[i+1] + histBlue[i+2] + histBlue[i+3] > maxBlue):
                        maxBlue = histBlue[i] + histBlue[i+1] + histBlue[i+2] + histBlue[i+3]
                        iBlue = i
                print(maxBlue, iBlue)
                if(iBlue < 75):
                    #print("Jaune : 0,10 0,20 0,50 centimes ou 2 euros")
                    couleur = "Jaune"
                    for v in range(radius//8) :
                        for w in range(radius//16) :
                            histRed2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,0]] += 1
                            histGreen2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,1]] += 1
                            histBlue2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,2]] += 1
                    print("ROUGE2 :")
                    maxRed2 = 0
                    iRed2 = 0
                    for i in range(253):
                        if(histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3] > maxRed2):
                            maxRed2 = histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3]
                            iRed2 = i
                    print(maxRed2, iRed2)
                    print("VERT2 :")
                    maxGreen2 = 0
                    iGreen2 = 0
                    for i in range(253):
                        if(histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3] > maxGreen2):
                            maxGreen2 = histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3]
                            iGreen2 = i
                    print(maxGreen2, iGreen2)
                    print("BLEU2 :")
                    maxBlue2 = 0
                    iBlue2 = 0
                    for i in range(253):
                        if(histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3] > maxBlue2):
                            maxBlue2 = histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3]
                            iBlue2 = i
                    print(maxBlue2, iBlue2)
                    if((iRed2+30) > iGreen2) and (iGreen2 > (iRed2-30)):
                        #print("Il y a du gris : 2 euros")
                        piece = "2.00E"
                elif(iGreen - 50 < 0 and iBlue - 50 < 0):
                    #print("Rouge : 0,01 0,02 0,05 centimes")
                    couleur = "Rouge"
                elif((iRed+30) > iGreen) and (iGreen > (iRed-30)):
                    #print("Gris : 1 euros")
                    piece = "1.00E"
                else:
                    #print("Jaune : 0,10 0,20 0,50 centimes ou 2 euros")
                    couleur = "Jaune"
                    for v in range(radius//8) :
                        for w in range(radius//16) :
                            histRed2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,0]] += 1
                            histGreen2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,1]] += 1
                            histBlue2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,2]] += 1
                    print("ROUGE2 :")
                    maxRed2 = 0
                    iRed2 = 0
                    for i in range(253):
                        if(histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3] > maxRed2):
                            maxRed2 = histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3]
                            iRed2 = i
                    print(maxRed2, iRed2)
                    print("VERT2 :")
                    maxGreen2 = 0
                    iGreen2 = 0
                    for i in range(253):
                        if(histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3] > maxGreen2):
                            maxGreen2 = histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3]
                            iGreen2 = i
                    print(maxGreen2, iGreen2)
                    print("BLEU2 :")
                    maxBlue2 = 0
                    iBlue2 = 0
                    for i in range(253):
                        if(histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3] > maxBlue2):
                            maxBlue2 = histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3]
                            iBlue2 = i
                    print(maxBlue2, iBlue2)
                    if((iRed2+30) > iGreen2) and (iGreen2 > (iRed2-30)):
                        #print("Il y a du gris : 2 euros")
                        piece = "2.00E"
                cv2.circle(src1, center, radius, (255, 0, 255), 3)
                cv2.imshow(file, src1)
                cv2.waitKey(0)
                
                tablab = []
                if piece != "" :
                    tabcoin.append(piece)
                else :
                    tabcoin.append(couleur)
                for x in data :                                 
                    value = x['label']
                    countP = countP + 1
                    if value == "0.50E" or value == "0.20E" or value == "0.10E" :
                        tablab.append("Jaune")    
                    elif value == "0.05E" or value == "0.02E" or value == "0.01E" :
                        tablab.append("Rouge")
                    else :
                        tablab.append(value)
                
                
                if len(tablab) == len(tabcoin) :
                    for i in range(len(tabcoin)) :
                        find = False 
                        for j in range(len(tablab)) :
                            print(i)
                            print(j)
                            print(len(tabcoin))
                            print(len(tablab))
                            print(tabcoin[i])
                            print(tablab[j])
                            if tabcoin[i] == tablab[j] and find == False :
                                finalP = finalP + 1
                                tablab.pop(j)
                                find = True
                
                    
                        

        
    elif file.endswith(".png"):
        countI = countI + 1
        s = file.split(".")[0]
        with open("DecoupageDonnees/JSON/"+s+".json") as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
    
        data = jsonObject['shapes']
        
        src1 = cv2.imread(cv2.samples.findFile(path + file), cv2.IMREAD_COLOR)
        src = cv2.cvtColor(src1,cv2.COLOR_BGR2RGB)
        plt.figure()
        plt.imshow(src)
        plt.show()
        histRed = [0] * 256
        histGreen = [0] * 256
        histBlue = [0] * 256
        histRed2 = [0] * 256
        histGreen2 = [0] * 256
        histBlue2 = [0] * 256
        couleur = ""
        piece = ""
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
            imgz = np.zeros((src.shape[0]//25, src.shape[1]//25), dtype = np.uint8)
            for c in circles[0, :]:
                piece = ""
                radius = c[2]
                center = (c[0], c[1])
                for x in range(imgz.shape[0]):
                    for y in range(imgz.shape[1]):
                        histRed[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,0]] += 1
                        histGreen[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,1]] += 1
                        histBlue[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,2]] += 1
                print("ROUGE :")
                maxRed = 0
                iRed = 0
                for i in range(253):
                    if(histRed[i] + histRed[i+1] + histRed[i+2] + histRed[i+3] > maxRed):
                        maxRed = histRed[i] + histRed[i+1] + histRed[i+2] + histRed[i+3]
                        iRed = i
                print(maxRed, iRed)
                print("VERT :")
                maxGreen = 0
                iGreen = 0
                for i in range(253):
                    if(histGreen[i] + histGreen[i+1] + histGreen[i+2] + histGreen[i+3] > maxGreen):
                        maxGreen = histGreen[i] + histGreen[i+1] + histGreen[i+2] + histGreen[i+3]
                        iGreen = i
                print(maxGreen, iGreen)
                print("BLEU :")
                maxBlue = 0
                iBlue = 0
                for i in range(253):
                    if(histBlue[i] + histBlue[i+1] + histBlue[i+2] + histBlue[i+3] > maxBlue):
                        maxBlue = histBlue[i] + histBlue[i+1] + histBlue[i+2] + histBlue[i+3]
                        iBlue = i
                print(maxBlue, iBlue)
                if(iBlue < 75):
                    #print("Jaune : 0,10 0,20 0,50 centimes ou 2 euros")
                    couleur = "Jaune"
                    for v in range(radius//8) :
                        for w in range(radius//16) :
                            histRed2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,0]] += 1
                            histGreen2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,1]] += 1
                            histBlue2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,2]] += 1
                    print("ROUGE2 :")
                    maxRed2 = 0
                    iRed2 = 0
                    for i in range(253):
                        if(histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3] > maxRed2):
                            maxRed2 = histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3]
                            iRed2 = i
                    print(maxRed2, iRed2)
                    print("VERT2 :")
                    maxGreen2 = 0
                    iGreen2 = 0
                    for i in range(253):
                        if(histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3] > maxGreen2):
                            maxGreen2 = histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3]
                            iGreen2 = i
                    print(maxGreen2, iGreen2)
                    print("BLEU2 :")
                    maxBlue2 = 0
                    iBlue2 = 0
                    for i in range(253):
                        if(histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3] > maxBlue2):
                            maxBlue2 = histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3]
                            iBlue2 = i
                    print(maxBlue2, iBlue2)
                    if((iRed2+30) > iGreen2) and (iGreen2 > (iRed2-30)):
                        print("Il y a du gris : 2 euros")
                        piece = "2.00E"
                elif(iGreen - 50 < 0 and iBlue - 50 < 0):
                    #print("Rouge : 0,01 0,02 0,05 centimes")
                    couleur = "Rouge"
                elif((iRed+30) > iGreen) and (iGreen > (iRed-30)):
                    #print("Gris : 1 euros")
                    piece = "1.00E"
                else:
                    #print("Jaune : 0,10 0,20 0,50 centimes ou 2 euros")
                    couleur = "Jaune"
                    for v in range(radius//8) :
                        for w in range(radius//16) :
                            histRed2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,0]] += 1
                            histGreen2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,1]] += 1
                            histBlue2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,2]] += 1
                    print("ROUGE2 :")
                    maxRed2 = 0
                    iRed2 = 0
                    for i in range(253):
                        if(histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3] > maxRed2):
                            maxRed2 = histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3]
                            iRed2 = i
                    print(maxRed2, iRed2)
                    print("VERT2 :")
                    maxGreen2 = 0
                    iGreen2 = 0
                    for i in range(253):
                        if(histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3] > maxGreen2):
                            maxGreen2 = histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3]
                            iGreen2 = i
                    print(maxGreen2, iGreen2)
                    print("BLEU2 :")
                    maxBlue2 = 0
                    iBlue2 = 0
                    for i in range(253):
                        if(histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3] > maxBlue2):
                            maxBlue2 = histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3]
                            iBlue2 = i
                    print(maxBlue2, iBlue2)
                    if((iRed2+30) > iGreen2) and (iGreen2 > (iRed2-30)):
                        #print("Il y a du gris : 2 euros")
                        piece = "2.00E"
                cv2.circle(src1, center, radius, (255, 0, 255), 3)
                cv2.imshow(file, src1)
                cv2.waitKey(0)
                
                for x in data :
                    value = x['label']
                    countP = countP + 1
                    if value == "0.50E" or value == "0.20E" or value == "0.10E" :
                        tablab.append("Jaune")    
                    elif value == "0.05E" or value == "0.02E" or value == "0.01E" :
                        tablab.append("Rouge")
                    else :
                        tablab.append(value)
                
                
                if len(tablab) == len(tabcoin) :
                    for i in range(len(tabcoin)) :
                        find = False 
                        for j in range(len(tablab)) :
                            if tabcoin[i] == tablab[j] and find == False :
                                finalP = finalP + 1
                                tablab.pop(j)
                                find = True
                    
    elif file.endswith(".jpg"):
        countI = countI + 1
        s = file.split(".")[0]
        with open("DecoupageDonnees/JSON/"+s+".json") as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
    
        data = jsonObject['shapes']
        
        src1 = cv2.imread(cv2.samples.findFile(path + file), cv2.IMREAD_COLOR)
        src = cv2.cvtColor(src1,cv2.COLOR_BGR2RGB)
        plt.figure()
        plt.imshow(src)
        plt.show()
        histRed = [0] * 256
        histGreen = [0] * 256
        histBlue = [0] * 256
        histRed2 = [0] * 256
        histGreen2 = [0] * 256
        histBlue2 = [0] * 256
        couleur = ""
        piece = ""
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
            imgz = np.zeros((src.shape[0]//25, src.shape[1]//25), dtype = np.uint8)
            for c in circles[0, :]:
                piece = ""
                radius = c[2]
                center = (c[0], c[1])
                for x in range(imgz.shape[0]):
                    for y in range(imgz.shape[1]):
                        histRed[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,0]] += 1
                        histGreen[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,1]] += 1
                        histBlue[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,2]] += 1
                print("ROUGE :")
                maxRed = 0
                iRed = 0
                for i in range(253):
                    if(histRed[i] + histRed[i+1] + histRed[i+2] + histRed[i+3] > maxRed):
                        maxRed = histRed[i] + histRed[i+1] + histRed[i+2] + histRed[i+3]
                        iRed = i
                print(maxRed, iRed)
                print("VERT :")
                maxGreen = 0
                iGreen = 0
                for i in range(253):
                    if(histGreen[i] + histGreen[i+1] + histGreen[i+2] + histGreen[i+3] > maxGreen):
                        maxGreen = histGreen[i] + histGreen[i+1] + histGreen[i+2] + histGreen[i+3]
                        iGreen = i
                print(maxGreen, iGreen)
                print("BLEU :")
                maxBlue = 0
                iBlue = 0
                for i in range(253):
                    if(histBlue[i] + histBlue[i+1] + histBlue[i+2] + histBlue[i+3] > maxBlue):
                        maxBlue = histBlue[i] + histBlue[i+1] + histBlue[i+2] + histBlue[i+3]
                        iBlue = i
                print(maxBlue, iBlue)
                if(iBlue < 75):
                    #print("Jaune : 0,10 0,20 0,50 centimes ou 2 euros")
                    couleur = "Jaune"
                    for v in range(radius//8) :
                        for w in range(radius//16) :
                            histRed2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,0]] += 1
                            histGreen2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,1]] += 1
                            histBlue2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,2]] += 1
                    print("ROUGE2 :")
                    maxRed2 = 0
                    iRed2 = 0
                    for i in range(253):
                        if(histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3] > maxRed2):
                            maxRed2 = histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3]
                            iRed2 = i
                    print(maxRed2, iRed2)
                    print("VERT2 :")
                    maxGreen2 = 0
                    iGreen2 = 0
                    for i in range(253):
                        if(histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3] > maxGreen2):
                            maxGreen2 = histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3]
                            iGreen2 = i
                    print(maxGreen2, iGreen2)
                    print("BLEU2 :")
                    maxBlue2 = 0
                    iBlue2 = 0
                    for i in range(253):
                        if(histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3] > maxBlue2):
                            maxBlue2 = histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3]
                            iBlue2 = i
                    print(maxBlue2, iBlue2)
                    if((iRed2+30) > iGreen2) and (iGreen2 > (iRed2-30)):
                        #print("Il y a du gris : 2 euros")
                        piece = "2.00E"
                elif(iGreen - 50 < 0 and iBlue - 50 < 0):
                    #print("Rouge : 0,01 0,02 0,05 centimes")
                    couleur = "Rouge"
                elif((iRed+30) > iGreen) and (iGreen > (iRed-30)):
                    #print("Gris : 1 euros")
                    piece = "1.00E"
                else:
                    #print("Jaune : 0,10 0,20 0,50 centimes ou 2 euros")
                    couleur = "Jaune"
                    for v in range(radius//8) :
                        for w in range(radius//16) :
                            histRed2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,0]] += 1
                            histGreen2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,1]] += 1
                            histBlue2[src[(c[1]-imgz.shape[0]//2)+x,(c[0]-imgz.shape[1]//2)-y,2]] += 1
                    print("ROUGE2 :")
                    maxRed2 = 0
                    iRed2 = 0
                    for i in range(253):
                        if(histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3] > maxRed2):
                            maxRed2 = histRed2[i] + histRed2[i+1] + histRed2[i+2] + histRed2[i+3]
                            iRed2 = i
                    print(maxRed2, iRed2)
                    print("VERT2 :")
                    maxGreen2 = 0
                    iGreen2 = 0
                    for i in range(253):
                        if(histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3] > maxGreen2):
                            maxGreen2 = histGreen2[i] + histGreen2[i+1] + histGreen2[i+2] + histGreen2[i+3]
                            iGreen2 = i
                    print(maxGreen2, iGreen2)
                    print("BLEU2 :")
                    maxBlue2 = 0
                    iBlue2 = 0
                    for i in range(253):
                        if(histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3] > maxBlue2):
                            maxBlue2 = histBlue2[i] + histBlue2[i+1] + histBlue2[i+2] + histBlue2[i+3]
                            iBlue2 = i
                    print(maxBlue2, iBlue2)
                    if((iRed2+30) > iGreen2) and (iGreen2 > (iRed2-30)):
                        #print("Il y a du gris : 2 euros")
                        piece = "2.00E"
                cv2.circle(src1, center, radius, (255, 0, 255), 3)
                cv2.imshow(file, src1)
                cv2.waitKey(0)
                for x in data :
                    value = x['label']
                    countP = countP + 1
                    if value == "0.50E" or value == "0.20E" or value == "0.10E" :
                        tablab.append("Jaune")    
                    elif value == "0.05E" or value == "0.02E" or value == "0.01E" :
                        tablab.append("Rouge")
                    else :
                        tablab.append(value)
                
                
                if len(tablab) == len(tabcoin) :
                    for i in range(len(tabcoin)) :
                        find = False 
                        for j in range(len(tablab)) :
                            if tabcoin[i] == tablab[j] and find == False :
                                finalP = finalP + 1
                                tablab.pop(j)
                                find = True
                    if len(labtab) == 0 :
                        finalI = finalI + 1
                        
PourcentageP = finalP / countP 
PourcentageI = finalI / countI

print("Notre algorithme a un taux de réussite de " + PourcentageP + " % sur les pièces" \n)
print("Et il a un taux de réussite de " + PourcentageI + " % sur les images" \n)
                    
                    
