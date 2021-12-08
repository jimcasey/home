import os

# parses an input line
def parseLine(line):
  sets = line.split(' | ')
  return {
      'input': parseDigits(sets[0]),
      'output': parseDigits(sets[1]),
  }

# parses a string of digits
def parseDigits(digits):
  return list(map(orderString, digits.split(' ')))

# puts a string in alphabetical order
def orderString(digit):
  return ''.join(sorted(list(digit)))

# read input
scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'
with open(inputPath) as file:
  readings = list(map(parseLine, file.read().splitlines()))

class DigitMap:
  def __init__(self, input):
    self.numbers = {}
    self.digits = {}

    fives = []
    sixes = []

    for digit in input:
      length = len(digit)

      if length == 5:
        # includes 2, 3, 5
        fives.append(digit)
      elif length == 6:
        # includes 0, 6, 9
        sixes.append(digit)
      else:
        # includes 1, 4, 3, 8
        self.add({2: 1, 4: 4, 3: 7, 7: 8}[length], digit)

    for digit in fives:
      if self.contains(self.digit(1), digit):
        # 3 must contain 1
        self.add(3, digit)
      elif self.contains(self.inverse(self.digit(4)), digit):
        # 2 must contain the inverse of 4
        self.add(2, digit)
      else:
        # must be 5
        self.add(5, digit)

    for digit in sixes:
      if self.contains(self.digit(3), digit):
        # 9 must contain 3
        self.add(9, digit)
      elif not self.contains(self.digit(7), digit):
        # 6 must not contain 7
        self.add(6, digit)
      else:
        # must be 0
        self.add(0, digit)

  # adds to number and digit maps
  def add(self, number, digit):
    self.numbers[digit] = number
    self.digits[number] = digit

  # gets digit matching the number
  def digit(self, number):
    return self.digits[number]

  # gets number matching the digit
  def number(self, digit):
    return self.numbers[digit]

  # whether a digit contains all the letters in the search string
  def contains(self, search, digit):
    count = 0
    for c in search:
      if c in digit:
        count += 1
    return count == len(search)

  # inverses a digit string
  def inverse(self, digit):
    inverseDigit = ''
    for c in 'abcdefg':
      if not c in digit:
        inverseDigit += c
    return inverseDigit

outputSum = 0
for reading in readings:
  input = reading['input']
  output = reading['output']

  digitMap = DigitMap(input)

  outputStr = ''
  for digit in output:
    outputStr += str(digitMap.number(digit))

  outputSum += int(outputStr)

print('Sum of all outputs in {0}.'.format(outputSum))
