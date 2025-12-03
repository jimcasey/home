from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  index = 50
  zero_count = 0

  for line in lines:
    direction = line[0]
    value = int(line[1:])

    if direction == 'R':
      # Count how many times we pass through 0 when moving right
      # We pass 0 when crossing multiples of 100
      zero_count += (index + value) // 100 - index // 100
      index = (index + value) % 100
    elif direction == 'L':
      # Count how many times we pass through 0 when moving left
      # We pass 0 when crossing multiples of 100 going down
      zero_count += (index - 1) // 100 - (index - value - 1) // 100
      index = (index - value) % 100

  print(zero_count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
