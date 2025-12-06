from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()

  # Parse ranges only (ignore values section)
  ranges = []

  for line in lines:
    if line == '':
      # Stop parsing when we hit the empty line
      break

    # Parse range like "3-5"
    parts = line.split('-')
    min_val = int(parts[0])
    max_val = int(parts[1])
    ranges.append((min_val, max_val))

  # Merge overlapping ranges and count total numbers
  merged_ranges = merge_ranges(ranges)

  # Count numbers in merged ranges using arithmetic
  total_count = 0
  for min_val, max_val in merged_ranges:
    total_count += (max_val - min_val + 1)

  print(f'Count of numbers in ranges: {total_count}')


def merge_ranges(ranges):
  """Merge overlapping ranges to avoid double-counting."""
  if not ranges:
    return []

  # Sort ranges by start value
  sorted_ranges = sorted(ranges)
  merged = [sorted_ranges[0]]

  for current_min, current_max in sorted_ranges[1:]:
    last_min, last_max = merged[-1]

    # Check if current range overlaps or is adjacent to last merged range
    if current_min <= last_max + 1:
      # Merge by extending the last range
      merged[-1] = (last_min, max(last_max, current_max))
    else:
      # No overlap, add as new range
      merged.append((current_min, current_max))

  return merged


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
