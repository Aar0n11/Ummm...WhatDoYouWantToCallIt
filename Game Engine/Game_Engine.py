import os
import json
import time
import keyboard



path = os.getcwd()
parent = os.path.dirname(path)

settings = open(parent + '/settings.json')
settingsData = json.load(settings)

processSpeed = 0.1

def move(key):
        print(key)
        time.sleep(processSpeed)

keyboard.add_hotkey("a", lambda: move("a"))
keyboard.add_hotkey("d", lambda: move("d"))
keyboard.add_hotkey("w", lambda: move("w"))
keyboard.add_hotkey("s", lambda: move("s"))