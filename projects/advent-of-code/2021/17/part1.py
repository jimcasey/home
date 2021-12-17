import os
import re

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  input = file.read()

  reStr = 'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)'
  lowerX, upperX, upperY, lowerY = list(map(
      int,
      re.match(reStr, input).group(1, 2, 3, 4))
  )

def inTarget(pos):
  x, y = pos
  if upperX < x or upperY > y:
    raise(OvershotError())
  return lowerX <= x and lowerY >= y

def step(pos, vel):
  posX, posY = pos
  velX, velY = vel
  newPos = [posX + velX, posY + velY]
  newVel = [
      velX - 1 if velX > 0 else velX + 1 if velX < 0 else 0,
      velY - 1
  ]
  return [newPos, newVel]

class OvershotError(Exception):
  pass

def findMaxY(vel):
  pos = [0, 0]
  maxY = pos[0]
  while True:
    pos, vel = step(pos, vel)
    maxY = max(maxY, pos[1])
    if inTarget(pos):
      return maxY

maxY = 0
for velY in range(1000):
  for velX in range(1000):
    try:
      maxY = max(maxY, findMaxY([velX, velY]))
    except OvershotError:
      pass

print(f"The highest point in the probe's tragectory is {maxY}.")
