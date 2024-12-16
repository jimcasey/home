from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def setStone(stones, stone, count):
  if stone in stones:
    stones[stone] += count
  else:
    stones[stone] = count


def blink(stones):
  changed = {}

  for stone in stones:
    if stone == 0:
      setStone(changed, 1, stones[stone])
    elif len(str(stone)) % 2 == 0:
      stoneStr = str(stone)
      i = len(stoneStr) // 2
      setStone(changed, int(stoneStr[:i]), stones[stone])
      setStone(changed, int(stoneStr[i:]), stones[stone])
    else:
      setStone(changed, stone * 2024, stones[stone])

  return changed


def main():
  input = [int(x) for x in readInput()[0].split(' ')]
  stones = {}
  for stone in input:
    stones[stone] = stones.get(stone, 0) + 1

  for i in range(75):
    stones = blink(stones)

  count = 0
  for stone in stones:
    count += stones[stone]

  print(count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
