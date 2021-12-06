import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  fish = list(map(int, file.read().splitlines()[0].split(',')))

for _ in range(80):
  newFish = 0
  for index, f in enumerate(fish):
    fish[index] -= 1
    if fish[index] < 0:
      fish[index] = 6
      newFish += 1
  fish.extend([8] * newFish)

print('There are {0} fish.'.format(len(fish)))
