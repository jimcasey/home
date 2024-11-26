from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def applySeedMap(seedRange, seedMap):
  mappedRanges = []

  start = seedRange[0]
  end = seedRange[1]

  if start > seedMap[-1][1]:
    mappedRanges.append([start, end])
    return mappedRanges

  for item in seedMap:
    offset = item[2]
    if start < item[0]:
      if end < item[0]:
        mappedRanges.append([start + offset, end + offset])
        return mappedRanges
      else:
        mappedRanges.append([start + offset, item[0] - 1 + offset])
        start = item[0]
    elif start <= item[1]:
      if end <= item[1]:
        mappedRanges.append([start + offset, end + offset])
        return mappedRanges
      else:
        mappedRanges.append([start + offset, item[1] + offset])
        start = item[1] + 1

  if (start <= end):
    mappedRanges.append([start, end])

  return mappedRanges


def main():
  lines = readInput()
  seeds = re.findall(r'\d+', lines[0])
  seeds = [int(seed) for seed in seeds]
  seedRanges = [[seeds[i], seeds[i] + seeds[i+1] - 1] for i in range(0, len(seeds), 2)]

  seedMaps = []
  currentSeedMap = None

  for index, line in enumerate(lines):
    if index == 0:
      continue

    if line == '':
      currentSeedMap = None
      continue

    numbers = [int(number) for number in re.findall(r'\d+', line)]
    if len(numbers) == 0:
      continue

    if currentSeedMap == None:
      currentSeedMap = []
      seedMaps.append(currentSeedMap)

    start = numbers[1]
    end = start + numbers[2] - 1
    offset = numbers[0] - numbers[1]
    currentSeedMap.append([start, end, offset])

  for seedMap in seedMaps:
    seedMap.sort(key=lambda x: x[0])

  transformMaps = []
  for seedMap in seedMaps:
    transformMap = []
    if seedMap[0][0] > 0:
      transformMap.append([0, seedMap[0][0] - 1, 0])
    for index, item in enumerate(seedMap):
      transformMap.append(item)
      if index < len(seedMap) - 1:
        transformMap.append([item[1] + 1, seedMap[index + 1][0] - 1, 0])
    if seedMap[-1][1] < end:
      transformMap.append([seedMap[-1][1] + 1, end, 0])
    transformMaps.append(transformMap)
  seedMaps = transformMaps

  for seedMap in seedMaps:
    newSeedRanges = []
    for seedRange in seedRanges:
      newSeedRanges += applySeedMap(seedRange, seedMap)
    seedRanges = newSeedRanges

  minLocation = float('inf')
  for seedRange in seedRanges:
    minLocation = min(minLocation, seedRange[0])
  print(minLocation)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
