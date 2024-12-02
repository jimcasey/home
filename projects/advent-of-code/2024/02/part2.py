from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def findDirection(a, b):
  if a < b:
    return 'up'
  else:
    return 'down'


def isSafe(levels):
  lastLevel = levels[0]
  lastDirection = findDirection(levels[0], levels[1])

  for i in range(1, len(levels)):
    currentLevel = levels[i]
    currentDirection = findDirection(lastLevel, currentLevel)
    diff = abs(lastLevel - currentLevel)
    if diff < 1 or 3 < diff or lastDirection != currentDirection:
      return False
    lastLevel = currentLevel
    lastDirection = currentDirection

  return True


def main():
  lines = readInput()
  safe = 0
  for line in lines:
    levels = list(map(int, re.findall(r"\d+", line)))
    if any(isSafe(levels[:i] + levels[i + 1:]) for i in range(len(levels))):
      safe += 1

  print(safe)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
