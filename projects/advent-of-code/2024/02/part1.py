from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  unsafe = 0
  for line in lines:
    last = None
    direction = None
    for match in re.findall(r"\d+", line):
      current = int(match)

      if last is not None:
        if last < current:
          currentDirection = 'up'
        else:
          currentDirection = 'down'

        if direction is None:
          direction = currentDirection
        elif direction != currentDirection:
          unsafe += 1
          break

        diff = abs(current - last)
        if diff < 1 or 3 < diff:
          unsafe += 1
          break

      last = current

  print(len(lines) - unsafe)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
