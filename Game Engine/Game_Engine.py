import os
import json
import time
from turtle import forward
import keyboard

path = os.getcwd()
parent = os.path.dirname(path)

settings = open(parent + '\settings.json')
settingsData = json.load(settings)

processSpeed = settingsData['speed']

def move(key):
        print(key)
        time.sleep(processSpeed)

keyboard.add_hotkey(settingsData['leftKey'], lambda: move("a"))
keyboard.add_hotkey(settingsData['rightKey'], lambda: move("d"))
keyboard.add_hotkey(settingsData['forwardKey'], lambda: move("w"))
keyboard.add_hotkey(settingsData['backwardKey'], lambda: move("s"))