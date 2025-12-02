from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()

  answer = 0

  for line in lines:
    parts = line.split(': ')
    value = int(parts[0])
    numbers = [int(n) for n in parts[1].split(' ')]

    results = [numbers[0], numbers[0]]
    for i in range(1, len(numbers)):
      results = [
          *[result * numbers[i] for result in results],
          *[result + numbers[i] for result in results],
          *[int(str(result) + str(numbers[i])) for result in results],
      ]

    if value in results:
      answer += value

  print(answer)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
