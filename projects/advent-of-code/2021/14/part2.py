import os
from functools import reduce

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  template, rules = file.read().split('\n\n')

  def parseRule(dict, line):
    pair, element = line.split(' -> ')
    dict[pair] = element
    return dict
  rules = reduce(parseRule, rules.splitlines(), {})

class DefaultDict(dict):
  def __init__(self, default, *args, **kwargs):
    self.__default = default
    super(DefaultDict, self).__init__(*args, **kwargs)

  def __getitem__(self, key):
    return self.get(key, self.__default)

pairCounts = DefaultDict(0)
for index in range(1, len(template)):
  pair = template[index - 1:index + 1]
  pairCounts[pair] += 1

for _ in range(40):
  nextCounts = DefaultDict(0)
  for pair, count in pairCounts.items():
    element = rules[pair]
    nextCounts[pair[0] + element] += count
    nextCounts[element + pair[1]] += count
  pairCounts = nextCounts

elementCounts = DefaultDict(0)
elementCounts[template[-1]] += 1
for pair, count in pairCounts.items():
  elementCounts[pair[0]] += count

minCount = min(elementCounts.values())
maxCount = max(elementCounts.values())

print(f'The answer is is {maxCount - minCount}.')
