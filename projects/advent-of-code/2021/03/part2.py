import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def readingBin(reading):
  return list(map(int, reading))

with open(inputPath) as file:
  diagnostics = list(map(readingBin, file.read().splitlines()))

def getRating(type):
  readings = diagnostics.copy()

  for index in range(len(diagnostics[0])):
    bitCount = [0, 0]
    for reading in readings:
      bitCount[reading[index]] += 1

    testIndex = 1 if type == 'o2' else 0
    testBit = testIndex if bitCount[0] <= bitCount[1] else (testIndex + 1) % 2

    remove = []
    for reading in readings:
      if reading[index] != testBit:
        remove.append(reading)

    for reading in remove:
      readings.remove(reading)

    if len(readings) == 1:
      break

  return int(''.join(map(str, readings[0])), 2)

o2Generator = getRating('o2')
co2Scrubber = getRating('co2')
lifeSupport = o2Generator * co2Scrubber

print('With oxygen generator rating ' + str(o2Generator) +
      ' and CO2 scrubber rating ' + str(co2Scrubber) + ',' +
      ' the life support rating is ' + str(lifeSupport) + '.')
