from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  input = readInput()
  matches = re.findall(r"do\(\)|mul\(\d+,\d+\)|don't\(\)", input)

  sum = 0
  enabled = True
  for match in matches:
    if match == "do()":
      enabled = True
    elif match == "don't()":
      enabled = False
    elif enabled:
      nums = list(map(int, re.findall(r"\d+", match)))
      sum += nums[0] * nums[1]

  print(sum)


def readInput():
  with open(inputPath) as file:
    return file.read()


main()
