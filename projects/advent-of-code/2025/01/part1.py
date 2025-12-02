from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'


def main():
  lines = readInput()

  for line in lines:
    print(line)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
