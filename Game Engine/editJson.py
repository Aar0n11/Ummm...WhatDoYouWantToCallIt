import json
from Game_Engine.py import datafile

datafile = datafile()

def editJson(dataField, newData):
    with open(datafile, 'r') as file:
        fileData = json.load(file)

        field = fileData.pop(dataField)
        fileData[newData] = field

        newData = json.dumps(fileData)

    with open(datafile, 'w') as file:
        file.truncate(0)
        file.write(newData)