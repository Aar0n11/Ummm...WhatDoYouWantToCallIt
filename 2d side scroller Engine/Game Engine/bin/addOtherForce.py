import os
import json

path = os.getcwd()
parent = os.path.dirname(path)

dataFile = parent + "/data.json"
data = json.load(dataFile)

settingsFile = parent + "/settings.json"
settings = json.load(settingsFile)

position = [data['characterPositionX'], data['characterPositionY']]

friction = settings['friction']

def addOtherForce(amount, direction):
    if(friction == "true"):
        for i in range(amount/3):
            if(direction = 'x'):
                position[0] = position[0] + 2

            elif(direction = 'y'):
                position[1] = position[1] + 2

            elif(direction = 'x'):
                position[0] = position[0] -2

            elif(direction = 'y'):
                position[1] = position[1] -2

        for i in range(2(amount/3)):
            if(direction = 'x'):
                position[0] = position[0] + 1

            elif(direction = 'y'):
                position[1] = position[1] + 1

            elif(direction = 'x'):
                [0] = position[0] -1

            elif(direction = 'y'):
                position[1] = position[1] -1

    else:
        for i in range(amount)):
            if(direction = 'x'):
                position[0] = position[0] + 1

            elif(direction = 'y'):
                position[1] = position[1] + 1

            elif(direction = 'x'):
                position[0] = position[0] -1

            elif(direction = 'y'):
                position[1] = position[1] -1

    return(position)