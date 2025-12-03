from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'


def main():
  lines = readInput()
  index = 0
  zero_count = 0

  for line in lines:
    direction = line[0]
    value = int(line[1:])

    if direction == 'R':
      index = (index + value) % 101
    elif direction == 'L':
      index = (index - value) % 101

    if index == 0:
      zero_count += 1

  print(zero_count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
