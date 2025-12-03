from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def find_largest_k_digits(line, k):
  """Find the largest k-digit number from line without reordering digits."""
  n = len(line)
  if n < k:
    return line  # Can't get k digits from fewer than k characters

  result = []
  to_remove = n - k  # How many digits we can afford to skip

  for digit in line:
    # While we can still remove digits and current digit is better than last
    while result and to_remove > 0 and result[-1] < digit:
      result.pop()
      to_remove -= 1

    result.append(digit)

  # Return exactly k digits
  return ''.join(result[:k])


def main():
  lines = readInput()
  total = 0

  for line in lines:
    if not line:
      continue

    # Find the largest 12-digit number from the line
    largest_12_digits = find_largest_k_digits(line, 12)
    number = int(largest_12_digits)
    print(f"{line} -> {largest_12_digits} = {number}")
    total += number

  print(f"\nTotal: {total}")


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
