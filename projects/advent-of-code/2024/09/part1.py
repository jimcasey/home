from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  disk = readInput()

  defragged = []
  for i in range(0, len(disk), 2):
    index = int(i / 2)
    file = int(disk[i])
    space = int(disk[i + 1]) if i + 1 < len(disk) else 0

    for j in range(file):
      defragged.append(str(index))

    for j in range(space):
      defragged.append('.')

  move = len(defragged) - 1
  for i in range(len(defragged)):
    block = defragged[i]
    if block == '.':
      while True:
        if defragged[move] != '.':
          break
        move -= 1

      if move <= i:
        break

      defragged[i] = defragged[move]
      defragged[move] = '.'
      move -= 1

  checksum = 0
  for i in range(len(defragged)):
    if defragged[i] == '.':
      break
    checksum += int(defragged[i]) * i

  print(checksum)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()[0]


main()
