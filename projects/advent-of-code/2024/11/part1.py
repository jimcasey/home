from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def blink(stones):
  changed = []

  for stone in stones:
    if stone == 0:
      changed.append(1)
    elif len(str(stone)) % 2 == 0:
      stoneStr = str(stone)
      i = len(stoneStr) // 2
      changed.append(int(stoneStr[:i]))
      changed.append(int(stoneStr[i:]))
    else:
      changed.append(stone * 2024)

  return changed


def main():
  stones = [int(x) for x in readInput()[0].split(' ')]
  for i in range(25):
    stones = blink(stones)

  print(len(stones))


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
