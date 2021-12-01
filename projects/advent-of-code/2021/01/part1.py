import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  soundings = map(int, file.read().splitlines())

increaseCount = 0
lastDepth = None
for depth in soundings:
  if lastDepth != None and depth > lastDepth:
    increaseCount += 1
  lastDepth = depth

print('Depth soundings have increased ' + str(increaseCount) + ' times.')
