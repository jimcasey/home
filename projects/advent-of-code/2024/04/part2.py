from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  count = 0

  for y in range(1, len(lines)-1):
    line = lines[y]
    for x in range(1, len(line)-1):
      if lines[y][x] != 'A':
        continue

      offsets = lines[y-1][x-1] + lines[y+1][x+1] + lines[y-1][x+1] + lines[y+1][x-1]

      if re.match(r"(MS|SM)(MS|SM)", offsets):
        count += 1

  print(count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
