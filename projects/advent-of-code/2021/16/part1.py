import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  input = file.readline().replace('\n', '')

cypher = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def decode(hexStr):
  return ''.join([cypher[c] for c in hexStr])

def read(message, pos, count):
  end = pos + count
  b = message[pos:end]
  return end, b

def readInt(message, pos, count):
  end, b = read(message, pos, count)
  return end, int(b, 2)

def parse(message, pos=0, versionSum=0):
  pos, version = readInt(message, pos, 3)
  versionSum += version
  pos, id = readInt(message, pos, 3)

  if id == 4:
    # literal value
    value = ''
    while True:
      pos, groupID = readInt(message, pos, 1)
      pos, b = read(message, pos, 4)
      value += b
      if groupID == 0:
        break
  else:
    # operator
    pos, type = readInt(message, pos, 1)
    if type == 0:
      # total length in bits
      pos, length = readInt(message, pos, 15)
      while length > 0:
        newPos, versionSum = parse(message, pos, versionSum)
        length -= newPos - pos
        pos = newPos
    else:
      # sub-packet count
      pos, count = readInt(message, pos, 11)
      for _ in range(count):
        pos, versionSum = parse(message, pos, versionSum)

  return pos, versionSum

message = decode(input)

_, versionSum = parse(message)

print(f'Sum of all versions is {versionSum}.')
