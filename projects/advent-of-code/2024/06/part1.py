from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

offsets = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}


def main():
  lines = readInput()
  dirIndex = 0
  dirKeys = list(offsets.keys())
  dir = dirKeys[dirIndex]

  for y in range(len(lines)):
    for x in range(len(lines[y])):
      if lines[y][x] == dir:
        pos = (x, y)
        break

  min = (0, 0)
  max = (len(lines) - 1, len(lines[0]) - 1)

  while True:
    offset = offsets[dir]
    nextPos = (pos[0] + offset[0], pos[1] + offset[1])

    if nextPos[0] > max[0] or nextPos[1] > max[1] or nextPos[0] < min[0] or nextPos[1] < min[1]:
      break

    if lines[nextPos[1]][nextPos[0]] == '#':
      dirIndex = (dirIndex + 1) % len(dirKeys)
      dir = dirKeys[dirIndex]
      continue

    pos = nextPos
    line = lines[pos[1]]
    lines[pos[1]] = line[:pos[0]] + 'X' + line[pos[0] + 1:]

  count = 0
  for line in lines:
    count += line.count('X')

  print(count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
