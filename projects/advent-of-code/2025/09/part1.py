from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  points = set()

  # Parse all points
  for line in lines:
    x, y = map(int, line.split(','))
    points.add((x, y))

  print(f"Total points: {len(points)}")

  max_area = 0
  best_pair = None

  # Convert to list for iteration
  point_list = list(points)
  n = len(point_list)

  # # Debug: print all distances
  # all_distances = []
  # for i in range(n):
  #   for j in range(i + 1, n):
  #     x1, y1 = point_list[i]
  #     x2, y2 = point_list[j]
  #     dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
  #     all_distances.append((dist_sq, (x1, y1), (x2, y2)))

  # all_distances.sort()
  # print("All squared distances:")
  # for dist_sq, p1, p2 in all_distances:
  #   print(f"  {dist_sq}: {p1} to {p2}")

  # Try all pairs of points as one SIDE of a square
  # The side length determines the square area
  for i in range(n):
    for j in range(i + 1, n):
      x1, y1 = point_list[i]
      x2, y2 = point_list[j]

      # Calculate side length squared (this will be the area)
      side_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2

      if side_sq > max_area:
        max_area = side_sq
        best_pair = [(x1, y1), (x2, y2)]

  print(f"Maximum area: {max_area}")


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
