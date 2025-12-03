from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'


def main():
  line = readInput()
  items = line.split(',')
  for item in items:
    start, end = item.split('-')
    for num in range(int(start), int(end) + 1):
      print(num)


def readInput():
  with open(inputPath) as file:
    return file.read().strip()


main()
