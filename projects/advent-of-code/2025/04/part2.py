from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def count_adjacent(grid, r, c, rows, cols):
  """Count adjacent @ characters for position (r, c)"""
  adjacent_count = 0

  # Check all 8 directions
  for dr in [-1, 0, 1]:
    for dc in [-1, 0, 1]:
      if dr == 0 and dc == 0:
        continue  # Skip the center position

      nr, nc = r + dr, c + dc

      # Check if the adjacent position is within bounds
      if 0 <= nr < rows and 0 <= nc < cols:
        if grid[nr][nc] == '@':
          adjacent_count += 1

  return adjacent_count


def main():
  lines = readInput()
  grid = [list(line) for line in lines]

  if not grid:
    print(0)
    return

  rows = len(grid)
  cols = len(grid[0]) if rows > 0 else 0

  total_removed = 0

  # Repeat until no more @ positions with < 4 neighbors
  while True:
    # Find all @ positions with fewer than 4 adjacent @ characters
    to_remove = []

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == '@':
          adjacent_count = count_adjacent(grid, r, c, rows, cols)

          if adjacent_count < 4:
            to_remove.append((r, c))

    # If no positions to remove, we're done
    if not to_remove:
      break

    # Remove all identified positions
    for r, c in to_remove:
      grid[r][c] = '.'

    total_removed += len(to_remove)

  print(total_removed)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
