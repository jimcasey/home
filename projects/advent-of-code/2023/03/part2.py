from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def findNumbers(line, start, end):
  numbers = []
  for match in re.finditer(r'\d+', line):
    xStart = match.start()
    xEnd = match.end() - 1
    if (start <= xStart and xStart <= end) or (start <= xEnd and xEnd <= end):
      numbers.append(match.group())
  return numbers


def main():
  input = readInput()
  sum = 0

  for y, line in enumerate(input):
    for match in re.finditer(r'\*', line):
      x = match.start()

      numbers = \
          (findNumbers(input[y-1], x-1, x+1) if y > 0 else []) + \
          re.findall(r'\d+$', line[0:x]) + \
          re.findall(r'^\d+', line[x+1:]) + \
          (findNumbers(input[y+1], x-1, x+1) if y < len(input) - 1 else [])

      if len(numbers) == 2:
        numbers = [int(i) for i in numbers]
        sum += numbers[0] * numbers[1]

  print(sum)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
