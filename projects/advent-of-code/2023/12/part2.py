from os import path
from functools import cache

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

# credit:
# https://github.com/Domyy95/Challenges/blob/master/2023-12-Advent-of-code/12.py

@cache
def countCombinations(springs, groups):
  if not groups:
    return 0 if "#" in springs else 1
  if not springs:
    return 1 if not groups else 0

  result = 0

  if springs[0] in ".?":
    result += countCombinations(springs[1:], groups)
  if springs[0] in "#?":
    if (
        groups[0] <= len(springs)
        and "." not in springs[: groups[0]]
        and (groups[0] == len(springs) or springs[groups[0]] != "#")
    ):
      result += countCombinations(springs[groups[0] + 1:], groups[1:])

  return result


def main():
  lines = readInput()

  solution = 0
  for line in lines:
    springs, groups = line.split()
    groups = eval(groups)

    springs = "?".join([springs] * 5)
    groups = groups * 5
    solution += countCombinations(springs, groups)

  print(solution)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
