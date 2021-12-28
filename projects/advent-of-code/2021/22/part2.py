from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def main():
  steps = readInput()

  cubes = []
  for enabled, cube in steps:
    for existingEnabled, existingCube in cubes.copy():
      intersectCube = intersect(cube, existingCube)
      if intersectCube:
        cubes.append((existingEnabled != True, intersectCube))

    if enabled:
      cubes.append((True, cube))

  vol = 0
  for enabled, cube in cubes:
    vol += volume(cube) * (1 if enabled else -1)

  print(f'{vol} cubes are on.')

def intersect(cubeA, cubeB):
  cube = ([0] * 3, [0] * 3)

  for i in range(3):
    cube[0][i] = max(cubeA[0][i], cubeB[0][i])
    cube[1][i] = min(cubeA[1][i], cubeB[1][i])
    if cube[0][i] > cube[1][i]:
      return False

  return tuple(map(tuple, cube))

def volume(cube):
  (x1, y1, z1), (x2, y2, z2) = cube
  return (x2 - x1) * (y2 - y1) * (z2 - z1)

def readInput():
  with open(inputPath) as file:
    def parseLine(line):
      reStr = '(-?\d+)\.\.(-?\d+)'
      reStr = f'(on|off) x={reStr},y={reStr},z={reStr}'
      items = re.match(reStr, line).groups()
      enable = True if items[0] == 'on' else False
      x1, x2, y1, y2, z1, z2 = map(int, items[1:])

      return (
          enable,
          (
              (x1, y1, z1),
              (x2 + 1, y2 + 1, z2 + 1),
          )
      )
    return tuple(map(parseLine, file.read().splitlines()))

main()
