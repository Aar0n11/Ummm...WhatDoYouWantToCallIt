import json
import os

path = os.getcwd()
parent = os.path.dirname(path)

dataFile = parent + '\data.json'

def editThatJson(object, dataField, newData, type):
    with open(dataFile, 'r') as file:
        fileData = json.load(file)

        if type == "edit":
            fileData.pop(dataField)
            fileData[object][dataField] = newData
            newData = json.dumps(fileData)

        elif type == "add":
            fileData[object][dataField] = newData

    with open(dataFile, 'w') as file:
        if type == "edit":
            file.truncate(0)


        file.seek(len(file) - 1)
        file.write(newData)