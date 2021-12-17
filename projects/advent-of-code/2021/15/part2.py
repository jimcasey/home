import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  lines = file.read().splitlines()

density = {}
visited = {}

maxX = 0
maxY = 0
for y, line in enumerate(lines):
  for x, c in enumerate(line):
    for offsetY in range(5):
      for offsetX in range(5):
        nodeX = x + offsetX * len(lines[0])
        nodeY = y + offsetY * len(lines)
        key = f'{nodeX},{nodeY}'
        value = int(c) + offsetY + offsetX
        density[key] = value if value <= 9 else value - 9
        visited[key] = False
        maxX = max(nodeX, maxX)
        maxY = max(nodeY, maxY)

offsets = [[0, -1], [1, 0], [0, 1], [-1, 0]]
def getNeighbors(key):
  x, y = list(map(int, key.split(',')))
  neighbors = []
  for oX, oY in offsets:
    nX = x + oX
    nY = y + oY
    if 0 <= nX and nX <= maxX and 0 <= nY and nY <= maxY:
      neighbors.append(f'{nX},{nY}')
  return neighbors

destination = f'{maxX},{maxY}'
current = '0,0'
distance = {}
distance[current] = 0

class Options:
  __map = {}

  def set(self, key, value):
    try:
      arr = self.__map[value]
    except KeyError:
      arr = self.__map[value] = []
    arr.append(key)

  def remove(self, key, value):
    try:
      self.__map[value].remove(key)
      if len(self.__map[value]) == 0:
        self.__map.pop(value)
    except (KeyError, ValueError):
      pass

  def next(self):
    value = self.__map[min(self.__map.keys())][0]
    return value

options = Options()

while True:
  for neighbor in getNeighbors(current):
    if not visited[neighbor]:
      currentDistance = distance[current] + density[neighbor]
      try:
        neighborDistance = distance[neighbor]
        options.remove(neighbor, neighborDistance)
        distance[neighbor] = min(currentDistance, neighborDistance)
      except KeyError:
        distance[neighbor] = currentDistance

      options.set(neighbor, distance[neighbor])

  if current == destination:
    break

  visited[current] = True
  options.remove(current, distance[current])

  current = options.next()

print(f'Shortest distance is {distance[destination]}.')
