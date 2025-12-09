from os import path
import math

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  points = parsePoints(lines)

  # Determine approach based on input size
  n = len(points)
  if n == 20:
    # Test data: target 11 circuits
    circuit_sizes = buildAndPartitionMST(points, 11, 'target_circuits')
  else:
    # Input data: process exactly 1000 shortest edges
    circuit_sizes = buildAndPartitionMST(points, 1000, 'max_edges')

  circuit_sizes.sort(reverse=True)

  print(f"\nCircuit sizes: {circuit_sizes}")

  if len(circuit_sizes) >= 3:
    result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    print(f"\nResult: {circuit_sizes[0]} × {circuit_sizes[1]} × {circuit_sizes[2]} = {result}")


def parsePoints(lines):
  """Parse lines into list of 3D points (tuples)"""
  points = []
  for line in lines:
    coords = list(map(int, line.split(',')))
    points.append(tuple(coords))
  return points


def distance(p1, p2):
  """Calculate Euclidean distance between two 3D points"""
  return math.sqrt(
    (p1[0] - p2[0]) ** 2 +
    (p1[1] - p2[1]) ** 2 +
    (p1[2] - p2[2]) ** 2
  )


def buildAndPartitionMST(points, param, mode='target_circuits'):
  """
  Build MST with two modes:
  - 'target_circuits': Process until exactly target_circuits remain
  - 'max_edges': Process exactly max_edges shortest connections
  Optimized to reduce memory usage by not storing point tuples in pairs list.
  """
  n = len(points)
  num_circuits = n

  # Union-Find data structure with path compression
  parent = {i: i for i in range(n)}
  size = {i: 1 for i in range(n)}

  def find(x):
    if parent[x] != x:
      parent[x] = find(parent[x])  # Path compression
    return parent[x]

  def union(i, j):
    nonlocal num_circuits
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
      # Union by size
      if size[root_i] < size[root_j]:
        parent[root_i] = root_j
        size[root_j] += size[root_i]
      else:
        parent[root_j] = root_i
        size[root_i] += size[root_j]
      num_circuits -= 1
      return True
    return False

  # Calculate all pairwise distances (optimized: only store dist, i, j)
  print(f"Calculating {n * (n-1) // 2} pairwise distances...")
  edges = []
  for i in range(n):
    for j in range(i + 1, n):
      dist = distance(points[i], points[j])
      edges.append((dist, i, j))

  print(f"Sorting {len(edges)} edges...")
  edges.sort()

  if mode == 'target_circuits':
    # Process edges until we reach target number of circuits
    print(f"Processing edges until {param} circuits remain...")
    edges_processed = 0
    for dist, i, j in edges:
      if num_circuits <= param:
        break
      if union(i, j):
        edges_processed += 1
    print(f"Processed {edges_processed} edges, {num_circuits} circuits formed")

  else:  # mode == 'max_edges'
    # Process exactly the first 'param' shortest edges
    print(f"Processing first {param} shortest edges...")
    edges_considered = 0
    edges_processed = 0
    for dist, i, j in edges:
      if edges_considered >= param:
        break
      edges_considered += 1
      if union(i, j):
        edges_processed += 1
    print(f"Considered {edges_considered} edges, successfully processed {edges_processed}, {num_circuits} circuits formed")

  # Count points in each component
  components = {}
  for i in range(n):
    root = find(i)
    if root not in components:
      components[root] = 0
    components[root] += 1

  return list(components.values())


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
