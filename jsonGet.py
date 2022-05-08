import json
progValue = '0.50E'
win = 0
with open("DecoupageDonnees/Test/1.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
 
data = jsonObject['shapes']
for x in data :
    value = x['label']
    print(value)
    if progValue == value :
        win = win + 1
print(win)
