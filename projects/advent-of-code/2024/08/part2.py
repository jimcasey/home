from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


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
    for nodeA in antennas[antenna]:
      for nodeB in antennas[antenna]:
        if (nodeA != nodeB):
          offset = (nodeA[0] - nodeB[0], nodeA[1] - nodeB[1])

          antinode = nodeA
          while True:
            antinode = (antinode[0] + offset[0], antinode[1] + offset[1])
            if (antinode[0] < 0 or antinode[0] > max[0] or antinode[1] < 0 or antinode[1] > max[1]):
              break
            if antinode != nodeB:
              antinodes.append(antinode)

          antinode = nodeA
          while True:
            antinode = (antinode[0] - offset[0], antinode[1] - offset[1])
            if (antinode[0] < 0 or antinode[0] > max[0] or antinode[1] < 0 or antinode[1] > max[1]):
              break
            if antinode != nodeB:
              antinodes.append(antinode)

  count = 0
  for y in range(len(lines)):
    for x in range(len(lines[y])):
      if (x, y) in antinodes or lines[y][x] != '.':
        count += 1

  print(count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
