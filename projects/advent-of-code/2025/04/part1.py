from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  grid = [list(line) for line in lines]

  if not grid:
    print(0)
    return

  rows = len(grid)
  cols = len(grid[0]) if rows > 0 else 0

  count = 0

  # Check each position in the grid
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == '@':
        # Count adjacent @ characters
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

        # Count if fewer than 4 adjacent @ characters
        if adjacent_count < 4:
          count += 1

  print(count)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
