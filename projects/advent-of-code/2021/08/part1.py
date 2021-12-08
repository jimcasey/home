import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def parseLine(line):
  splitLine = line.split(' | ')
  return {
      'input': splitLine[0].split(' '),
      'output': splitLine[1].split(' '),
  }

with open(inputPath) as file:
  readings = list(map(parseLine, file.read().splitlines()))

digits = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg'
]

uniqueDigits = [1, 4, 7, 8]

count = 0
for reading in readings:
  for value in reading['output']:
    for number in uniqueDigits:
      if len(value) == len(digits[number]):
        count += 1

print('Digits 1, 4, 7 and 8 appear {0} times.'.format(count))
