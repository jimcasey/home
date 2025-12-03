from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'


def main():
  lines = readInput()
  total = 0

  for line in lines:
    if not line:
      continue

    # Find the largest digit in the line, excluding the last character
    line_without_last = line[:-1]
    max_digit = max(line_without_last)

    # Find the first position of this largest digit
    first_pos = line.index(max_digit)

    # Get substring after the first occurrence of max_digit
    after_substring = line[first_pos + 1:]

    # Find the largest digit after that position (or 0 if nothing after)
    if after_substring:
      second_digit = max(after_substring)
    else:
      second_digit = '0'

    # Combine the two digits into a number
    number = int(max_digit + second_digit)
    print(f"{line} -> {max_digit}{second_digit} = {number}")
    total += number

  print(f"\nTotal: {total}")


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
