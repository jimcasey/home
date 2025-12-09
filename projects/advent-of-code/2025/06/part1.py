from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()

  # Parse all lines except the last as numbers
  number_lines = []
  for i in range(len(lines) - 1):
    numbers = [int(x) for x in lines[i].split()]
    number_lines.append(numbers)

  # Parse the last line as operators
  operators = lines[-1].split()

  # For each column, apply the operator to all numbers in that column
  total_sum = 0
  num_cols = len(number_lines[0])

  for col_idx in range(num_cols):
    # Get all numbers in this column
    column_numbers = [row[col_idx] for row in number_lines]
    operator = operators[col_idx]

    # Apply the operator sequentially
    result = column_numbers[0]
    for i in range(1, len(column_numbers)):
      if operator == '+':
        result = result + column_numbers[i]
      elif operator == '*':
        result = result * column_numbers[i]
      elif operator == '-':
        result = result - column_numbers[i]
      elif operator == '/':
        result = result / column_numbers[i]

    total_sum += result

  print(f"Sum of all results: {total_sum}")


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
