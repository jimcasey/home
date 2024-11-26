from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()

  for y, line in enumerate(lines):
    x = line.find('S')
    if x != -1:
      startPos = (x, y)
      break

  def navigate(lastPos, currentPos):
    x0, y0 = lastPos
    x1, y1 = currentPos
    c = lines[y1][x1]

    if c == '.':
      return None
    elif c == '|':
      if y1 > y0:
        nextPos = (x1, y1 + 1)
      else:
        nextPos = (x1, y1 - 1)
    elif c == '-':
      if x1 > x0:
        nextPos = (x1 + 1, y1)
      else:
        nextPos = (x1 - 1, y1)
    elif c == 'L':
      if x1 < x0:
        nextPos = (x1, y1 - 1)
      else:
        nextPos = (x1 + 1, y1)
    elif c == 'J':
      if x1 > x0:
        nextPos = (x1, y1 - 1)
      else:
        nextPos = (x1 - 1, y1)
    elif c == '7':
      if x1 > x0:
        nextPos = (x1, y1 + 1)
      else:
        nextPos = (x1 - 1, y1)
    elif c == 'F':
      if x1 < x0:
        nextPos = (x1, y1 + 1)
      else:
        nextPos = (x1 + 1, y1)

    x, y = nextPos

    if y < 0 or y >= len(lines):
      return None

    if x < 0 or x >= len(lines[y]):
      return None

    if lines[y][x] == 'S':
      return 'S'

    return nextPos

  def findPath(lastPos, nextPos):
    count = 1
    while True:
      currentPos = nextPos
      nextPos = navigate(lastPos, currentPos)

      if nextPos == None:
        return None

      count += 1
      if nextPos == 'S':
        return count

      x, y = nextPos
      lastPos = currentPos

  x, y = startPos
  startRoutes = [
      (x - 1, y),
      (x + 1, y),
      (x, y - 1),
      (x, y + 1)
  ]
  for nextPos in startRoutes:
    count = findPath(startPos, nextPos)
    if count != None:
      print(int(count / 2))
      break


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
