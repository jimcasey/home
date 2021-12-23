import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def main():
  algorithm, image = readInput()
  for index in range(50):
    fill = '.' if algorithm[0] == '.' else '#' if index % 2 == 1 else '.'
    image = padImage(image, fill)
    image = enhanceImage(image, algorithm, fill)

  countLit = 0
  for row in image:
    countLit += row.count('#')

  print(f'There are {countLit} lit pixels')

def readInput():
  with open(inputPath) as file:
    algorithm, image = file.read().strip().split('\n\n')
    algorithm = algorithm
    image = image.split('\n')
    return algorithm, image

def padImage(image, fill):
  minX = len(image[0])
  maxX = 0
  minY = len(image)
  maxY = 0

  for y in range(len(image)):
    for x in range(len(image[0])):
      if image[y][x] == '#':
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)

  paddedImage = []
  for y in range(minY - 3, maxY + 4):
    row = []
    paddedImage.append(row)
    for x in range(minX - 3, maxX + 4):
      outOfRange = y < minY or maxY < y or x < minX or maxX < x
      row.append(fill if outOfRange else image[y][x])

  return paddedImage

def getAlgorithmIndex(image, findX, findY, fill):
  bitStr = ''

  for y in range(findY - 1, findY + 2):
    for x in range(findX - 1, findX + 2):
      outOfRange = y < 0 or len(image) <= y or x < 0 or len(image[0]) <= x
      pixel = image[y][x] if not outOfRange else fill
      bitStr += '1' if pixel == '#' else '0'
  return int(bitStr, 2)

def enhanceImage(image, algorithm, fill):
  newImage = []
  for y in range(len(image)):
    row = []
    newImage.append(row)
    for x in range(len(image[0])):
      row.append(algorithm[getAlgorithmIndex(image, x, y, fill)])

  return newImage

def printImage(image):
  bright = '\033[1;36m'
  gray = '\033[90m'
  normal = '\033[0m'
  light = f'{bright}#{normal}'
  dark = f'{gray}.{normal}'

  for y in range(len(image)):
    for x in range(len(image[0])):
      print(light if image[y][x] == '#' else dark, end='')
    print('')

main()
