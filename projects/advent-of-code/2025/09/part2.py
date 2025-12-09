from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def point_in_polygon(point, polygon):
  """Ray casting algorithm to check if point is inside or on polygon boundary"""
  x, y = point
  n = len(polygon)
  inside = False

  p1x, p1y = polygon[0]
  for i in range(1, n + 1):
    p2x, p2y = polygon[i % n]

    # Check if point is on the edge
    if is_on_segment(point, (p1x, p1y), (p2x, p2y)):
      return True

    # Ray casting algorithm
    if y > min(p1y, p2y):
      if y <= max(p1y, p2y):
        if x <= max(p1x, p2x):
          if p1y != p2y:
            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
            if p1x == p2x or x <= xinters:
              inside = not inside
    p1x, p1y = p2x, p2y

  return inside


def is_on_segment(point, seg_start, seg_end):
  """Check if point is on line segment"""
  px, py = point
  x1, y1 = seg_start
  x2, y2 = seg_end

  # Check if point is within bounding box
  if not (min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2)):
    return False

  # Check if point is collinear with segment
  cross = (py - y1) * (x2 - x1) - (px - x1) * (y2 - y1)
  return abs(cross) < 1e-9


def is_rectangle_inside_polygon(corner1, corner2, polygon):
  """Check if rectangle defined by two diagonal corners is inside polygon"""
  x1, y1 = corner1
  x2, y2 = corner2

  # Generate all 4 corners of the rectangle
  corners = [
    (min(x1, x2), min(y1, y2)),
    (max(x1, x2), min(y1, y2)),
    (min(x1, x2), max(y1, y2)),
    (max(x1, x2), max(y1, y2))
  ]

  # Check if all 4 corners are inside or on the polygon
  for corner in corners:
    if not point_in_polygon(corner, polygon):
      return False

  return True


def main():
  lines = readInput()
  polygon = []

  # Parse polygon vertices
  for line in lines:
    x, y = map(int, line.split(','))
    polygon.append((x, y))

  # Find the largest rectangle that fits inside the polygon
  max_area = 0
  best_pair = None

  for i in range(len(polygon)):
    for j in range(i + 1, len(polygon)):
      x1, y1 = polygon[i]
      x2, y2 = polygon[j]

      # Skip if points form a line (no area)
      if x1 == x2 or y1 == y2:
        continue

      # Check if rectangle is inside the polygon
      if is_rectangle_inside_polygon((x1, y1), (x2, y2), polygon):
        # Calculate area including the points themselves
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height

        if area > max_area:
          max_area = area
          best_pair = (polygon[i], polygon[j])

  print(f"Largest rectangle area inside polygon: {max_area}")
  if best_pair:
    print(f"Formed by points: {best_pair[0]} and {best_pair[1]}")


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
