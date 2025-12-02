from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'


def main():
  lines = readInput()
  index = 0

  for line in lines:
    direction = line[0]
    value = int(line[1:])

    if direction == 'R':
      index += value
      if index > 99:
        index = 0
    elif direction == 'L':
      index -= value
      if index < 0:
        index = 99

    print(f"{index} {line}")


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
