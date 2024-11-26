from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
pattern = r"(?=(\d|{}))".format("|".join(numbers.keys()))


def get_number(str):
  return numbers[str] if str in numbers else str


def main():
  lines = readInput()
  sum = 0
  for line in lines:
    matches = [match.group(1) for match in re.finditer(pattern, line) if match.group(1)]
    sum += int(get_number(matches[0]) + get_number(matches[-1]))

  print(sum)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
