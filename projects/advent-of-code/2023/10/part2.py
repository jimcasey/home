from os import path
import re

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

  x, y = startPos
  startRoutes = [
      (x - 1, y),
      (x + 1, y),
      (x, y - 1),
      (x, y + 1)
  ]

  blankPath = [['.' for x in range(len(lines[0]))] for y in range(len(lines))]

  for firstPos in startRoutes:
    lastPos = startPos
    nextPos = firstPos

    path = blankPath

    x, y = startPos
    path[y][x] = lines[y][x]

    deadEnd = False
    while True:
      x, y = nextPos
      path[y][x] = lines[y][x]
      currentPos = nextPos
      nextPos = navigate(lastPos, currentPos)
      lastPos = currentPos

      if nextPos == None:
        deadEnd = True
        break

      if nextPos == 'S':
        break

    if not deadEnd:
      break

  def getDirection(pos0, pos1):
    x0, y0 = pos0
    x1, y1 = pos1

    if x1 < x0:
      return 'L'
    elif x1 > x0:
      return 'R'
    elif y1 < y0:
      return 'T'
    elif y1 > y0:
      return 'B'

  dirs = ''.join(sorted([getDirection(startPos, firstPos), getDirection(startPos, lastPos)]))

  if dirs == 'LT':
    c = 'J'
  elif dirs == 'BL':
    c = '7'
  elif dirs == 'RT':
    c = 'L'
  elif dirs == 'BR':
    c = 'F'
  elif dirs == 'BT':
    c = '|'
  elif dirs == 'LR':
    c = '-'

  path[startPos[1]][startPos[0]] = c

  count = 0
  for y, line in enumerate(path):
    inside = False
    bend = None
    for x, c in enumerate(line):
      if c == '.':
        if inside:
          count += 1
          path[y][x] = '+'
      elif c == '|':
        inside = not inside
      elif c in 'LJ7F':
        if bend == None:
          bend = c
        else:
          if (bend == 'L' and c == '7') or (bend == 'F' and c == 'J'):
            inside = not inside
          bend = None
      print(path[y][x], end='')
    print()
  print(count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
