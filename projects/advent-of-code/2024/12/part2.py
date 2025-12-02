from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

offsets = {
    'N': [0, -1],
    'E': [1, 0],
    'S': [0, 1],
    'W': [-1, 0],
}


def main():
  garden = readInput()

  mx = len(garden[0]) - 1
  my = len(garden) - 1

  plots = []
  counted = set()
  for y, row in enumerate(garden):
    for x, plant in enumerate(row):
      if (x, y) in counted:
        continue

      plot = []
      fence = set()
      search = [(x, y)]
      while len(search) > 0:
        nextSearch = []
        for [sx, sy] in search:
          if (sx, sy) in counted:
            continue

          counted.add((sx, sy))
          plot.append((sx, sy))

          for d in offsets:
            [dx, dy] = offsets[d]
            nx = sx + dx
            ny = sy + dy

            if nx < 0 or mx < nx or ny < 0 or my < ny or garden[ny][nx] != plant:
              fence.add((d, nx, ny))
            elif (nx, ny) not in counted:
              nextSearch.append((nx, ny))
        search = nextSearch

      sides = 0
      while len(fence) > 0:
        search = [fence.pop()]
        sides += 1

        while len(search) > 0:
          [d, fx, fy] = search.pop()

          if d == 'N' or d == 'S':
            p = ['E', 'W']
          else:
            p = ['N', 'S']

          for pd in p:
            [dx, dy] = offsets[pd]
            nx = fx + dx
            ny = fy + dy
            if (d, nx, ny) in fence:
              search.append((d, nx, ny))
              fence.remove((d, nx, ny))

      plots.append((len(plot), sides))

  price = 0
  for [area, sides] in plots:
    price += area * sides

  print(price)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
