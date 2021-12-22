import os

def main():
  # get all scanners, which is a set of coordinates
  scanners = readInput()

  # define the field as the first scanner,
  # this is what we'll reorent all other scanners to
  field = set(scanners.pop(0))

  # a collection of scanner locations
  scannerCoords = []

  # calculate a set of scanner neighbor maps;
  # this is so we don't have to recalculate this every time
  # we try to find matching neighbors
  scannerMaps = [
      (scanner, createNeighborMap(scanner))
      for scanner in scanners
  ]

  # iterate through scanners until none are left
  while len(scannerMaps) > 0:
    # get the first scanner that shares at least three beacons with the field
    fieldMap = createNeighborMap(field)
    neighbors = findMatchingNeighbors(fieldMap, scannerMaps)
    scanner, fieldNeighbors, scannerNeighbors = neighbors

    # we've found a match, remove the scanner
    for index in range(len(scannerMaps)):
      if scannerMaps[index][0] == scanner:
        scannerMaps.pop(index)
        break

    # calculate the orientation of a scanner
    # through matching sets of neighbor coordinates
    orientation = calculateOrientation(fieldNeighbors, scannerNeighbors)

    # save the location of the scanner
    scannerCoord, _, _ = orientation
    scannerCoords.append(scannerCoord)

    # update the field with the reoriented scanner beacons
    field.update(reorientCoords(orientation, scanner))

  # count of unique beacons (part 1)
  beaconCount = len(field)

  # find the maximum distance between two scanner locations (part 2)
  maxDistance = findMaxDistance(scannerCoords)

  print(
      f'For {beaconCount} beacons, the maximum ' +
      f'distance between two scanners is {maxDistance}.'
  )

# reads the puzzle input
def readInput():
  scriptPath = os.path.dirname(os.path.abspath(__file__))
  inputPath = scriptPath + '/input.txt'

  with open(inputPath) as file:
    # return an array of coordinate tuples for each scanner group
    return [
        [tuple(map(int, line.split(','))) for line in group.split('\n')[1:]]
        for group in file.read().strip().split('\n\n')
    ]

# calculate the manhattan distance between two coordinates
def distance(coordA, coordB):
  return sum([abs(coordA[pos] - coordB[pos]) for pos in range(3)])

# finds the maximum manhattan distance between a set of coordinates
def findMaxDistance(coords):
  maxDistance = 0
  for indexA in range(len(coords)):
    for indexB in range(indexA + 1, len(coords)):
      coordA = coords[indexA]
      coordB = coords[indexB]
      maxDistance = max(maxDistance, distance(coordA, coordB))
  return maxDistance

# creates a map of each coordinate with its three nearest neigbhors,
# which is keyed off of the distance between all three
def createNeighborMap(coords):
  neighborMap = {}
  for coord in coords:
    # map distance to this coordinate with all its peers
    peerDistances = {}
    for peer in coords:
      if peer != coord:
        peerDistances[distance(coord, peer)] = peer

    # get the two shortest distances and find the nearest neighbors
    distanceA, distanceB = sorted(peerDistances)[0:2]
    neighborA = peerDistances[distanceA]
    neighborB = peerDistances[distanceB]

    # create a hash of the distance between all three neighbors;
    # this will be unique to any three beacons regardless of scanner orientation
    hash = (distanceA + distanceB) * distance(neighborA, neighborB)
    neighborMap[hash] = (coord, neighborA, neighborB)

  return neighborMap

# finds the first scanner that has a matching set of neighbors in the field
def findMatchingNeighbors(fieldMap, scannerMaps):
  for fieldHash in fieldMap.keys():
    for scanner, scannerMap in scannerMaps:
      for scannerHash in scannerMap.keys():
        if scannerHash == fieldHash:
          fieldNeighbors = fieldMap[scannerHash]
          scannerNeighbors = scannerMap[scannerHash]
          return (scanner, fieldNeighbors, scannerNeighbors)

# calculates the orientation of a scanner to the field,
# using sets of three matching beacon neighbors
def calculateOrientation(fieldNeighbors, scannerNeighbors):
  # offset of the scanner from the origin;
  # this is also scanner location coordinates relative to the field
  offset = [None] * 3

  # direction the scanner is facing
  direction = [None] * 3

  # rotation of the scanner
  rotation = [None] * 3

  # iterate all three coordinate positions (x, y, z)
  for pos in range(3):
    if offset[pos] != None:
      # we've already found an orientation for this position
      continue

    # iterate all rotation possibilities,
    # which essentially skews x, y, and z between the scanner and the field
    for rotationPos in range(3):
      # iterate direction flips
      for directionFlip in [-1, 1]:
        # build a set of offsets,
        # which is the difference between the field coordinate
        # and the potential scanner coordinate
        offsets = set()
        for index in range(3):
          offsets.add(
              fieldNeighbors[index][pos] -
              scannerNeighbors[index][rotationPos] * directionFlip
          )

        if len(offsets) == 1:
          # all three coordinates have the same offset,
          # which means we found our orientation
          offset[pos] = offsets.pop()
          direction[pos] = directionFlip
          rotation[pos] = rotationPos

  return (offset, direction, rotation)

# reorients a set of coordinates from the given offset, direction and rotation
def reorientCoords(orientation, coords):
  offset, direction, rotation = orientation
  return [
      tuple([
          # rotation moves directions (x, y, z) relative to the field,
          # direction flips it positive or negative (by multiplying by 1 or -1)
          # and the offset moves the coordinate relative to the field origin
          coord[rotation[index]] * direction[index] + offset[index]
          for index in range(3)
      ])
      for coord in coords
  ]

main()
