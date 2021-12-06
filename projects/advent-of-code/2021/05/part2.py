import os
import re
import math

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def findStep(offset):
  return 0 if offset == 0 else int(math.copysign(1, offset))

vents = {}
intersections = 0

with open(inputPath) as file:
  lines = file.read().splitlines()

for line in lines:
  x1, y1, x2, y2 = list(map(int, (re.findall('\d+', line))))

  xOffset = x2 - x1
  xStep = findStep(xOffset)

  yOffset = y2 - y1
  yStep = findStep(yOffset)

  distance = max(abs(xOffset), abs(yOffset))

  x = x1
  y = y1
  for _ in range(distance + 1):
    key = "{0},{1}".format(x, y)

    vents[key] = vents[key] + 1 if key in vents else 1

    if vents[key] == 2:
      intersections += 1

    x += xStep
    y += yStep

print(str(intersections) + ' vents intersect.')
