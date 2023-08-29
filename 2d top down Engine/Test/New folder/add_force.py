from gravity import addGravity
from editJson import editThatJson

def addForce(type, strength, direction, entity):
    if(type == "gravity"):
        gravity(strength, direction, entity)


def gravity(strength, direction, entity):
    addGravity(strength, direction)
    entityCoords = addGravity(strength, direction, entity)

    writeJson(entityCoords, entity)

def writeJson(coords, entity):
    editThatJson(entity, coords[0])
    editThatJson(entity, coords[1])