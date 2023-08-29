from bin.add_force import addForce
from bin.editJson import editThatJson
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

playerHeight = data['character']['height']
playerWidth = data['character']['width']

playerState = data['character']['state']

def handleSpeed():
    if(processSpeed != 0):
        time.sleep(processSpeed)

def handleState(playerState):
    if(playerState = "idle"):
        canJump = True

    elif(playerState = "jumping"):
        gravity = False

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
        if(direction == "left"):
            position[0] = position[0] - 5
            playerState = "running"

            if(position[0] < (0 - size[1] + playerWidth)):
                position[0] = (0 - size[1] + playerWidth)

        elif(direction == "right"):
            position[0] = position[0] + 5
            playerState = "running"

            if(position[0] > (size[1] - playerWidth):
                position[0] = (size[1] - playerWidth)

        elif(direction == "jump"):
            if(canJump == True):
                for i in range(10)
                    position[1] = position[1] + 1

        else:
            playerState = "idle"

        handleState(playerState)

keyboard.add_hotkey(settingsData['leftKey'], lambda: move("left"))
keyboard.add_hotkey(settingsData['rightKey'], lambda: move("right"))
keyboard.add_hotkey(settingsData['forwardKey'], lambda: move("jump"))

while True:
    print(position)

    editThatJson("character", 'charPositionX', position[0])
    editThatJson('charPositionY', position[1])

    handleSpeed()

    editThatJson("character", "state", playerState)

    if(gravity != False):
        addForce("gravity", 1, "-y", "char")