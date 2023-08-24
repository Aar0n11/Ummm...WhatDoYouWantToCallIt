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
            print(position)
        time.sleep(processSpeed)

keyboard.add_hotkey(settingsData['leftKey'], lambda: move("left"))
keyboard.add_hotkey(settingsData['rightKey'], lambda: move("right"))
keyboard.add_hotkey(settingsData['forwardKey'], lambda: move("forward"))
keyboard.add_hotkey(settingsData['backwardKey'], lambda: move("backward"))