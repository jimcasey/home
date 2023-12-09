from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  directions = lines[0]

  nodes = {}
  for index in range(2, len(lines)):
    line = lines[index]
    match = re.match(r'(\w+)\s*=\s*\((.*?)\)', line)
    nodes[match.group(1)] = [node.strip() for node in match.group(2).split(',')]

  directionIndex = 0
  step = 0
  current = 'AAA'
  target = 'ZZZ'
  while current != target:
    step += 1
    current = nodes[current][0 if directions[directionIndex % len(directions)] == 'L' else 1]
    directionIndex += 1

  print(step)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
