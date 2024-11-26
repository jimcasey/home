from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  time = int(''.join(re.findall(r'\d+', lines[0])))
  record = int(''.join(re.findall(r'\d+', lines[1])))

  beats = 0
  for speed in range(1, time + 1):
    distance = speed * (time - speed)
    if distance > record:
      beats += 1
  print(beats)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
