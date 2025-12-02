from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def printDisk(disk):
  print(''.join([str(i[0]) * i[1] for i in disk]))


def main():
  input = readInput()

  if len(input) % 2 == 1:
    input += "0"

  disk = []
  for i in range(0, len(input), 2):
    index = int(i / 2)
    searchIndex = index
    file = int(input[i])
    free = int(input[i + 1])

    disk.append((index, file))
    if free > 0:
      disk.append(('.', free))

  while searchIndex >= 0:
    findIndex = next((i for i, item in enumerate(disk) if item[0] == searchIndex), -1)
    move = disk[findIndex]

    for i in range(len(disk)):
      if i == findIndex:
        break

      if disk[i][0] == '.' and disk[i][1] >= move[1]:
        disk = disk[:i] + [move, ('.', disk[i][1] - move[1])] + disk[i+1:]
        disk = disk[:findIndex+1] + [('.', move[1])] + disk[findIndex+2:]
        break

    searchIndex -= 1

  defragged = []
  for file in disk:
    for _ in range(file[1]):
      defragged.append(file[0])

  checksum = 0
  for i, index in enumerate(defragged):
    if index != '.':
      checksum += index * i

  print(checksum)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()[0]


main()
