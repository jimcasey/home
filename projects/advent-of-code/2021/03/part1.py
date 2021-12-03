import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  diagnostics = file.read().splitlines()

bitCounts = list()
for n in range(len(diagnostics[0])):
  bitCounts.append([0, 0])

for reading in diagnostics:
  for index, bit in enumerate(reading):
    bitCounts[index][int(bit)] += 1

def mapJoin(func, iterable):
  return ''.join(map(func, iterable))

def mostCommonBit(count):
  return str(0 if count[0] > count[1] else 1)

def inverseBit(bit):
  return str((int(bit) + 1) % 2)

gammaBin = mapJoin(mostCommonBit, bitCounts)
gammaRate = int(gammaBin, 2)

epsilonBin = mapJoin(inverseBit, gammaBin)
epsilonRate = int(epsilonBin, 2)

print('Gamma rate is ' + str(gammaRate) + ', epsilon rate ' + str(epsilonRate) +
      ' for a power consumption of ' + str(gammaRate * epsilonRate) + '.')
