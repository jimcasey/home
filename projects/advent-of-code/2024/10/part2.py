from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


offsets = [
    [0, -1],
    [1, 0],
    [0, 1],
    [-1, 0],
]


def main():
  input = readInput()

  min = (0, 0)
  max = (len(input[0]) - 1, len(input) - 1)

  score = 0
  for y in range(len(input)):
    for x in range(len(input[y])):
      if input[y][x] == '0':
        routes = [(x, y)]

        for i in range(1, 10):
          newRoutes = []
          for route in routes:
            for offset in offsets:
              search = (route[0] + offset[0], route[1] + offset[1])
              if search[0] < min[0] or max[0] < search[0] or search[1] < min[1] or max[1] < search[1]:
                continue

              if input[search[1]][search[0]] == str(i):
                newRoutes.append(search)
          routes = newRoutes

          if len(routes) == 0:
            break

        score += len(routes)

  print(score)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
