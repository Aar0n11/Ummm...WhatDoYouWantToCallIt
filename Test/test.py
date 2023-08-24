import os
import json
import time
from turtle import forward
import keyboard

path = os.getcwd()
parent = os.path.dirname(path)

settings = open(parent + '\settings.json')
settingsData = json.load(settings)

dataFile = open(parent + '\settings.json')
data = json.load(dataFile)

processSpeed = settingsData['speed']

position = [0, 0]

def move(direction):
        if(direction == "forward"):
            position[1] = position[1] + 5
            time.sleep(processSpeed)

        elif(direction == "backward"):
            position[1] = position[1] - 5
            time.sleep(processSpeed)

        elif(direction == "left"):
            position[0] == position[0] - 5
            time.sleep(processSpeed)

        elif(direction == "right"):
            position[0] == position[0] + 5
            time.sleep(processSpeed)

        else:
            move()

        

keyboard.add_hotkey(settingsData['leftKey'], lambda: move("left"))
keyboard.add_hotkey(settingsData['rightKey'], lambda: move("right"))
keyboard.add_hotkey(settingsData['forwardKey'], lambda: move("forward"))
keyboard.add_hotkey(settingsData['backwardKey'], lambda: move("backward"))