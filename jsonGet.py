
import json
import os

path = "DecoupageDonnees/Test/"

dirs = os.listdir(path)
count = 0
win = 0
final = 0
for file in dirs:
    count = count + 1
    s = file.split(".")[0]
    couleur = "Jaune"
    progValue = '0.50E'
    with open(s.json) as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    
    data = jsonObject['shapes']
    piece = ""
    for x in data :
        value = x['label']
        print(value)
        if piece != "" : 
            if piece == "2.00E" and piece == value :
                win = win + 1
                piece = "C'est une pièce de 2 euros"
            elif piece == value :
                win = win + 1
                piece = "C'est une pièce d'1 euros"

        elif couleur == "Jaune" :
            piece = "C'est une pièce de 50 centimes, de 20 centimes, ou de 10 centimes"
            if value == "0.50E" :
                win = win + 1

            elif value == "0.20E" :
                win = win + 1

            elif value == "0.10E" :
                win = win + 1

        elif couleur == "Rouge" :
            piece = "C'est une pièce de 5 centimes, de 2 centimes, ou d'1 centime"
            if value == "0.05E" :
                win = win + 1
                        
            elif value == "0.02E" :
                win = win + 1

            elif value == "0.01E" :
                win = win + 1
    
    if win >= 1 :
        final = final + 1

Pourcentage = final / count 

print("Notre algorithme a un taux de réussite de " + Pourcentage + " %")


