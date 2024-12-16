from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'


neighbors = {
    (0, -1): 'T',
    (1, 0): 'R',
    (0, 1): 'B',
    (-1, 0): 'L',
}

corners = [
    (0, 0),
    (1, -1),
    (1, 1),
    (-1, 1),
    (-1, -1),
]

options = {
    'T': ['R', 'L'],
    'R': ['T', 'B'],
    'B': ['R', 'L'],
    'L': ['T', 'B'],
}


def popNext(fence, item):
  for n in neighbors:
    find = (item[0], item[1] + n[0], item[2] + n[1])
    if find in fence:
      fence.remove(find)
      return find

  for corner in corners:
    for dir in options[item[0]]:
      find = (dir, item[1] + corner[0], item[2] + corner[1])
      if find in fence:
        fence.remove(find)
        return find

  return None


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
      fence = set()
      while len(search) > 0:
        nextSearch = []
        for currentItem in search:
          if currentItem in counted:
            continue

          area += 1
          counted.add(currentItem)

          for n in neighbors:
            dir = neighbors[n]
            neighbor = (currentItem[0] + n[0], currentItem[1] + n[1])
            if neighbor[0] < min[0] or max[0] < neighbor[0] or neighbor[1] < min[1] or max[1] < neighbor[1] or garden[neighbor[1]][neighbor[0]] != plant:
              fence.add((dir, *neighbor))
            elif neighbor not in counted:
              nextSearch.append(neighbor)
        search = nextSearch

      sides = 0
      currentItem = firstItem = fence.pop()
      while True:
        nextItem = popNext(fence, currentItem)
        if not nextItem:
          if currentItem[0] != firstItem[0]:
            sides += 1
          break

        if currentItem[0] != nextItem[0]:
          sides += 1

        currentItem = nextItem

      print(f'{plant}: {area} {sides}')
      count += area * sides

  print(count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
