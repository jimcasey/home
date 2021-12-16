import os
import sys
import time

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
options = {}

while True:
  for neighbor in getNeighbors(current):
    if not visited[neighbor]:
      distance[neighbor] = min(
          distance[neighbor] if neighbor in distance else sys.maxsize,
          distance[current] + density[neighbor]
      )
      options[neighbor] = distance[neighbor]

  if current == destination:
    break

  visited[current] = True
  options.pop(current, None)

  minDistance = sys.maxsize
  for key, value in options.items():
    if value < minDistance:
      current = key
      minDistance = value

print(f'Shortest distance is {distance[destination]}.')
