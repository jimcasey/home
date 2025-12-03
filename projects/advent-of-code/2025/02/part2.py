from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  line = readInput()
  items = line.split(',')
  total = 0
  for item in items:
    start, end = item.split('-')
    for num in range(int(start), int(end) + 1):
      if is_mirrored(num):
        total += num
  print(total)


def is_mirrored(num):
  s = str(num)
  length = len(s)
  for pattern_len in range(1, length):
    if length % pattern_len == 0:
      pattern = s[:pattern_len]
      if pattern * (length // pattern_len) == s:
        return True
  return False


def readInput():
  with open(inputPath) as file:
    return file.read().strip()


main()
