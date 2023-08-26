import os
import json
import time
import keyboard

path = os.getcwd()
parent = os.path.dirname(path)

settings = open(parent + '\settings.json')
settingsData = json.load(settings)

dataFile = open(parent + '\settings.json')
data = json.load(dataFile)

processSpeed = settingsData['speed']
print(processSpeed)

size = [settingsData['width'], settingsData['height']]

position = [0, 0]

def move(direction):
        if(direction == "forward"):
            position[1] = position[1] + 5
            time.sleep(processSpeed)

            if(position[1] > size[0]):
                position[1] = size[0]

        elif(direction == "backward"):
            position[1] = position[1] - 5
            time.sleep(processSpeed)

            if(position[1] > (size[0] - (size[0]*2))):
                position[1] = (size[0] - (size[0]*2))

        elif(direction == "left"):
            position[0] = position[0] - 5
            time.sleep(processSpeed)

            if(position[0] > size[1]):
                position[0] = size[1]

        elif(direction == "right"):
            position[0] = position[0] + 5
            time.sleep(processSpeed)

            if(position[0] > (size[1] - (size[1]*2))):
                position[0] = (size[1] - (size[1]*2))

keyboard.add_hotkey(settingsData['leftKey'], lambda: move("left"))
keyboard.add_hotkey(settingsData['rightKey'], lambda: move("right"))
keyboard.add_hotkey(settingsData['forwardKey'], lambda: move("forward"))
keyboard.add_hotkey(settingsData['backwardKey'], lambda: move("backward"))

while True:
    print(position)
    time.sleep(0.1)