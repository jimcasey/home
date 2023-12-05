from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  seeds = [int(seed) for seed in re.findall(r'\d+', lines[0])]

  maps = []
  currentMap = None

  for index, line in enumerate(lines):
    if index == 0:
      continue

    if line == '':
      currentMap = None
      continue

    numbers = [int(number) for number in re.findall(r'\d+', line)]
    if len(numbers) == 0:
      continue

    if currentMap == None:
      currentMap = []
      maps.append(currentMap)

    currentMap.append(numbers)

  minLocation = float('inf')

  for seed in seeds:
    pip = seed
    for map in maps:
      nextPip = None
      for item in map:
        source = item[1]
        destination = item[0]
        range = item[2]
        if source <= pip <= source + range:
          nextPip = destination + (pip - source)
          break
      pip = nextPip if nextPip != None else pip
    minLocation = min(minLocation, pip)

  print(minLocation)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
