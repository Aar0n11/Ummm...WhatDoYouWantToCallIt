from bin.editJson import editThatJson
import os
import json

path = os.getcwd()
parent = os.path.dirname(path)

newDataFile = parent + '\data.json'
newSettingsFile = parent + 'settings.json'

dataFile = '\data.json'
settingsFile = 'settings.json'

def copyThatJson():
    with open(dataFile, 'r') as file:
        fileData = json.load(file)
        newData = json.dumps(fileData)

    with open(newDataFile, 'w') as file:
        file.truncate(0)
        file.write(newData)

    with open(settingsFile, 'r') as file2:
        fileData2 = json.load(file2)
        newData2 = json.dumps(fileData2)

    with open(newSettingsFile, 'w') as file2:
        file.truncate(0)
        file.write(newData2)