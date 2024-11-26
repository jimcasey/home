from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'


def main():
  lines = readInput()
  lineLength = len(lines[0])

  doubleY = []
  for y, line in enumerate(lines):
    if line.find('#') == -1:
      doubleY.append(y)

  blankLine = '.' * lineLength
  for y in reversed(doubleY):
    lines.insert(y, blankLine)

  doubleX = []
  for x in range(lineLength):
    append = True
    for line in lines:
      if line[x] == '#':
        append = False
        break
    if append:
      doubleX.append(x)

  for x in reversed(doubleX):
    for y, line in enumerate(lines):
      lines[y] = line[:x] + '.' + line[x:]

  galaxies = []
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      if char == '#':
        galaxies.append((x, y))

  for galaxy in galaxies:
    print(galaxy)

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
