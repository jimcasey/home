from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  lineLength = len(lines[0])

  doubleY = []
  for y, line in enumerate(lines):
    if line.find('#') == -1:
      doubleY.append(y)

  doubleX = []
  for x in range(lineLength):
    append = True
    for line in lines:
      if line[x] == '#':
        append = False
        break
    if append:
      doubleX.append(x)

  galaxies = []
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      if char == '#':
        galaxies.append((x, y))

  multiplier = 1000000

  xOffset = 0
  xOffsets = []
  for index in range(lineLength):
    if index in doubleX:
      xOffset += multiplier - 1
    xOffsets.append(index + xOffset)

  yOffset = 0
  yOffsets = []
  for index in range(len(lines)):
    if index in doubleY:
      yOffset += multiplier - 1
    yOffsets.append(index + yOffset)

  for index, galaxy in enumerate(galaxies):
    cx, cy = galaxy
    galaxies[index] = (xOffsets[cx], yOffsets[cy])

  sum = 0
  while len(galaxies) > 0:
    x, y = galaxies.pop(0)
    for galaxy in galaxies:
      cx, cy = galaxy
      dx = abs(x - cx)
      dy = abs(y - cy)
      sum += dx + dy

  print(sum)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
