import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

class OctoMap:
  def __init__(self, lines):
    self.octopi = {}
    offsets = [
        [0, -1],
        [1, -1],
        [1, 0],
        [1, 1],
        [0, 1],
        [-1, 1],
        [-1, 0],
        [-1, -1]
    ]

    self.width = len(lines[0])
    self.height = len(lines)
    self.count = self.width * self.height

    for y in range(self.height):
      for x in range(self.width):
        adjacent = []
        for offset in offsets:
          offsetX, offsetY = offset
          adjacentX = x + offsetX
          if adjacentX < 0 or self.width <= adjacentX:
            continue

          adjacentY = y + offsetY
          if adjacentY < 0 or self.height <= adjacentY:
            continue

          adjacent.append(f'{adjacentX},{adjacentY}')

        self.octopi[f'{x},{y}'] = {
            'power': int(lines[y][x]),
            'adjacent': adjacent
        }

  def step(self):
    nines = []
    for octopus in self.octopi.values():
      octopus['power'] += 1
    self.flash()

    flashes = 0
    for octopus in self.octopi.values():
      if octopus['power'] == 0:
        flashes += 1
    return flashes

  def flash(self):
    flashes = 0
    for octopus in self.octopi.values():
      if octopus['power'] > 9:
        flashes += 1
        octopus['power'] = 0

        for adjacentCoord in octopus['adjacent']:
          if self.octopi[adjacentCoord]['power'] != 0:
            self.octopi[adjacentCoord]['power'] += 1

    if flashes > 0:
      self.flash()

  def print(self):
    for y in range(self.height):
      for x in range(self.width):
        power = self.octopi[f'{x},{y}']['power']
        output = f'\033[1;36m{power}\033[0m' if power == 0 else power
        print(output, end='')
      print('')
    print('-' * self.width)

with open(inputPath) as file:
  octoMap = OctoMap(file.read().splitlines())

index = 0
flashes = 0
while flashes != octoMap.count:
  index += 1
  flashes = octoMap.step()

print(f'First synchronized step was {index}.')
