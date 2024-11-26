from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def findCombinations(arrayLength, value):
  if arrayLength == 0:
    return [[]]
  if value == 0:
    return [[0] * arrayLength]

  combinations = []
  for i in range(value + 1):
    subcombinations = findCombinations(arrayLength - 1, value - i)
    for subcombination in subcombinations:
      combinations.append([i] + subcombination)

  return filter(lambda combination: sum(combination) == value, combinations)


def main():
  lines = readInput()

  springs = []
  groups = []
  for line in lines:
    split = line.split(' ')
    springs.append(split[0])
    groups.append([int(n) for n in split[1].split(',')])

  total = 0
  for index, group in enumerate(groups):
    pattern = springs[index]
    length = len(pattern)
    gap = length - sum(group)

    possible = 0
    combinations = findCombinations(len(group) + 1, gap)

    for combination in combinations:
      if not all(combination[1:-1]):
        continue

      option = ''
      for index, n in enumerate(combination):
        option += '.' * n
        if index < len(group):
          option += '#' * group[index]

      isPossible = True
      for index, c in enumerate(option):
        if pattern[index] == '?':
          continue
        if pattern[index] != c:
          isPossible = False
          break

      if isPossible:
        possible += 1

    total += possible

  print(total)

def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
