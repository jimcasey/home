import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'
with open(inputPath) as file:
  def parseLine(line): return list(map(int, line))
  heightmap = list(map(parseLine, file.read().splitlines()))

width = len(heightmap[0])
height = len(heightmap)

vectors = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def getOffsets(y, x):
  offsets = []
  for v in vectors:
    vy, vx = v
    oy = y - vy
    if oy < 0 or oy >= height:
      continue
    ox = x - vx
    if ox < 0 or ox >= width:
      continue
    offsets.append([oy, ox])
  return offsets

lowPoints = []
for y in range(height):
  for x in range(width):
    value = heightmap[y][x]
    lowPoint = True
    for o in getOffsets(y, x):
      oy, ox = o
      if value >= heightmap[oy][ox]:
        lowPoint = False
        break
    if lowPoint:
      lowPoints.append(value)

riskLevelSum = 0
for value in lowPoints:
  riskLevelSum += value + 1

print('Sum of the risk levels is {0}'.format(riskLevelSum))
