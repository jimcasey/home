from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  sum = 0
  for line in lines:
    matches = re.findall(r"\d", line)
    first_digit = matches[0]
    last_digit = matches[-1]

    sum += int(first_digit + last_digit)

  print(sum)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
