from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

directions = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]


def countXmases(lines, y, x):
  count = 0
  min = (0, 0)
  max = (len(lines) - 1, len(lines[0]) - 1)

  for direction in directions:
    found = True
    for i in range(1, 4):
      pos = (y + direction[0] * i, x + direction[1] * i)
      if min[1] > pos[1] or pos[1] > max[1] or min[0] > pos[0] or pos[0] > max[0]:
        found = False
        break

      char = lines[pos[0]][pos[1]]

      if char != 'MAS'[i - 1]:
        found = False
        break

    if found:
      count += 1

  return count


def main():
  lines = readInput()
  count = 0
  for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
      char = line[x]
      if char == 'X':
        count += countXmases(lines, y, x)

  print(count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
