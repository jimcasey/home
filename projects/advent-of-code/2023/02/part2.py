from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()

  sum = 0

  for line in lines:
    reveals = [{color: int(number)} for number, color in re.findall(r"(\d+) (\w+)", line)]

    minColors = {'red': 0, 'green': 0, 'blue': 0}
    for reveal in reveals:
      for color, number in reveal.items():
        minColors[color] = max(minColors[color], number)

    sum += minColors['red'] * minColors['green'] * minColors['blue']

  print(sum)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
