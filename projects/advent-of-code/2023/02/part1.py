from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()

  targetBag = {'red': 12, 'green': 13, 'blue': 14}
  sum = 0

  for line in lines:
    game = int(re.search(r"Game (\d+):", line).group(1))
    reveals = [{color: int(count)} for count, color in re.findall(r"(\d+) (\w+)", line)]

    possible = True
    for reveal in reveals:
      for color, count in reveal.items():
        if count > targetBag.get(color, 0):
          possible = False
          break
      if not possible:
        break

    if possible:
      sum += game

  print(sum)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
