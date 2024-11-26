from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def getChars(input, y, xStart, xEnd):
  return '' if y < 0 or y >= len(input) else input[y][max(0, xStart):min(len(input), xEnd)]


def findAdjacentChars(input, y, xStart, xEnd):
  return getChars(input, y-1, xStart-1, xEnd+1) + \
      getChars(input, y, xStart-1, xStart) + \
      getChars(input, y, xEnd, xEnd+1) + \
      getChars(input, y+1, xStart-1, xEnd+1)


def main():
  input = readInput()
  sum = 0

  for y, line in enumerate(input):
    for match in re.finditer(r'\d+', line):
      xStart = match.start()
      xEnd = match.end()
      number = int(match.group())

      adjacentChars = findAdjacentChars(input, y, xStart, xEnd)
      hasSymbol = bool(re.search(r'[^.]', adjacentChars))

      if hasSymbol:
        sum += number

  print(sum)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
