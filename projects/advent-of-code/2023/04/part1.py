from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  score = 0

  for line in lines:
    winningNumbers = [int(n) for n in re.findall(r":\s*(.*?)\s*\|", line)[0].split()]
    scratchNumbers = [int(n) for n in re.findall(r"\|\s*(.*?)\s*$", line)[0].split()]

    cardScore = 0
    for number in scratchNumbers:
      if number in winningNumbers:
        cardScore = 1 if cardScore == 0 else cardScore * 2

    score += cardScore

  print(score)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
