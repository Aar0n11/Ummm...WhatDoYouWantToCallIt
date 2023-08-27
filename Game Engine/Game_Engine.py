from editJson import editThatJson
import os
import json
import time
import keyboard

path = os.getcwd()
parent = os.path.dirname(path)

settings = open(parent + '\settings.json')
settingsData = json.load(settings)

dataFile = open(parent + '\data.json')
data = json.load(dataFile)

processSpeed = settingsData['speed']

size = [settingsData['width'], settingsData['height']]

defaultPosition = [data['charDefaultX'], data['charDefaultY']]

position = [0,0]

with open(parent + '\data.json', 'r') as file:
    fileData = json.load(file)

    fileData.pop('charPositionX')
    fileData.pop('charPositionY')

    fileData["charPositionX"] = defaultPosition[0]
    fileData["charPositionY"] = defaultPosition[1]

    newData = json.dumps(fileData)

with open(parent + '\data.json', 'w') as file:
    file.truncate(0)
    file.write(newData)

def move(direction):
        if(direction == "forward"):
            position[1] = position[1] + 5
            time.sleep(processSpeed)

            if(position[1] > size[0]):
                position[1] = size[0]

        elif(direction == "backward"):
            position[1] = position[1] - 5
            time.sleep(processSpeed)

            if(position[1] < (size[0] - (size[0]*2))):
                position[1] = (size[0] - (size[0]*2))

        elif(direction == "left"):
            position[0] = position[0] - 5
            time.sleep(processSpeed)

            if(position[0] < (size[1] - (size[1]*2))):
                position[0] = (size[1] - (size[1]*2))

        elif(direction == "right"):
            position[0] = position[0] + 5
            time.sleep(processSpeed)

            if(position[0] > size[1]):
                position[0] = size[1]    

keyboard.add_hotkey(settingsData['leftKey'], lambda: move("left"))
keyboard.add_hotkey(settingsData['rightKey'], lambda: move("right"))
keyboard.add_hotkey(settingsData['forwardKey'], lambda: move("forward"))
keyboard.add_hotkey(settingsData['backwardKey'], lambda: move("backward"))

while True:
    print(position)

    editThatJson('charPositionX', position[0])
    editThatJson('charPositionY', position[1])

    time.sleep(processSpeed)