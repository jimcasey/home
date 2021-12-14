import os
from functools import reduce

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  polymer, rules = file.read().split('\n\n')

  def parseRule(dict, line):
    pair, element = line.split(' -> ')
    dict[pair] = element
    return dict
  rules = reduce(parseRule, rules.splitlines(), {})

def step(current):
  next = current[0]
  for index in range(1, len(current)):
    pair = current[index - 1:index + 1]
    next += rules[pair] + current[index]
  return next

for _ in range(10):
  polymer = step(polymer)

elementCounts = {}
for element in polymer:
  if not element in elementCounts.keys():
    elementCounts[element] = 0
  elementCounts[element] += 1

minCount = min(elementCounts.values())
maxCount = max(elementCounts.values())

print(f'The answer is is {maxCount - minCount}.')
