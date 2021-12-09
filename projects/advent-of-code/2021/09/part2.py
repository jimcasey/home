import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  def parseLine(line): return list(map(int, line))
  input = list(map(parseLine, file.read().splitlines()))

vectors = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def getOffsets(y, x):
  offsets = []
  for vector in vectors:
    vectorY, vectorX = vector
    offsetY = y - vectorY
    if offsetY < 0 or offsetY >= height:
      continue
    offsetX = x - vectorX
    if offsetX < 0 or offsetX >= width:
      continue
    offsets.append([offsetY, offsetX])
  return offsets

def getCoord(y, x): return '{0},{1}'.format(y, x)

width = len(input[0])
height = len(input)
heightMap = {}

for y in range(height):
  for x in range(width):
    coord = getCoord(y, x)
    heightMap[coord] = {
        'value': input[y][x],
        'adjacent': {}
    }
    for offset in getOffsets(y, x):
      offsetY, offsetX = offset
      adjacentCoord = getCoord(offsetY, offsetX)
      heightMap[coord]['adjacent'][adjacentCoord] = input[offsetY][offsetX]

lowPoints = []
for coord, entry in heightMap.items():
  lowPoint = True
  for adjacentValue in entry['adjacent'].values():
    if adjacentValue <= entry['value']:
      lowPoint = False
      break
  if lowPoint:
    lowPoints.append(coord)

def findBasin(coord, basin):
  basin.append(coord)
  for adjacentCoord, adjacentValue in heightMap[coord]['adjacent'].items():
    if adjacentValue == 9 or adjacentCoord in basin:
      continue
    findBasin(adjacentCoord, basin)
  return basin

basins = [findBasin(coord, []) for coord in lowPoints]
basinLengths = sorted(list(map(len, basins)), reverse=True)

product = None
for index in range(3):
  length = basinLengths[index]
  product = length if not product else product * length

print('Product of the three largest basins is {0}.'.format(product))
