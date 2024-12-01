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

  score = 0
  for i in range(len(left)):
    score += left[i] * right.count(left[i])

  print(score)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
