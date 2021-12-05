import os
import re

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def toInts(arr):
  return list(map(int, arr))

def createKey(x, y):
  return "{},{}".format(x, y)

def findStep(offset):
  if offset < 0:
    return -1
  if offset > 0:
    return 1
  return 0

vents = {}
maxX = 0
maxY = 0

with open(inputPath) as file:
  for line in file.read().splitlines():
    points = toInts(re.findall('\d+', line))

    x1, y1 = points[0:2]
    x2, y2 = points[2:4]

    xOffset = x2 - x1
    xStep = findStep(xOffset)

    yOffset = y2 - y1
    yStep = findStep(yOffset)

    distance = max(abs(xOffset), abs(yOffset)) + 1

    x = x1
    y = y1
    for _ in range(distance):
      maxX = max(maxX, x)
      maxY = max(maxY, y)
      key = createKey(x, y)
      vents[key] = vents[key] + 1 if key in vents else 1
      x += xStep
      y += yStep

count = 0
for value in vents.values():
  if value > 1:
    count += 1

print(str(count) + ' vent lines intersect.')
