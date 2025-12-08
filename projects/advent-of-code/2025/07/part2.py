from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'


def count_routes(lines, line_idx, pos, line_length):
  """
  Recursively count all possible routes from current position.

  Args:
    lines: The input grid
    line_idx: Current line index
    pos: Current beam position
    line_length: Width of the grid

  Returns:
    Number of possible routes from this state
  """
  # Base case: reached the end of the grid
  if line_idx >= len(lines):
    return 1

  # Out of bounds - this path is invalid
  if pos < 0 or pos >= line_length:
    return 0

  line = lines[line_idx]

  # Check if there's a splitter at this position
  if line[pos] == '^':
    # Beam can go either left or right
    routes = 0

    # Try going left (pos - 1)
    if pos > 0:
      routes += count_routes(lines, line_idx + 1, pos - 1, line_length)

    # Try going right (pos + 1)
    if pos < line_length - 1:
      routes += count_routes(lines, line_idx + 1, pos + 1, line_length)

    return routes
  else:
    # Beam continues at same position
    return count_routes(lines, line_idx + 1, pos, line_length)


def main():
  lines = readInput()

  # Find the starting position 'S' in the first line
  first_line = lines[0]
  start_pos = first_line.index('S')
  line_length = len(first_line)

  # Count all possible routes starting from line 1 (after the S)
  route_count = count_routes(lines, 1, start_pos, line_length)

  print(f'Number of possible routes: {route_count}')


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
