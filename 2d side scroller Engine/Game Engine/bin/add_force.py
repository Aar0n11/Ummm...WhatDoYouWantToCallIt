from gravity import addGravity
from addOtherForce import addOtherForce
from editJson import editThatJson
import os
import json

path = os.getcwd()
parent = os.path.dirname(path)

dataFile = open(parent + '\data.json')
data = json.load(dataFile)

playerState = data['character']['state']

def addForce(type, strength, direction, entity):
    if(type == "gravity"):
        gravity(strength, direction, entity)

    if(type == "other"):
        otherForce(strength, direction, entity)


def gravity(strength, direction, entity):
    if(playerState != "jumping"):
        entityCoords = addGravity(strength, direction)

    writeJson(entityCoords, entity)

def otherForce(strength, direction, entity):
    entityCoords = addOtherForce(strength, direction)

    writeJson(direction, entityCoords, entity)

def writeJson(direction, coords, entity):
    if(direction == "x"):
        editThatJson(entity, entity + "PositionX",coords[0])

    elif(direction == "-x"):
        editThatJson(entity, entity + "PositionX",coords[0])

    elif(direction == "y"):
        editThatJson(entity, entity + "PositionY", coords[1])

    elif(direction == "-y"):
        editThatJson(entity, entity + "PositionY",coords[1])