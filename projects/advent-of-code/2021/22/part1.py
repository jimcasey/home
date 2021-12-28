from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def main():
  steps = readInput()

  inRange = (lambda value: -50 <= value and value <= 50)

  on = set()
  for step in steps:
    operation, (x1, x2), (y1, y2), (z1, z2) = step
    for x in range(x1, x2 + 1):
      if inRange(x):
        for y in range(y1, y2 + 1):
          if inRange(y):
            for z in range(z1, z2 + 1):
              if inRange(z):
                key = f'{x},{y},{z}'
                if operation:
                  on.add(key)
                elif key in on:
                  on.remove(key)

  print(f'{len(on)} cubes are on.')

def readInput():
  with open(inputPath) as file:
    def parseLine(line):
      rangeRe = '(-?\d+)\.\.(-?\d+)'
      reStr = f'(on|off) x={rangeRe},y={rangeRe},z={rangeRe}'
      items = re.match(reStr, line).groups()
      operation = True if items[0] == 'on' else False
      x1, x2, y1, y2, z1, z2 = map(int, items[1:])

      return (
          operation,
          (x1, x2),
          (y1, y2),
          (z1, z2)
      )
    return tuple(map(parseLine, file.read().splitlines()))

main()
