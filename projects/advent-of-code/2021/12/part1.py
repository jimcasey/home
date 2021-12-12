import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

class CaveMap:
  def __init__(self, lines):
    self.caves = {}
    for line in lines:
      caveA, caveB = line.split('-')
      self.add(caveA, caveB)
      self.add(caveB, caveA)

  def add(self, cave, connection):
    if not cave in self.caves.keys():
      self.caves[cave] = {
          'connections': [],
          'large': cave[0].isupper()
      }
    if not connection in self.getConnections(cave):
      self.caves[cave]['connections'].append(connection)

  def getConnections(self, cave):
    return self.caves[cave]['connections']

  def isLarge(self, cave):
    return self.caves[cave]['large']

  def getPaths(self, path=['start']):
    paths = []
    *_, cave = path
    for connection in self.getConnections(cave):
      if connection in path and not self.isLarge(connection):
        continue
      newPath = path.copy()
      newPath.append(connection)
      if connection == 'end':
        paths.append(newPath)
      else:
        paths.extend(self.getPaths(newPath))
    return paths

with open(inputPath) as file:
  caveMap = CaveMap(file.read().splitlines())

paths = caveMap.getPaths()
print(f'There are {len(paths)} possible paths.')
