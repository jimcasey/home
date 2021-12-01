import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  soundings = list(map(int, file.read().splitlines()))

sums = list()
for index, _ in enumerate(soundings):
  if index >= 2:
    sums.append(sum(soundings[index-2:index+1]))

increaseCount = 0
lastSum = None
for sum in sums:
  if lastSum != None and sum > lastSum:
    increaseCount += 1
  lastSum = sum

print('Sliding window depth soundings have increased ' +
      str(increaseCount) + ' times.')
