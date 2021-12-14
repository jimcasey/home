import os
import re
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

counts = None
for element in rules.values():
  count = polymer.count(element)
  if counts == None:
    counts = [count, count]
  else:
    counts[0] = min(counts[0], count)
    counts[1] = max(counts[1], count)

minCount, maxCount = counts

print(f'Maximum less minimum frequency of letters is {maxCount - minCount}.')
