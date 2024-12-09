from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def getAntinodes(nodeA, nodeB):
  offset = (nodeA[0] - nodeB[0], nodeA[1] - nodeB[1])
  return [r for r in [
    (nodeA[0] + offset[0], nodeA[1] + offset[1]),
    (nodeA[0] - offset[0], nodeA[1] - offset[1]),
    (nodeB[0] + offset[0], nodeB[1] + offset[1]),
    (nodeB[0] - offset[0], nodeB[1] - offset[1]),
  ] if r != nodeA and r != nodeB]


def main():
  lines = readInput()

  antennas = {}

  max = (len(lines[0]) - 1, len(lines) - 1)

  for y in range(len(lines)):
    for x in range(len(lines[y])):
      char = lines[y][x]
      if char != '.':
        if antennas.get(char) is None:
          antennas[char] = []
        antennas[char].append((x, y))


  antinodes = []
  for antenna in antennas:
    for nodeA  in antennas[antenna]:
      for nodeB in antennas[antenna]:
        if (nodeA != nodeB):
          for antinode in getAntinodes(nodeA, nodeB):
            if (0 <= antinode[0] <= max[0] and 0 <= antinode[1] <= max[1]):
              antinodes.append(antinode)

  count = 0
  for y in range(len(lines)):
    for x in range(len(lines[y])):
      if (x, y) in antinodes:
        print('#', end='')
        count += 1
      else:
        print(lines[y][x], end='')
    print()

  print(count)

def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
