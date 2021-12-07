import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  crabs = list(map(int, file.readline().replace('\n', '').split(',')))

maxCrabs = max(crabs)
triSequence = [int(n * (n + 1) / 2) for n in range(maxCrabs + 1)]
fuel = [0] * maxCrabs

for crab in crabs:
  for index, _ in enumerate(fuel):
    fuel[index] += triSequence[abs(crab - index)]

print('Minimum possible is {0} fuel.'.format(min(fuel)))
