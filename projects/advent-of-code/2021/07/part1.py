import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  crabs = list(map(int, file.readline().replace('\n', '').split(',')))

fuel = [0] * max(crabs)

for crab in crabs:
  for index, _ in enumerate(fuel):
    fuel[index] += abs(crab - index)

print('Minimum possible is {0} fuel.'.format(min(fuel)))
