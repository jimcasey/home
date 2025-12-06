from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()

  # Ensure all lines have the same length
  max_len = max(len(line) for line in lines)
  lines = [line.ljust(max_len) for line in lines]

  num_rows = len(lines)
  num_cols = len(lines[0])

  # Identify all-space columns (calculation separators)
  separators = []
  for col_idx in range(num_cols):
    is_all_space = all(lines[row][col_idx] == ' ' for row in range(num_rows))
    if is_all_space:
      separators.append(col_idx)

  # Split into calculation sections
  calculations = []
  start = 0
  for sep in separators:
    if start < sep:
      calculations.append((start, sep - 1))
    start = sep + 1
  if start < num_cols:
    calculations.append((start, num_cols - 1))

  total_sum = 0

  for calc_start, calc_end in calculations:
    # Find the operator for this calculation (first non-space in operator row)
    operator = None
    operator_row = lines[-1]
    for col_idx in range(calc_start, calc_end + 1):
      if operator_row[col_idx] != ' ':
        operator = operator_row[col_idx]
        break

    if operator is None:
      continue

    # Collect numbers by reading columns RTL
    numbers = []
    for col_idx in range(calc_end, calc_start - 1, -1):
      # Form a number from this column by concatenating digits from rows 0 to n-2
      digits = []
      for row_idx in range(num_rows - 1):
        char = lines[row_idx][col_idx]
        if char != ' ':
          digits.append(char)

      if digits:
        number = int(''.join(digits))
        numbers.append(number)

    # Apply operator to all numbers
    if numbers:
      result = numbers[0]
      for i in range(1, len(numbers)):
        if operator == '+':
          result = result + numbers[i]
        elif operator == '*':
          result = result * numbers[i]
        elif operator == '-':
          result = result - numbers[i]
        elif operator == '/':
          result = result / numbers[i]

      total_sum += result

  print(f"Sum of all results: {int(total_sum)}")


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
