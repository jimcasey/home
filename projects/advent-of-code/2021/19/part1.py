from collections import defaultdict
from math import sqrt
import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  scanners = [
      [tuple(map(int, line.split(','))) for line in group.split('\n')[1:]]
      for group in file.read().strip().split('\n\n')
  ]

def distance(beaconA, beaconB):
  xA, yA, zA = beaconA
  xB, yB, zB = beaconB
  return sqrt(pow(xA - xB, 2) + pow(yA - yB, 2) + pow(zA - zB, 2) * 1.0)

unique = set()

for beacons in scanners:
  for beacon in beacons:
    neighbors = {}
    for peer in beacons:
      if peer != beacon:
        neighbors[distance(beacon, peer)] = peer
    distanceA, distanceB = sorted(neighbors)[0:2]
    neighborA = neighbors[distanceA]
    neighborB = neighbors[distanceB]
    key = (distanceA + distanceB) * distance(neighborA, neighborB)
    unique.add(key)

print(len(unique))

# credit where credit is due on this one:
# https://bit.ly/3yOF591
