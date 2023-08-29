import os
import json

path = os.getcwd()
parent = os.path.dirname(path)
mainFolder = os.path.dirname(parent)

dataFile = 'mainFolder/settings.json'
data = json.load(dataFile)

position = [data['characterPositionX'], data['characterPositionY']]

def addGravity(speed, direction):
    if(direction = 'x'):
        position[0] = position[0] + speed

    elif(direction = 'y'):
        position[1] = position[1] + speed

    elif(direction = '-x'):
        position[0] = position[0] - speed

    elif(direction = '-y'):
        position[1] = position[1] - speed

    return(position)