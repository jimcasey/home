from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  scratchers = [1] * len(lines)

  for index, line in enumerate(lines):
    winningNumbers = [int(n) for n in re.findall(r":\s*(.*?)\s*\|", line)[0].split()]
    scratchNumbers = [int(n) for n in re.findall(r"\|\s*(.*?)\s*$", line)[0].split()]

    matchCount = 0
    for number in scratchNumbers:
      if number in winningNumbers:
        matchCount += 1

    if matchCount > 0:
      for copyIndex in range(index + 1, index + 1 + matchCount):
        scratchers[copyIndex] += scratchers[index]

  score = 0
  for scratcherCount in scratchers:
    score += scratcherCount

  print(score)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
