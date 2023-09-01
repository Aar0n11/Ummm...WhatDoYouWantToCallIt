from PIL import Image
import os
import json

path = os.getcwd()
parent = os.path.dirname(path)

settingsFile = open(parent + '\settings.json')
settings = json.load(settingsFile)

areaWidth = settings['width']
areaHeight = settings['height']

path = parent + "/ground.png"

columnWidth = 5

array = []

def raycast(columnpos, image):
    count = 0

    ray = [columnpos, areaHeight]

    for ray in range(areaHeight):
        ray[1] = ray[1] - 1

        color = image.getpixel(ray)

        if(color[2] == 1):
            count = count + 1

def main():
    try: 
        image = Image.open(path).convert('L')

        for(i) in range(areaWidth):
            raycast(i/columnWidth, image)
            array.append(count)
            count = 0
    except IOError:
        pass

if __name__ == "__main__":
    main()