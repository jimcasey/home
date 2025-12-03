from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'


def main():
  line = readInput()
  items = line.split(',')
  for item in items:
    print(item)


def readInput():
  with open(inputPath) as file:
    return file.read().strip()


main()
