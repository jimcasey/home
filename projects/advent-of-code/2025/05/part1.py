from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()

  # Parse ranges and values
  ranges = []
  values = []
  parsing_ranges = True

  for line in lines:
    if line == '':
      parsing_ranges = False
      continue

    if parsing_ranges:
      # Parse range like "3-5"
      parts = line.split('-')
      min_val = int(parts[0])
      max_val = int(parts[1])
      ranges.append((min_val, max_val))
    else:
      # Parse value
      values.append(int(line))

  # Count good values
  good_count = 0
  for value in values:
    if is_in_any_range(value, ranges):
      good_count += 1

  print(f'Good values: {good_count}')


def is_in_any_range(value, ranges):
  for min_val, max_val in ranges:
    if min_val <= value <= max_val:
      return True
  return False


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
