import os
import sys

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  lines = file.read().splitlines()

density = {}
distance = {}
unvisited = []

offsets = [[0, -1], [1, 0], [0, 1], [-1, 0]]
def getNeighbors(key):
  x, y = list(map(int, key.split(',')))
  return [f'{x + oX},{y + oY}' for oX, oY in offsets]

for y, line in enumerate(lines):
  for x, c in enumerate(line):
    key = f'{x},{y}'
    density[key] = int(c)
    distance[key] = sys.maxsize
    unvisited.append(key)

destination = f'{len(lines[0]) - 1},{len(lines) - 1}'
current = '0,0'
distance[current] = 0

while True:
  for neighbor in getNeighbors(current):
    if neighbor in unvisited:
      distance[neighbor] = min(
          distance[neighbor],
          distance[current] + density[neighbor]
      )

  unvisited.remove(current)

  if current == destination:
    break

  current = unvisited[0]
  minDistance = distance[current]
  for key in unvisited:
    if distance[key] < minDistance:
      current = key
      minDistance = distance[key]

print(f'Shortest distance is {distance[destination]}.')
