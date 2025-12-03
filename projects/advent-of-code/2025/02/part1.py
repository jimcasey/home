from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'


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
  if length % 2 != 0:
    return False
  mid = length // 2
  return s[:mid] == s[mid:]


def readInput():
  with open(inputPath) as file:
    return file.read().strip()


main()
