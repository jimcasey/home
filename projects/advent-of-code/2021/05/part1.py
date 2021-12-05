import os
import re

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def toInts(arr):
  return list(map(int, arr))

def createKey(x, y):
  return "{},{}".format(x, y)

vents = {}
maxX = 0
maxY = 0

with open(inputPath) as file:
  for line in file.read().splitlines():
    points = toInts(re.findall('\d+', line))
    x1, y1 = points[0:2]
    x2, y2 = points[2:4]
    if (x1 == x2):
      step = 1 if y1 < y2 else -1
      for y in range(y1, y2 + step, step):
        maxX = max(maxX, x1)
        maxY = max(maxY, y)
        key = createKey(x1, y)
        vents[key] = vents[key] + 1 if key in vents else 1
    if (y1 == y2):
      step = 1 if x1 < x2 else -1
      for x in range(x1, x2 + step, step):
        maxX = max(maxX, x)
        maxY = max(maxY, y1)
        key = createKey(x, y1)
        vents[key] = vents[key] + 1 if key in vents else 1

count = 0
for value in vents.values():
  if value > 1:
    count += 1

print('{} vent lines intersect.'.format(count))
