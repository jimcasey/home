from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  points = []

  # Parse coordinates
  for line in lines:
    x, y = map(int, line.split(','))
    points.append((x, y))

  # Find the largest rectangle area formed by any two points
  max_area = 0
  best_pair = None

  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      x1, y1 = points[i]
      x2, y2 = points[j]

      # Calculate area of rectangle with these two points as corners
      # Include the points themselves in the count
      width = abs(x2 - x1) + 1
      height = abs(y2 - y1) + 1
      area = width * height

      if area > max_area:
        max_area = area
        best_pair = (points[i], points[j])

  print(f"Largest rectangle area: {max_area}")
  if best_pair:
    print(f"Formed by points: {best_pair[0]} and {best_pair[1]}")


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
