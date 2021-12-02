import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  commands = file.read().splitlines()

horizontal = 0
depth = 0

for command in commands:
  direction, distance = command.split()
  distance = int(distance)
  if direction == 'forward':
    horizontal += distance
  else:
    depth += distance if direction == 'down' else 0 - distance

print('Horizontal is ' + str(horizontal) + ' and depth ' +
      str(depth) + ' for a multiple of ' + str(depth * horizontal) + '.')
