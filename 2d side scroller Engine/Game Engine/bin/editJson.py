import json
import os

path = os.getcwd()
parent = os.path.dirname(path)

dataFile = parent + '\data.json'

def editThatJson(object, dataField, newData):
    with open(dataFile, 'r') as file:
        fileData = json.load(file)

        fileData.pop(dataField)

        fileData[object][dataField] = newData

        newData = json.dumps(fileData)

    with open(dataFile, 'w') as file:
        file.truncate(0)
        file.write(newData)