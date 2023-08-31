from editJson import editThatJson
import json
import os

path = os.getcwd()
parent = os.path.dirname(path)

dataFile = open(parent + '\data.json')
data = json.load(dataFile)

def spawnEntity(object, name, position):


    editThatJson(object, name, position, "add")