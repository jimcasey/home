import os
from functools import reduce

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  input = file.readline().replace('\n', '')

def decode(hexStr):
  parseHex = (lambda s, c: s + str.rjust(f'{int(c, 16):b}', 4, '0'))
  return reduce(parseHex, hexStr, '')

def read(message, pos, count):
  end = pos + count
  b = message[pos:end]
  return end, b

def readInt(message, pos, count):
  end, b = read(message, pos, count)
  return end, int(b, 2)

def parse(message, pos=0):
  pos, _ = readInt(message, pos, 3)
  pos, id = readInt(message, pos, 3)

  if id == 4:
    # literal value
    valueStr = ''
    while True:
      pos, groupID = readInt(message, pos, 1)
      pos, b = read(message, pos, 4)
      valueStr += b
      if groupID == 0:
        return pos, int(valueStr, 2)
  else:
    # operator
    pos, type = readInt(message, pos, 1)
    values = []
    if type == 0:
      # total length in bits
      pos, length = readInt(message, pos, 15)
      while length > 0:
        newPos, value = parse(message, pos)
        length -= newPos - pos
        pos = newPos
        values.append(value)
    else:
      # sub-packet count
      pos, count = readInt(message, pos, 11)
      for _ in range(count):
        pos, value = parse(message, pos)
        values.append(value)

    value = None
    if id == 0:
      # sum
      value = sum(values)
    elif id == 1:
      # product
      value = reduce((lambda a, b: a * b), values)
    elif id == 2:
      # minimum
      value = min(values)
    elif id == 3:
      # maximum
      value = max(values)
    elif id == 5:
      # greater than
      a, b = values
      value = 1 if a > b else 0
    elif id == 6:
      # less than
      a, b = values
      value = 1 if a < b else 0
    elif id == 7:
      # equal to
      a, b = values
      value = 1 if a == b else 0

    return pos, value

_, value = parse(decode(input))
print(f'Output of the transmission is {value}.')
