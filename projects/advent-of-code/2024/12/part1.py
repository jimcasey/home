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
  garden = readInput()

  min = (0, 0)
  max = (len(garden[0]) - 1, len(garden) - 1)

  count = 0
  counted = set()
  for y, row in enumerate(garden):
    for x, plant in enumerate(row):
      if (x, y) in counted:
        continue

      search = [(x, y)]
      area = 0
      fence = 0
      while len(search) > 0:
        nextSearch = []
        for item in search:
          if item in counted:
            continue

          area += 1
          counted.add(item)

          for offset in offsets:
            neighbor = (item[0] + offset[0], item[1] + offset[1])
            if neighbor[0] < min[0] or max[0] < neighbor[0] or neighbor[1] < min[1] or max[1] < neighbor[1] or garden[neighbor[1]][neighbor[0]] != plant:
              fence += 1
            elif neighbor not in counted:
              nextSearch.append(neighbor)
        search = nextSearch

      count += area * fence

  print(count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
