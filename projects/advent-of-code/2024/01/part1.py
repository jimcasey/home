from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()

  left = []
  right = []

  for line in lines:
    matches = re.findall(r"\d+", line)
    left.append(int(matches[0]))
    right.append(int(matches[-1]))

  left.sort()
  right.sort()

  diff = 0
  for i in range(len(left)):
    diff += abs(left[i] - right[i])

  print(diff)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
