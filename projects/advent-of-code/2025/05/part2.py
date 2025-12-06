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

  # Find all unique numbers covered by any range
  covered_numbers = set()
  for min_val, max_val in ranges:
    for num in range(min_val, max_val + 1):
      covered_numbers.add(num)

  print(f'Count of numbers in ranges: {len(covered_numbers)}')


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
