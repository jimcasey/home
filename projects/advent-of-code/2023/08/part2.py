from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def lowestCommonDenominator(numbers):
  def gcd(a, b):
    while b:
      a, b = b, a % b
    return a

  def lcm(a, b):
    return a * b // gcd(a, b)

  lcd = numbers[0]
  for number in numbers[1:]:
    lcd = lcm(lcd, number)
  return lcd


def main():
  lines = readInput()
  directions = lines[0]

  nodes = {}
  positions = []
  for index in range(2, len(lines)):
    line = lines[index]
    match = re.match(r'(\w+)\s*=\s*\((.*?)\)', line)
    node = match.group(1)
    if node[2] == 'A':
      positions.append(node)
    nodes[node] = [node.strip() for node in match.group(2).split(',')]

  periods = []

  for position in positions:
    step = 0
    node = position
    while True:
      direction = directions[step % len(directions)]
      node = nodes[node][0 if direction == 'L' else 1]
      step += 1

      if node[2] == 'Z':
        break

    periods.append(step)

  print(lowestCommonDenominator(periods))


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
