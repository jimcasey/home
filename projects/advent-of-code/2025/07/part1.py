from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()

  # Find the starting position 'S' in the first line
  first_line = lines[0]
  beam_positions = {first_line.index('S')}

  split_count = 0
  line_length = len(first_line)

  # Process each subsequent line
  for line in lines[1:]:
    # Early termination if no beams remain
    if not beam_positions:
      break

    new_beam_positions = set()

    for pos in beam_positions:
      # Only process beams within valid bounds
      if pos < 0 or pos >= line_length:
        continue

      # Check if there's a splitter at this position
      if line[pos] == '^':
        # Beam splits
        split_count += 1
        # Create beams at previous and next positions (bounds checked when added)
        if pos > 0:
          new_beam_positions.add(pos - 1)
        if pos < line_length - 1:
          new_beam_positions.add(pos + 1)
      else:
        # Beam continues at same position
        new_beam_positions.add(pos)

    # Merge beams (set automatically handles duplicates)
    beam_positions = new_beam_positions

  print(f'Number of splits: {split_count}')


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
