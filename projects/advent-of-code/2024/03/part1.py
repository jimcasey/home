from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  input = readInput()
  matches = re.findall(r"mul\(\d+,\d+\)", input)

  sum = 0
  for match in matches:
    nums = list(map(int, re.findall(r"\d+", match)))
    sum += nums[0] * nums[1]

  print(sum)


def readInput():
  with open(inputPath) as file:
    return file.read()


main()
